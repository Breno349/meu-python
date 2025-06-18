module.exports = (req, res) => {
  const { url, method } = req;

  if (method === 'GET') {
    if (url === '/' || url === '') {
      res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end("Olá, mundo!\nEssa é a rota principal.\nBem-vindo!");
    }

    else if (url === '/json') {
      res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
      res.end(JSON.stringify({ mensagem: "Isso é um JSON!", status: "ok" }, null, 2));
    }

    else if (url === '/html') {
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
      res.end(`
        <html>
          <body>
            <h1>Página HTML</h1>
            <p>Isso é um parágrafo</p>
            <pre>Texto com\nmúltiplas\nlinhas aqui</pre>
          </body>
        </html>
      `);
    }

    else {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end("Erro 404: rota não encontrada.");
    }
  }

  else {
    res.writeHead(405, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end("Método não permitido.");
  }
};
