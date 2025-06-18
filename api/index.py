from http.server import BaseHTTPRequestHandler, HTTPServer

def send_plain_text(response, text, status=200, extra_headers=None):
    response.status_code = status
    response.set_header('Content-Type', 'text/plain; charset=utf-8')
    if extra_headers:
        for k, v in extra_headers.items():
            response.set_header(k, v)
    response.send(text)

def send_json(response, data, status=200):
    import json
    response.status_code = status
    response.set_header('Content-Type', 'application/json; charset=utf-8')
    response.send(json.dumps(data))

def handler(request, response):
    method = request.method.upper()
    path = request.url
    query = request.args

    if method == 'GET':
        name = query.get('name', 'mundo')
        message = f"Olá, {name}! Você acessou: {path}\nMétodo: {method}"
        send_plain_text(response, message)

    elif method == 'POST':
        try:
            body = request.body.decode('utf-8')
        except Exception:
            body = "<não foi possível decodificar o corpo>"
        message = f"Recebi um POST com o corpo:\n{body}"
        send_plain_text(response, message)

    else:
        send_plain_text(response, "Método não permitido", status=405, extra_headers={"Allow": "GET, POST"})
