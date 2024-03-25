# llm-app

### Python version

python version = 3.10

### .env file contains
```
HOST="127.0.0.1"
PORT=4000
OPENAI_API_KEY=""
PINECONE_API_KEY=""
PINECONE_ENV=""
PINECONE_INDEX_NAME=""
```
# Development

1. create an environment on anaconda with python 3.10
  1. `conda create -p py_env python==3.10`
  2. `conda activate py_env/`
  3. `pip install -r requirements.txt`

2. To run the application, clone it on the local machine and run
  1. `python index.py`

3. To see all the installed pip libraries, run
  1. pip freeze > requirements.txt
