import os
import requests

API_KEY = os.getenv('DEEPSEEK_API_KEY', 'your_api_key_here')
BASE_URL = 'https://api.deepseek.com/v1/chat/completions'

def chat_with_deepseek(prompt):
    """使用DeepSeek API进行对话
    
    Args:
        prompt: 用户输入的提示词
        
    Returns:
        模型的回复内容
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    payload = {
        'model': 'deepseek-chat',
        'messages': [{
            'role': 'user',
            'content': prompt
        }],
        'temperature': 0.7,
        'max_tokens': 1000
    }
    response = requests.post(BASE_URL, headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']

if __name__ == '__main__':
    print('DeepSeek Chatbot')
    print('Type exit to quit')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        try:
            response = chat_with_deepseek(user_input)
            print(f'Bot: {response}')
        except Exception as e:
            print(f'Error: {e}')
