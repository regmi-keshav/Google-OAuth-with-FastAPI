from fastapi import FastAPI
from api import user
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from db.database import init_db

app = FastAPI()

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ucall.services"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SESSION_SECRET_KEY,
    session_cookie="google_oauth_session"
)

# Initialize database on startup


@app.on_event("startup")
async def startup_event():
    init_db()

# Include routers
app.include_router(user.router)

# Root endpoint for basic health check or welcome message


@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login Page</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f4f4f4;
                font-family: Arial, sans-serif;
            }
            a {
                font-size: 24px;
                text-decoration: none;
                color: #ffffff;
                background-color: #4285F4;
                padding: 15px 30px;
                border-radius: 5px;
                transition: background-color 0.3s;
            }
            a:hover {
                background-color: #357ae8;
            }
        </style>
    </head>
    <body>
        <a href="/auth/login">Login with Google</a>
    </body>
    </html>
    """
