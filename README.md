**Script for Testing AI NousResearch**

The logic is simple: GPT asks a question, Nous answers, and this goes in a loop.

**First, set up config.py:**

- GPT API key
- Nous AI API key — get it here: https://portal.nousresearch.com/api-keys
- GPT version — by default, the most cost-effective one is set
- Nous version — you can change it as you like; all versions are listed on the project’s main page
- TIME_SLEEP — pause time in seconds between each question-answer cycle

**How to run:**

- Create a virtual environment: python -m venv .venv
- Activate it: .venv\Scripts\activate (on Windows)
- Install dependencies: pip install -r requirements.txt
- Run the script: python main.py
