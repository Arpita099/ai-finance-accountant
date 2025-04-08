import os
from agent import query_agent
from voice_module import listen, speak
from finance_api import process_command
from retriever import retrieve_context

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "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"

def main():
    speak("How can I help you with your finances today?")
    command = listen()
    print("Command received:", command)

    if "sorry" in command or "catch" in command:  # Check if we got an error message from speech recognition
        response = "Sorry, I didn't catch that. Can you please repeat your request?"
    elif "guide" in command:
        context = retrieve_context(command)
        prompt = f"Based on this context: {context}\nAnswer this: {command}"
        response = query_agent(prompt)
    elif "transaction" in command:
        response = process_command(command)
    else:
        response = "Sorry, I didn't understand that. Can you please clarify?"

    print("Response:", response)
    speak(response)

if __name__ == "__main__":
    main()
