# Data Challenge - Part 1 - Data API Ingestion

- Data Collection API:
Make the method that performs the data collection and that receives parameters via Http Post, in the params object.

Tip: Use the urllib.request library urlretrieve method https://docs.python.org/3/library/urllib.request.html
Or any other lib that is easier.

Tip 2: Create a Params class with the attributes.
- url: The url of the file to be downloaded must be informed
- bucket_name: gcs bucket name
- output_file_prefix: prefix for storing the data inside the gcs bucket


Create a function that can upload the data downloaded by the download function to the GCS

-----
## Criar virtual environment 
python -m venv [nomevenv]
[nomevenv]\Scripts\activate

## Iniciar Ambiente
uvicorn [nomedoaquivo]:[varialvelapp] --reload

