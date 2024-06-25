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

function makeChoice(choice) {
    fetch("/continue_story", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ choice: choice }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("story").innerText = data.new_story;
      })
      .catch((error) => console.error("Error:", error));
  }

  function resetStory() {
    fetch("/reset_story", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("story").innerText = data.new_story;
      })
      .catch((error) => console.error("Error:", error));
  }






app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
