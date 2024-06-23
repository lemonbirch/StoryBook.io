import express from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 3000;

app.use(express.static("public"));


app.get("/", (req, res) => {
  res.render("index.ejs");
});

app.get("/storychoicebuilder", (req, res) => {
  res.render("storychoicebuilder.ejs");
});

app.get("/story", (req, res) => {
  res.render("story.ejs");
});
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
