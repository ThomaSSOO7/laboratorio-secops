import json


def lambda_handler(event, context):
    print(f"Evento recebido: {json.dumps(event)}")


    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"Processando ficheiros: {key} do bucket {bucket}")


    return {
        'statusCode': 200,
        'body': json.dumps('Processamento concluido!')
    }
