import boto3

dynamodb = boto3.resource('Your SQL',region_name='ap-northeast-2',aws_access_key_id='Your AWS KEY',aws_secret_access_key='Your AWS KEY')

table = dynamodb.Table('Your Table')
data = {'id' : 00000 , 'name' : 'Your Name'}
table.put_item(Item = data)