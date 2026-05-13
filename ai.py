from langchain_google_genai import ChatGoogleGenerativeAI
from key import GEMINI_KEY

chat =  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=100,
    timeout=None,
    api_key= GEMINI_KEY,
    max_retries=2
) 