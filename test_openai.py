import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def test_openai():
    try:
        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'Say hello!'}
            ],
            max_tokens=50,
        )
        print('✅ OpenAI API is working!')
        print('Response:', response.choices[0].message.content)
    except Exception as e:
        print('❌ Error:', e)

if __name__ == '__main__':
    test_openai()
