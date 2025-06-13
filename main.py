#
from colorama import init, Fore, Style

import random
import time 

from config import TIME_SLEEP, PROXY
from logger import logger
from logic import generate_answer_from_nous, generate_question_from_gpt, check_requests


init(autoreset=True)

BLUE = Fore.BLUE + Style.BRIGHT
WHITE = Fore.WHITE + Style.NORMAL
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT


def main():

        try:  
            question = generate_question_from_gpt(proxy=PROXY)
            check_requests(resp=question)
            
            answer = generate_answer_from_nous(prompt=question, proxy=PROXY)
            check_requests(resp=answer)
        except Exception:
                logger.error(f"{RED}Failed to generate request. Start new request")
        
        
        while True:
            try:
                question = generate_question_from_gpt(prompt=answer, proxy=PROXY)
                logger.info(f"{BLUE}GPT QUESTION || {WHITE}{Fore.WHITE + question}\n{BLUE}{check_requests(resp=question)}")
                answer = generate_answer_from_nous(prompt=question, proxy=PROXY)
                logger.info(f"{GREEN}NOUS ANSWER || {WHITE}{answer}\n{GREEN}{check_requests(resp=answer)}")

            except Exception:
                logger.error(f"{RED}Failed to generate request. Start new request")

            time.sleep(random.randint(*TIME_SLEEP))
        

if __name__ == "__main__":
        main()