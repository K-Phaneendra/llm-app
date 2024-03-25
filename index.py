from dotenv import load_dotenv, dotenv_values

from src.server import (app)

def startFlaskServer():
    host = dotenv_values(".env")['HOST']
    port = dotenv_values(".env")['PORT']
    if __name__ == '__main__':
        app.run(host=host, port=port, debug=True)

if load_dotenv():
    print('.env file loaded successfully')
    startFlaskServer()
else:
    print('Failed to load .env file')
