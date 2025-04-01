import boto3

polly_client = boto3.Session(
    aws_access_key_id = 'Your AWS KEY',
    aws_secret_access_key = 'Your AWS KEY',
    region_name = 'ap-northeast-2'
).client('polly')

text = "범인이랑 협상을 하려고 하는데 그럼 범인이 안된다고 하니까 나도 어떡해? 나도 안된다고 하겠지? 그러면 범인이 지 무시하는 줄 알고 협상 안 한다고 하겠지? 그럼 지가 협상 안 하니까 나는 협상 하고 싶겠냐? 협상 안 한다고 하겠지? 그럼 범인이 지가 열 받아 가지고, 어? 지도 열 받아 가지고 지 주제를 모르고 우리를 고소한다니까? 우리한테 고소한다고! 아 고소하라 그래, 고소하라 그래. 어? 야, 그런데 이런 일들이 왜 벌어지느냐, 야, 우리를 우습게 보니까 그런 거야. 우리가 범인들 잡아가지고 웃음을 주는 사람들이지, 우리가 우스운 사람들이야? 고소하라 그래! 고소하라 그래! 아 나도 내 할 말 다 했어. 아오 속이 시원하네 진짜. 아오 고소해 진짜, 아오 고소해 진짜. 아오 고소하다, 아오 고소하다~ 아오! 헤헤헤, 자기는 나 고소하지마!"

response = polly_client.synthesize_speech(
    Engine = 'standard',
    OutputFormat = 'mp3',
    Text = text,
    VoiceId = 'Seoyeon'
)

with open('speech.mp3','wb') as file:
    file.write(response['AudioStream'].read())

print('음성 변환 완료 : speech.mp3')