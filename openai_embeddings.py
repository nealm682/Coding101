
'''
Description: This script demonstrates how to use the OpenAI API to interact with the embeddings model.
Set openai API key:
    Reference: https://platform.openai.com/docs/quickstart?desktop-os=macOS&quickstart-example=completions&language-preference=python
    Set virtual environment: python -m venv venv
    Activate virtual environment: Mac: source venv/bin/activate    Windows: cd venv\Scripts\activate
    Install OpenAI: pip install openai
    CLI - set key for Windows: setx OPENAI_API_KEY "your_api_key_here"
    CLI - set key for MAC: export OPENAI_API_KEY="your_api_key_here"
    CLI - run: MAC: python3 openai_embeddings.py   WINDOWS: python openai_embeddings.py

'''

from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)

print(response)