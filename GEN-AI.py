# gen_ai.py
import openai

# Initialize the OpenAI API
openai.api_key = 'your-openai-api-key'

def generate_feedback(input_text):
    # Use the OpenAI API to generate feedback based on the input
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Give constructive feedback on the following soft skill aspect: {input_text}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    feedback = response.choices[0].text.strip()
    return feedback
