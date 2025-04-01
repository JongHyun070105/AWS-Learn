import boto3

dynamodb = boto3.resource('Your SQL',region_name='ap-northeast-2',aws_access_key_id='Your AWS KEY',aws_secret_access_key='Your AWS KEY')

table = dynamodb.Table('Your Table')

# 전체 데이터 스캔
response = table.scan()

# 아이템 출력
items = response['Items']
for item in items : 
    print(item)