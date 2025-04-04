import boto3

ACESS_KEY = 'Your AWS KEY'
SECRET_KEY = 'Your AWS KEY'
REGION_NAME = 'ap-northeast-2'

client = boto3.client(
    'comprehend',
    aws_access_key_id = ACESS_KEY,
    aws_secret_access_key = SECRET_KEY,
    region_name = REGION_NAME
)

text = '옛날로 돌아가보면 사실 74 월드컵 네덜란드는 지금의 시선으로 보면 되게 형편없습니다. 보다가 계속 꺼버리고 결국엔 대부분의 경기들을 풀 타임 시청을 못하긴 했는데 (아리고 사키의 밀란까진 어떻게 됐는데 그 이전은 풀 타임 시청이 안 되더라구요. 원래 다시 보기라는 거 자체를 안 좋아하긴 하는데 옛날 경기 다 보고나서 다시 보기는 정말 할 게 못 된다는 걸 느끼고 그 후로 지나간 경기들이나 옛날 경기들은 안 찾아봅니다.) 모두가 미친듯이 뛰어다니긴 하는데 되게 무질서하고 중구난방이었습니다. 근데 당시에 충격적이었던 건 그거죠. 축구란 스포츠는 긴 거리를 돌파하고 상대 수비수들을 박스 근처에서 현란하게 제끼면서 골키퍼를 넘어서는 그런 스포츠였는데 다른 의미로 접근한 거였으니까요.'

# response = client.detect_sentiment(
#     Text = text,
#     LanguageCode = 'ko'
# )

# response = client.detect_key_phrases(
#     Text = text,
#     LanguageCode='ko'
# )

response = client.detect_entities(
    Text = text,
    LanguageCode = 'ko'
)

# print('Sentiment : ', response['Sentiment'])
# print('Sentiment Score : ', response['SentimentScore'],'\n')

# print('추출된 핵심어 : ')
# for phrase in response['KeyPhrases']:
#     print('-',phrase['Text'])

print('엔티티 인식 결과')
for entity in response['Entities']:
    print(f'엔티티 : {entity['Text']}, 유형 : {entity['Type']}, 신뢰도 : {entity['Score']}')
