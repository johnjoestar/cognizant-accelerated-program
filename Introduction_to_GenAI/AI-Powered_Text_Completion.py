from openai import OpenAI
import os

openapi_key = os.getenv("OPENAI_API_KEY")
if not openapi_key:
    raise ValueError("Missing OpenAI API Key. Set 'OPENAI_API_KEY' as an environment variable")

client = OpenAI(api_key=openapi_key)

def generate_text(prompt):
    if not prompt.strip():
        return "Error: Prompt cannot be empty. Please enter a valid prompt"
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=100
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("AI-Powered Text Completion")
    print("Type 'exit' to quit the application")

    while True:
        user_input = input("Enter your prompt: ")
        if user_input.lower() == "exit":
            print("Exiting the application. Goodbye!")
            break

        try:
            temp = float(input("Set creativity (temperature) [0.0 - 1.0]: "))
        except ValueError:
            temp = 0.7

        try:
            length = int(input("Set max response length (tokens): "))
        except ValueError:
            length = 150


        response = generate_text(user_input)
        print("\nAI Response:\n", response, "\n")

