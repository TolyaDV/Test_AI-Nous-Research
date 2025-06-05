**The script is intended for testing AI Nous Research.**

Its operation is simple: ChatGPT generates a question for Nous, Nous responds, and the cycle repeats.

To run the script, you need to configure config.py:

- Add the API key from Nous Research - https://portal.nousresearch.com/api-keys
- Add the API key from ChatGPT
- You can also add a proxy (optional) – format: "http://user:pass@ip:port"
- "TIME_SLEEP"- sets the pause duration (in seconds) between the question-response cycles
- "NOUS_AI_MODEL" - You can also change the AI model for testing, as listed on their website

To run the script, create and activate a virtual environment and install the dependencies:

python -m venv .venv  
.venv\Scripts\activate  
pip install -r requirements.txt 


After everything is set up, you can launch the script with:

python main.py
