'''
Description: This script demonstrates how to use the OpenAI API to interact with the GPT-4o-mini model for chat completions.
Set openai API key:
    Reference: https://platform.openai.com/docs/quickstart?desktop-os=macOS&quickstart-example=completions&language-preference=python
    Set virtual environment: python -m venv venv
    Activate virtual environment: Mac: source venv/bin/activate    Windows: cd venv\Scripts\activate
    Install OpenAI: pip install openai
    CLI Windows: set OPENAI_API_KEY=your_api_key_here
    CLI MAC: export OPENAI_API_KEY=your_api_key_here
    RUN: MAC: python3 openai_text.py   WINDOWS: python openai_text.py
'''



from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Tell me about the Cleveland Browns' 2022 season."
        }
    ]
)

# Extract the assistant's response text
response_text = completion.choices[0].message.content

print('Parsed response:', response_text)
