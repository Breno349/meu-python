const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send("Servidor Node.js rodando!");
});

app.get('/json', (req, res) => {
  res.json({ status: 'ok', mensagem: 'JSON enviado!' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor iniciado em http://localhost:${PORT}`);
});
