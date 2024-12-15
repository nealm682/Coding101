
'''
Description: This script demonstrates how to use the OpenAI API to interact with the image generation model.
Set openai API key:
    Reference: https://platform.openai.com/docs/quickstart?desktop-os=macOS&quickstart-example=completions&language-preference=python
    Set virtual environment: python -m venv venv
    Activate virtual environment: Mac: source venv/bin/activate    Windows: cd venv\Scripts\activate
    Install OpenAI: pip install openai
    CLI Windows: setx OPENAI_API_KEY "your_api_key_here"
    CLI MAC: export OPENAI_API_KEY="your_api_key_here"
    RUN: MAC: python3 openai_image.py   WINDOWS: python openai_image.py

'''

from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)