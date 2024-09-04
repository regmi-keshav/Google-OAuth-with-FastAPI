<!-- # Google-OAuth-with-FastAPI

---

It is a FastAPI application that implements Google Sign-In functionality. Users can authenticate via Google, and the application will handle both new user registrations and existing user logins. User information is stored in a PostgreSQL database.

## Features

- Google Sign-In integration
- User registration and login
- Session management
- Basic HTML frontend for login

## Project Structure

```
Google-OAuth-with-FastAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Entry point for the FastAPI application
│   ├── api/
│   │   ├── __init__.py
│   │   └── user.py        # Routes and endpoint logic for user-related operations
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py      # Configuration settings (e.g., environment variables)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py        # Database model for users
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user.py        # CRUD operations for user data
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py    # Database connection and setup
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/regmi-keshav/Google-OAuth-with-FastAPI.git
   cd Google-OAuth-with-FastAPI
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the root directory of your project and add your environment variables. Here is a sample `.env` file:**

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   SESSION_SECRET_KEY=your-session-secret-key
   ```

6. **Initialize the database:**

   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

1. **Start the FastAPI application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **Open your browser and go to `http://127.0.0.1:8000`.** You should see a login page with a button to log in using Google.

3. **Click the "Login with Google" button** to start the authentication process. If you're a new user, your information will be registered in the database. If you're an existing user, you will be logged in and redirected to the welcome page.

## Additional Notes

- **Token Decoding**: Currently, JWT decoding is performed without signature verification. For production, consider using proper signature verification.

- **Error Handling**: Ensure that all potential errors are properly managed and logged for better debugging.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. -->

---

# Google-OAuth-with-FastAPI

---

It is a FastAPI application that implements Google Sign-In functionality. Users can authenticate via Google, and the application will handle both new user registrations and existing user logins. User information is stored in a PostgreSQL database.

## Features

- Google Sign-In integration
- User registration and login
- Session management
- Basic HTML frontend for login

## Project Structure

```
Google-OAuth-with-FastAPI/
│
├── app/
│   ├── __init__.py
│   ├── main.py            # Entry point for the FastAPI application
│   ├── api/
│   │   ├── __init__.py
│   │   └── user.py        # Routes and endpoint logic for user-related operations
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py      # Configuration settings (e.g., environment variables)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py        # Database model for users
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── user.py        # CRUD operations for user data
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py    # Database connection and setup
├── .env                   # Environment variables
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/regmi-keshav/Google-OAuth-with-FastAPI.git
   cd Google-OAuth-with-FastAPI
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Create a `.env` file in the root directory of your project and add your environment variables. Here is a sample `.env` file:**

   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/yourdatabase
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   REDIRECT_URI=http://localhost:8000/auth/callback
   SESSION_SECRET_KEY=your-session-secret-key
   ```

6. **Initialize the database:**

   ```bash
   uvicorn app.main:app --reload
   ```

## Getting OAuth Credentials

To integrate Google Sign-In, you'll need to obtain OAuth credentials from Google. Follow these steps to create and configure your OAuth credentials:

1. **Go to the Google Cloud Console:**

   Navigate to the [Google Cloud Console](https://console.cloud.google.com/).

2. **Create a New Project:**

   - Click on the project dropdown in the top-left corner and select "New Project."
   - Enter a project name and select an organization (if applicable), then click "Create."

3. **Enable the Google+ API (or Google Identity Services):**

   - In the Google Cloud Console, go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
   - Click "Enable APIs and Services."
   - Search for "Google+ API" or "Google Identity Services" and enable it.

4. **Configure OAuth Consent Screen:**

   - Go to the [OAuth consent screen](https://console.cloud.google.com/apis/credentials/consent) tab in the Google Cloud Console.
   - Select "External" for the user type and click "Create."
   - Fill in the required fields, including App name, User support email, and Developer contact email.
   - Save your changes.

5. **Create OAuth 2.0 Credentials:**

   - Go to the [Credentials](https://console.cloud.google.com/apis/credentials) tab in the Google Cloud Console.
   - Click "Create Credentials" and select "OAuth 2.0 Client IDs."
   - Configure the OAuth consent screen settings.
   - Choose "Web application" as the application type.
   - Set the "Authorized redirect URIs" to `http://localhost:8000/auth/callback` (or the appropriate URI for your application).
   - Click "Create."

6. **Obtain Your Client ID and Client Secret:**

   - Once created, you will see a dialog with your OAuth 2.0 Client ID and Client Secret.
   - Copy these values and add them to your `.env` file:

     ```env
     GOOGLE_CLIENT_ID=your-google-client-id
     GOOGLE_CLIENT_SECRET=your-google-client-secret
     ```

## Usage

1. **Start the FastAPI application:**

   ```bash
   uvicorn app.main:app --reload
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **Open your browser and go to `http://127.0.0.1:8000`.** You should see a login page with a button to log in using Google.

3. **Click the "Login with Google" button** to start the authentication process. If you're a new user, your information will be registered in the database. If you're an existing user, you will be logged in and redirected to the welcome page.

## Additional Notes

- **Token Decoding**: Currently, JWT decoding is performed without signature verification. For production, consider using proper signature verification.

- **Error Handling**: Ensure that all potential errors are properly managed and logged for better debugging.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

---
