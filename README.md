# Build Your First AI App: A Simple Fact Generator with Python, LangChain, and Gemini

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-b5002a)](https://www.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Welcome! This repository contains the code for a simple but fun command-line application that uses **Google's powerful Gemini 1.5 Flash model** to generate interesting facts on any topic you choose. It's built with Python and the popular **LangChain** framework.

This project is designed to be a perfect starting point for developers new to building applications with Large Language Models (LLMs). By following the steps below, you will have a working Python application and a solid understanding of the basic components of a LangChain application.

## ✨ Features

*   **Interactive CLI:** A simple and intuitive command-line interface.
*   **Powered by Google Gemini:** Leverages the speed and power of the `gemini-1.5-flash` model.
*   **Built with LangChain:** Demonstrates the basic building blocks of the LangChain framework, including prompt templates and model chaining.
*   **Easy to Set Up:** Get up and running in just a few minutes with minimal dependencies.

## 🚀 Demo

Here is a quick look at the application in action:

```
$ python app.py
Welcome to the Simple LangChain Application!

Enter a topic (or 'q' to quit): The planet Mars
Thinking...

Fact: Mars has the largest dust storms in the solar system. They can last for months and cover the entire planet.

Enter a topic (or 'q' to quit): q
Goodbye!
```

## ✅ What You'll Need

Before you begin, ensure you have the following:

*   **Python 3.7+**
*   A **Google AI Studio API Key**. You can obtain one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).
*   Basic knowledge of using the command line.

## 🛠️ Step 1: Setting Up Your Project

Follow these steps to get the project environment set up on your local machine.

**1. Clone the Repository:**

```bash
git clone https://github.com/sanketbisne/Langchain-app.git
cd Langchain-app
```

**2. Create and Activate a Virtual Environment:**

It is highly recommended to use a virtual environment to manage project-specific dependencies.

*   **On macOS/Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
*   **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

**3. Install the Dependencies:**

Install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

**4. Configure Your API Key:**

Your API key needs to be stored securely as an environment variable.

*   First, make a copy of the example environment file:
    ```bash
    cp .env.example .env
    ```
*   Next, open the newly created `.env` file and replace the placeholder text with your actual Google AI Studio API key.

    ```
    # .env
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
This file is listed in our `.gitignore` file, so your secret key won't be accidentally committed to source control.

## 🐍 Step 2: Understanding the Code

The main logic resides in the `app.py` file. Here is the full source code:

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

def main():
    print("Welcome to the Simple LangChain Application!")

    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY environment variable not found.")
        print("Please copy .env.example to .env and add your API key.")
        return

    # Initialize the LLM (Google's Gemini 1.5 Flash)
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

    # Create a simple prompt template
    prompt_template = PromptTemplate.from_template(
        "Tell me a short, interesting fact about {topic}."
    )

    # Create the chain using the new runnable syntax
    chain = prompt_template | llm

    while True:
        try:
            topic = input("\nEnter a topic (or 'q' to quit): ").strip()

            if topic.lower() == 'q':
                print("Goodbye!")
                break

            if not topic:
                continue

            print("Thinking...")
            # Invoke the chain
            response = chain.invoke({"topic": topic})

            print(f"\nFact: {response.content}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
```

### How it Works

1.  **Imports and Loading:** We import the necessary classes from our libraries and call `load_dotenv()` to load our `GOOGLE_API_KEY` from the `.env` file.
2.  **Initializing the LLM:** We create an instance of `ChatGoogleGenerativeAI`, specifying `gemini-1.5-flash` as our model. The `temperature` parameter controls the creativity of the model's responses.
3.  **Creating a Prompt Template:** A `PromptTemplate` is a powerful LangChain feature that allows us to create reusable prompts with dynamic inputs. Here, we create a simple template that expects a `topic` variable.
4.  **Creating the Chain:** This is the core of our LangChain application. We use the `|` (pipe) operator to chain our `prompt_template` and `llm` together. This creates a "runnable sequence" where the output of the prompt template is directly fed as input to the language model.
5.  **The Main Loop:** The application enters a loop, asks the user for a topic, and then `invokes` the chain with the provided topic. The LLM generates a response, and we print the `content` of that response.

## ▶️ Step 3: Running Your Application

Once you have completed the setup, you can run the application with a single command:

```bash
python app.py
```

The application will prompt you to enter a topic. To exit, type `q` and press Enter.

## 🚀 Next Steps & Contributing

Congratulations on getting the application running! From here, you could:

*   **Try a different model:** Swap out `gemini-1.5-flash` for another model and see how the responses change.
*   **Build a web interface:** Use a framework like Flask or FastAPI to create a web-based UI for your fact generator.
*   **Explore more complex chains:** LangChain offers many ways to build more sophisticated applications with memory, data sources, and agent-like behaviors.

Contributions are welcome! If you have ideas for improvements, please fork the repository and submit a pull request.

## 📄 License

This project is distributed under the MIT License.
