import json
import openai
import random
def get_api_key():
    '''
    {"api": "你的 api keys"}
    '''
    openai_key_file = './openai_key.json'
    with open(openai_key_file, 'r', encoding='utf-8') as f:
        openai_key = json.loads(f.read())
    api_key_list = ['api1', 'api2', 'api3']
    api_value = random.sample(api_key_list, 1)
    print("api",openai_key[api_value[0]])
    return openai_key[api_value[0]]


def create_openai(prompt):
    openai.api_key = get_api_key()
    response = openai.ChatCompletion.create(
        # text-davinci-003 是指它的模型
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.get("choices")[0].message["content"]
    return message
