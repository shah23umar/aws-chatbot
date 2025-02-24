import sys
print(sys.path)
sys.path.append('/usr/local/lib/python3.7/site-packages')
print(sys.path)

import boto3
import json

session = boto3.Session(region_name="us-east-1")
bedrock_agent_runtime = session.client(service_name='bedrock-agent-runtime', region_name='us-east-1')

def call_bedrock_service(question):

    user_question = question
    knowledge_base_id = '9WTHCKM0GF'
    model_arn = 'arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-5-sonnet-20240620-v1:0'
 
    try:
        response = bedrock_agent_runtime.retrieve_and_generate(
            input={
                'text': user_question
            },
            retrieveAndGenerateConfiguration={
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': {
                    'knowledgeBaseId': knowledge_base_id,
                    'modelArn': model_arn
                }
            }
        )
        generated_text = response['output']['text']
        return generated_text
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def main():
    while True:
        # get question from the user
        q = input("input your questions: ")
        resp = call_bedrock_service(q)
        print(resp)
        print()


if __name__ == '__main__':
    main()
