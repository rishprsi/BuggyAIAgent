from google import genai
import os
from dotenv import load_dotenv
from google.genai import types

load_dotenv()
def call_llm(user_prompt="",debug_mode = False):
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("MODEL")
    client = genai.Client(api_key=api_key)
    
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]
    
    result = client.models.generate_content(model=model,contents=messages)
    print(result.text)
    if (debug_mode):
        prompt_tokens = result.usage_metadata.prompt_token_count
        cand_tokens = result.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {cand_tokens}")
