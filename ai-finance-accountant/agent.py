import os
from openai import OpenAI

# Set the OpenAI API key directly in this file or fetch from environment variables
os.environ["OPENAI_API_KEY"] = "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"

# Fetch the API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client with the API key
client = OpenAI(api_key=openai_api_key)

def query_agent(prompt):
    try:
        # Call the OpenAI API to get a response based on the prompt
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        # Return the content of the response
        return response.choices[0].message.content
    except Exception as e:
        # Handle potential API errors
        return f"Error occurred while querying the agent: {e}"
