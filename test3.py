import requests
import json

API_ENDPOINT = 'Your End Point'

data = {'input_text' : 'Father and son are playing chess,'}

response = requests.post(API_ENDPOINT, json=data)

if response.status_code == 200:
    result = response.json()
    print("LLM 응답 : ", result['generated_text'])
else : 
    print("에러 : ", response.status_code, response.text)
