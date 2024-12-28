Here is a single, complete README markdown file for you to copy and paste:

```markdown
# OpenAI API Beginner Guide

This repository is designed to help beginner programmers learn how to access and interact with OpenAI's three primary APIs: **Chat Completions**, **Image Generation**, and **Embeddings**. Each script demonstrates how to set up your environment and use the respective API model.

---

## Prerequisites

Before running the scripts, ensure the following:

1. **Python Installed**: Version 3.7 or higher.
2. **API Key**: Obtain your OpenAI API key from [OpenAI Platform](https://platform.openai.com/).
3. **Virtual Environment**: Set up a Python virtual environment for dependency management.

---

## Setup Instructions

### 1. Set up a Virtual Environment
- Create a virtual environment:
  ```bash
  python -m venv venv
  ```
- Activate the virtual environment:
  - **Mac/Linux**:
    ```bash
    source venv/bin/activate
    ```
  - **Windows**:
    ```cmd
    venv\Scripts\activate
    ```

### 2. Install Dependencies
Install the `openai` Python package:
```bash
pip install openai
```

### 3. Set Your OpenAI API Key
- **Windows**:
  ```cmd
  set OPENAI_API_KEY=your_api_key_here
  ```
- **Mac/Linux**:
  ```bash
  export OPENAI_API_KEY=your_api_key_here
  ```

---

## Scripts Overview

### **1. Chat Completions Script**
This script demonstrates how to interact with the **GPT-4o-mini** model to perform chat completions.

**File**: `openai_text.py`  
**Run**:
- **Mac/Linux**:
  ```bash
  python3 openai_text.py
  ```
- **Windows**:
  ```cmd
  python openai_text.py
  ```

**Example Code**:
```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about the Cleveland Browns' 2022 season."}
    ]
)

response_text = completion.choices[0].message.content
print('Parsed response:', response_text)
```

---

### **2. Image Generation Script**
This script demonstrates how to generate images using the OpenAI API's **Image Generation** model.

**File**: `openai_image.py`  
**Run**:
- **Mac/Linux**:
  ```bash
  python3 openai_image.py
  ```
- **Windows**:
  ```cmd
  python openai_image.py
  ```

**Example Code**:
```python
from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt="A cute baby sea otter",
    n=2,
    size="1024x1024"
)

print(response.data[0].url)
```

---

### **3. Embeddings Script**
This script demonstrates how to use the OpenAI API's **Embeddings** model for creating vector embeddings.

**File**: `openai_embeddings.py`  
**Run**:
- **Mac/Linux**:
  ```bash
  python3 openai_embeddings.py
  ```
- **Windows**:
  ```cmd
  python openai_embeddings.py
  ```

**Example Code**:
```python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    model="text-embedding-3-large",
    input="The food was delicious and the waiter..."
)

print(response)
```

---

## Reference Documentation
- OpenAI API Quickstart Guide: [Link](https://platform.openai.com/docs/quickstart)

---

## Troubleshooting

- Ensure your OpenAI API key is correctly set.
- If you encounter errors, check your Python version and virtual environment setup.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

You can now paste this into your `README.md` file. Let me know if you need further assistance!