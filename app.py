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
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

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
