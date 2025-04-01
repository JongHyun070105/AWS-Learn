import boto3

ACESS_KEY = 'Your AWS KEY'
SECRET_KEY = 'Your AWS KEY'
REGION_NAME = 'ap-northeast-2'

comprehend = boto3.client(
    'comprehend',
    aws_access_key_id = ACESS_KEY,
    aws_secret_access_key = SECRET_KEY,
    region_name = REGION_NAME
)

text = 'My name is Admin. My phone number 010-1234-5678 and my email example@gmail.com. I live in Seoul.'

response = comprehend.detect_pii_entities(
    Text = text,
    LanguageCode = 'en'
)

print('Detected PII Entities : ')
for entity in response['Entities']:
    print(f' - Type : {entity['Type']}, Score : {entity['Score']:.2f}, BeginOffset : {entity['BeginOffset']}, EndOffset : {entity['EndOffset']}')
    print(f" --> Text : '{text[entity['BeginOffset']:entity['EndOffset']]}")