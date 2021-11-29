const express = require('express');
const mysql = require('mysql');
const sqlite3 = require('sqlite3').verbose();

const bodyParser = require('body-parser');

const PORT = process.env.PORT || 3050;

const app = express();

// Add headers before the routes are defined
app.use(function (req, res, next) {

  // Website you wish to allow to connect
  res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:8080');

  // Request methods you wish to allow
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

  // Request headers you wish to allow
  res.setHeader('Access-Control-Allow-Headers', 'Origin,X-Requested-With,content-type');

  // Set to true if you need the website to include cookies in the requests sent
  // to the API (e.g. in case you use sessions)
  res.setHeader('Access-Control-Allow-Credentials', true);

  // Pass to next layer of middleware
  next();
});

app.use(bodyParser.json());

let connection = new sqlite3.Database('../ransomware-sudoers/example.db',sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the in-memory SQlite database.');
});

// Route
app.get('/', (req, res) => {
  res.send('Welcome to my API!');
});

// all equipos
app.get('/equipos', (req, res) => {
  const sql = 'SELECT * FROM equipos';

  connection.all(sql, (error, results) => {
    if (error) throw error;
    if (results) {
      res.send(results);
    } else {
      res.send('Not result');
    }
  });
});


//a equip
app.get('/equipos/:id', (req, res) => {
  const { id } = req.params;
  const sql = `SELECT * FROM equipos WHERE id = '${id}'`;
  connection.each(sql, (error, result) => {
    if (error) throw error;

    if (result) {
      res.send(result);
    } else {
      res.send('Not result');
    }
  });
});

app.get('/comandos/:id', (req, res) => {
  const { id } = req.params;
  const sql = `SELECT * FROM comandos WHERE id_equipo = '${id}'`;
  connection.each(sql, (error, result) => {
    if (error) throw error;
    if (result) {
      res.send(result);
    } else {
      res.send('Not result');
    }
  });
});

app.patch("/comandos/update/", (req, res, next) => {
  connection.run(`UPDATE comandos set pendiente = ? WHERE id_equipo = ?`,
      [req.body.pendiente, req.body.id_equipo],
      function (err, result) {
          if (err) {
              res.status(400).json({ "error": res.message })
              return;
          }
          res.status(200).json({ updatedID: this.changes });
      });
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
