from fastapi import APIRouter, Request, HTTPException, Depends
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from authlib.integrations.starlette_client import OAuth
from core.config import settings
from sqlalchemy.orm import Session
from db.database import get_db
from controllers.user import get_user, create_user, update_user
import jwt
import secrets

router = APIRouter()

# Initialize OAuth
oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={'scope': 'openid profile email'}
)


@router.get("/auth/login")
async def login(request: Request):
    try:
        state = secrets.token_urlsafe(16)
        request.session['oauth_state'] = state
        redirect_uri = request.url_for('auth_callback')
        return await oauth.google.authorize_redirect(request, redirect_uri, state=state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Login Error: {str(e)}")


@router.get("/auth/callback")
async def auth_callback(request: Request, db: Session = Depends(get_db)):
    try:
        state = request.query_params.get('state')
        saved_state = request.session.get('oauth_state')

        if state != saved_state:
            raise HTTPException(
                status_code=400, detail="Invalid state parameter.")

        token = await oauth.google.authorize_access_token(request)
        id_token = token.get('id_token')
        user_info = jwt.decode(id_token, options={"verify_signature": False})

        db_user = get_user(db, user_info['sub'])

        if db_user:
            db_user = update_user(db, user_info['sub'], user_info)
        else:
            db_user = create_user(db, user_info)

        request.session['user'] = dict(user_info)
        return RedirectResponse(url='/welcome')
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Callback Error: {str(e)}")


@router.get("/welcome")
async def welcome(request: Request):
    user = request.session.get('user')
    if not user:
        return RedirectResponse(url='/')
    return HTMLResponse(f"""
    <html>
        <head>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                }}
                .container {{
                    text-align: center;
                }}
                a {{
                    font-size: 24px;
                    text-decoration: none;
                    color: #ffffff;
                    background-color: #4285F4;
                    padding: 15px 30px;
                    border-radius: 5px;
                    margin-top: 100px; 
                    transition: background-color 0.3s;
                }}
                a:hover {{
                    background-color: #357ae8;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome {user.get('name', 'User')}!</h1>
                <p>Email: {user.get('email', 'Not provided')}</p>
                <a href="/logout">Logout</a>
            </div>
        </body>
    </html>

    """)


@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url='/')
