import os
import urllib
import uvicorn
from google.cloud import storage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ac-data-challenge-9d6dd621be3b.json'

storage_client = storage.Client()

dir(storage_client)
# BUCKET_NAME = 'insira_nome_bucket'
# bucket = storage_client.bucket(BUCKET_NAME)

# Bucket Detail
# vars(bucket)

# Accessing Bucket
# my_bucket = storage_client.get_bucket(BUCKET_NAME)

app = FastAPI()

class Params(BaseModel):
    url: str
    bucket_name: str
    output_file_prefix: str

# Upload Files
def put_file_to_gcs(output_file:str, bucket_name:str, content_file):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(output_file)
        blob.upload_from_string(content_file)
        return 'OK'
    except Exception as ex:
        print(f'Erro ao enviar arquivo para o GCS: {ex}')
        return 'ERROR'

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/download_combustivel")
async def download_combustivel(params: Params):
    try:
        with urllib.request.urlopen(params.url) as response:
            status_code = response.getcode()
            if status_code == 200:
                content = response.read()
                put_file_to_gcs(bucket_name=params.bucket_name,
                                output_file=params.output_file_prefix,
                                content_file=content)

                return {"Status": "OK"}
            else:
                raise HTTPException(status_code=status_code, detail=f"Erro ao baixar o arquivo: {status_code}")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {ex}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

