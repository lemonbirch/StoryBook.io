//To see how the final website should work, run "node solution.js".
//Make sure you have installed all the dependencies with "npm i".
//The password is ILoveProgramming
import express from "express";
import morgan from "morgan";
import bodyParser from "body-parser";
import { dirname } from "path";
import { fileURLToPath } from "url"; 

const __dirname = dirname(fileURLToPath(import.meta.url));
const password = "password123"

const app = express();
const port = 3000;
app.use(bodyParser.urlencoded({ extended: true }));

var result = false; 


app.get("/", (req, res) => {
    res.sendFile(__dirname + "/public/index.html");
  });

function authenticatePassword (req, res, next) { 
    var userPassword = req.body["password"]; 
    console.log(userPassword);
    if (password === userPassword) {
        result = true;
    }
    next(); 
}
app.use(authenticatePassword);

app.post("/check", (req, res) => {
    if (result === true) {
        res.sendFile(__dirname + "/public/secret.html");
    } else {
        res.sendFile(__dirname + "/public/index.html");
    }

})
app.listen(port, () => {
    console.log(`Listening on port ${port}`);
  });
  