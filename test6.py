import boto3
import time
import requests

transcribe = boto3.client(
    'transcribe',
    aws_access_key_id = 'Your AWS KEY',
    aws_secret_access_key = 'Your AWS KEY',
    region_name = 'ap-northeast-2'
)

job_name = "Your Job Name"
job_uri = f'S3 Bucket Video Path'

transcribe.start_transcription_job(
    TranscriptionJobName = job_name,
    Media = {'MediaFileUri' : job_uri},
    MediaFormat = 'm4a',
    LanguageCode = 'ko-KR'
)

while True :
    status = transcribe.get_transcription_job(TranscriptionJobName = job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED','FAILED']:
        break
    print('작업 진행 중...')
    time.sleep(5)

if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
    transcript_file_uri = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
    print(f'트랜스크립트 파일 위치 : {transcript_file_uri}')

    response = requests.get(transcript_file_uri)
    with open('transcript.json','wb') as file:
        file.write(response.content)
    print('트랜스크립트 파일 다운로드 완료')