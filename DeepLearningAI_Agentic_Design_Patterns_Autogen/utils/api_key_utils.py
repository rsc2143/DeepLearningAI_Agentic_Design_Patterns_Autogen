from dotenv import load_dotenv
import os
load_dotenv()

def get_openai_api_key():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    print("OPENAI API KEY Exported")
    # print(openai_api_key)
    return openai_api_key 

# if __name__ == "__main__":
#     get_openai_api_key()