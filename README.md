# Llama Groq Chat 

## 1. Create Python enviroment

`virtualenv .venv`

## 2. Install requirements

`pip install -r requirements.txt`

## 3. Create env variables:

`cp .env_template .env`

## 4. Add your key into the .env file
The .env file will store your API key for Groq. Update the file with your Groq API key:

`GROQ_API_KEY=your_groq_api_key_here`

## 5. Run Streamlit

`streamlit run ./chat-groq.py`