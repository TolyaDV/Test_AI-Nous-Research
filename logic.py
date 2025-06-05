import requests

from config import API_KEY_GPT, API_KEY_NOUS, BASIC_PROMPT_FOR_GPT, NOUS_AI_MODEL
from logger import logger


def requests_function(url: str, headers: dict, data: dict, proxy: str | None = None) -> str | None:

    """Function for creating API requests"""
    
    try:
        if proxy:
            proxy = {"http": proxy}
            response = requests.post(url=url, headers=headers, json=data, proxies=proxy, timeout=15).json()
        else:
            response = requests.post(url=url, headers=headers, json=data, timeout=15).json()
        
        return response['choices'][0]['message']['content']
    
    except ValueError as error:
        logger.error(f"Invalid JSON")
    except requests.HTTPError:
        logger.error(f"HTTP error")
    except TimeoutError as tmerror:
        logger.error(f"Timeoute error | {tmerror}")
    except Exception as error:
        logger.error(f"Unexpected error | {error}")
        
    return None


def generate_question_from_gpt(prompt: str = "start", proxy: str = None) -> str | None:
    
    """Function for forming a request to the GPT API"""
    
    api_url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
    "Authorization": f"Bearer {API_KEY_GPT}",
    "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4", 
        "messages": [
            {"role": "system", "content": BASIC_PROMPT_FOR_GPT},
            {"role": "user", "content": str(prompt)}
        ],
        "temperature": 0.7
    }
    
    return requests_function(url=api_url, headers=headers, data=data, proxy=proxy)
    

def generate_answer_from_nous(prompt: str, proxy: str = None) -> str | None:
    
    """Function for forming a request to the Nous API"""
    
    api_url = "https://inference-api.nousresearch.com/v1/chat/completions"    
    
    headers = {
            "Authorization": f"Bearer {API_KEY_NOUS}",        
            "Content-Type": "application/json"    
    }    
    
    data = {
        "model": NOUS_AI_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},            
            {"role": "user", "content": prompt}        
        ],        
        "max_tokens": 4096  
    }  
    
    return requests_function(url=api_url, headers=headers, data=data, proxy=proxy)


def check_requests(resp: str | None) -> Exception | str:
    
    """Function for checking the result of the request"""
    
    if not resp:
        raise RuntimeError("Failed to generate request. Exiting.")

    return "-" * 25
         