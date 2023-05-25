
from datetime import datetime, timedelta
import random
import json
import boto3

STREAM_NAME = "kinesis"


def get_data(day):
    start_date = datetime(2023, 4, 26) + timedelta(days=day)
    close_value = round(random.uniform(4400.000000, 4850.000000), 6)
    formatted_date = start_date.strftime('%Y-%m-%d')
    return {
        'date': formatted_date,
        'close': close_value
    }


def generate(stream_name, kinesis_client):
    for day in range(20):
        data = get_data(day)
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey"
        )


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis', region_name='us-east-1'))
