AI LAB 6 - TASK 1
Tokenization and FAQ Chatbot

FILES
1. task1_tokens.py     Tokenization comparison
2. lab6_search.py      TF-IDF search helper
3. guided_chatbot.py   Interactive FAQ chatbot
4. requirements.txt    Required Python libraries

SETUP
1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Create a virtual environment:
   python -m venv .venv

5. Activate it on Windows PowerShell:
   .venv\Scripts\Activate.ps1

   If PowerShell blocks activation, use Command Prompt and run:
   .venv\Scripts\activate.bat

6. Install the required libraries:
   python -m pip install -r requirements.txt

RUN TOKENIZATION
   python task1_tokens.py

RUN CHATBOT
   python guided_chatbot.py

Type exit to stop the chatbot.

NOTE
The sentence-transformers package is optional for the basic Task 1 work.
If installed, its first run downloads the model and requires internet access.
The FAQ chatbot uses TF-IDF and runs locally.
