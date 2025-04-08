from openai import openai

openai.api_key = "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"  

try:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Hello, how are you?",
        max_tokens=5
    )
    print("API Key is valid. Response:", response.choices[0].text.strip())

except openai.error.AuthenticationError:
    print("Invalid API Key!")
except Exception as e:
    print(f"Error occurred: {e}")
