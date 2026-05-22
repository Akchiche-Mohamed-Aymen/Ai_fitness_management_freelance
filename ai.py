from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
chat =  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  
    max_tokens=100,
    timeout=None,
    api_key= GEMINI_KEY,
    max_retries=2
) 
