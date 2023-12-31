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
    return openai_key["api1"]


def create_openai(prompt):
    openai.api_key = get_api_key()
    response = openai.ChatCompletion.create(
        # text-davinci-003 是指它的模型
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.get("choices")[0].message['content']
    return message

def create_openai_mt(prompt):
    openai.api_key = get_api_key()
    response = openai.ChatCompletion.create(
        # text-davinci-003 是指它的模型
        model="gpt-3.5-turbo-1106",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.get("choices")[0].message['content']
    return message


create_openai("美国是最发达的国家吗")

if __name__ == '__main__':
    result = create_openai("美国是最发达的国家吗")
    print(result)