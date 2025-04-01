import boto3
import time

aws_access_key_id = 'Your AWS KEY'
aws_secret_access_key = 'Your AWS KEY'
region_name = 'ap-northeast-2'

bucket_name = 'Your Bucket Name'
video_file_name = 'File Name'

rekognition = boto3.client(
    'rekognition',
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key,
    region_name = region_name
)

with open('Your Image', 'rb') as image_file:
    image_bytes = image_file.read()

response = rekognition.detect_faces(
    Image={'Bytes': image_bytes},
    Attributes=['ALL']
)

for face_detail in response['FaceDetails']:
    print(f'성별 : {face_detail['Gender']['Value']}, \n'
          f'나이대 : {face_detail['AgeRange']['Low']} - {face_detail['AgeRange']['High']},\n'
          f'웃음 여부 : {face_detail['Smile']['Value']},\n'
          f'감정 : {face_detail['Emotions'][0]['Type']} \n')
    
with open('Your Image','rb') as image_file : 
    image_bytes = image_file.read()

response = rekognition.detect_labels(
    Image = {'Bytes' : image_bytes},
    MaxLabels = 10,
    MinConfidence = 80
)

for label in response['Labels'] : 
    print(f'탐지된 객체 : {label['Name']} (신뢰도 : {label['Confidence']:.2f}%)')

response = rekognition.start_label_detection(
    Video = {
        'S3Object' : {
            'Bucket' : bucket_name,
            'Name' : video_file_name
        }
    },
    MinConfidence = 75
)

job_id = response['JobId']
print(f'작업 ID : {job_id}')

while True : 
    response = rekognition.get_label_detection(JobId = job_id)
    status = response['JobStatus']

    if status == 'SUCCEEDED':
        print('영상 분석 완료')
        break
    elif status == 'FAILED':
        print('영상 분석 실패')
        break
    else : 
        print('영상 분석 진행 중...')
        time.sleep(5)

response = rekognition.get_label_detection(JobId = job_id)

for label_detection in response['Labels']:
    timestamp = label_detection['Timestamp']
    label = label_detection['Label']
    print(f'{timestamp / 1000:.2f}초 : {label['Name']} (정확도 : {label['Confidence']:.2f}%)')