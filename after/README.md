# Groq API Python Example

This project demonstrates how to make a REST call to the Groq API using Python.

## Setup Instructions (Windows)
```
$env:GROQ_API_KEY="your_actual_api_key"
 
```
### 1. Clone the repository
```
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment (recommended)
```
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Set your Groq API key
- Open `main.py`.
- Replace `YOUR_GROQ_API_KEY` with your actual Groq API key.

### 5. Run the script
```
python after\main.py
```

## Notes
- Make sure you have Python 3.7 or higher installed.
- The script uses the `requests` library for HTTP calls.
- The `poml` package is listed in requirements.txt but is not used in the example. Remove it if not needed.

---

Feel free to modify the prompt or model in `main.py` as needed.
