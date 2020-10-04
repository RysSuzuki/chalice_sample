import boto3

def get_parameters(param_key):
    ssm = boto3.client('ssm')
    response = ssm.get_parameters(
        Names=[
            param_key,
        ],
        WithDecryption=True
    )
    return response['Parameters'][0]['Value']