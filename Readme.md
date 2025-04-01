
# Logic Wise Coding Assistant

A web application built using Vite React for the frontend and Flask for the backend.

## Table of Contents
- [Installation](#installation)
- [Frontend Setup](#frontend-setup)
- [Backend Setup](#backend-setup)
- [Running the Application](#running-the-application)
- [License](#license)

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Node.js and npm
- Python 3.x and pip
- Firebase account (for API key generation)
- Groq API key

## Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Generate a Firebase API key from the Firebase console.
4. Create a `dbconfig.js` file inside the `config` folder and add the Firebase API key:
   ```js
   // config/dbconfig.js
   export const firebaseConfig = {
       apiKey: "YOUR_FIREBASE_API_KEY"
   };
   ```

## Backend Setup

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root backend directory and add your Groq API key and chat completions URL:
   ```sh
   GROQ_KEY=your_groq_api_key
   GROQ_URL=your_groq_chat_completions_url
   ```

## Running the Application

### Start the Backend
```sh
cd backend
flask run
```

### Start the Frontend
```sh
cd frontend
npm run dev
```

The frontend should now be running on `http://localhost:5173` and the backend on `http://localhost:5000`.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

