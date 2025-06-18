print('$$'*100)

def handler(request, response):
    name = request.args.get("name", "mundo")
    response.status_code = 200
    response.headers["Content-Type"] = "text/plain"
    response.send(f"Olá, {name}! 👋")
