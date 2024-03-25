import json

from src.utils.llm import (retreive_answers)

def main(Response, body):
    try:
        our_query = body['message']
        if (len(our_query) > 0):
            answer = retreive_answers(our_query)
            body = json.dumps({'status': 'success', 'reply': answer})
            return Response(body, status=200, mimetype='application/json')
        
    except Exception as e:
        body = json.dumps({'status': 'failed', 'message': e})
        return Response(body, status=500, mimetype='application/json')
