from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Params(BaseModel):
    url: str
    bucket_name: str
    output_file_prefix: str

def put_file_to_gcs(output_file:str, bucket_name:str, content_file):
    try:
        """
        Crie uma função que seja possível realizar o upload dos dados
        baixados pela função download_combustivel para o GCS
        
        Dica: Utilize a biblioteca do SDK da Google Cloud,
        https://cloud.google.com/storage/docs/reference/libraries
        upload_from_string
        """
        return 'OK'
    except Exception as ex:
        print(ex)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/download_combustivel")
async def download_combustivel(params: Params):
    try:
        """
        Faça aqui o metodo que realize a coleta de dados.
        Que receba parametros via Http Post, no objeto params.

        Dica: Utilize a biblioteca urllib.request metodo urlretrieve
        https://docs.python.org/3/library/urllib.request.html
        Ou qualquer outra lib que tenha mais facilidade.
        
        Dica 2: Crie uma classe Params com os atributos. 
        - url: Deverá ser informada url do arquivo a ser baixado
        - bucket_name: nome do bucket gcs
        - output_file_prefix: prefixo de armazenamento do dados dentro do bucket gcs
        """
        
        put_file_to_gcs(bucket_name=params.bucket_name, 
                        output_file=params.output_file_prefix, 
                        content_file=None)
        
        return {"Status": "OK"}
    except Exception as ex:
        raise HTTPException(status_code=ex.code, detail=f"{ex}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
