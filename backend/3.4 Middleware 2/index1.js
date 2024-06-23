import express from "express";
import { dirname } from "path";
import { fileURLToPath } from "url";
import bodyParser from "body-parser";

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const port = 3000;
app.use(morgan("combined"));

// Middleware to parse URL-encoded data
app.use(bodyParser.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/public/index.html");
});

app.post("/submit", (req, res) => {
  console.log(req.body);  // Should log the form data
  res.send('Form submitted!');
});

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
});
