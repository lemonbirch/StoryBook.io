import express from 'express';
import bodyParser from 'body-parser';
import axios from 'axios';
import * as storyModule from "./prompt.js"
import dotenv from "dotenv";
import { GoogleGenerativeAI } from "@google/generative-ai";

const app = express();
const port = 3000;

app.use(express.static("views"));
app.use(express.static("public"));

dotenv.config(); 
const GEMINI_KEY = process.env.API_KEY;

const genAI = new GoogleGenerativeAI(GEMINI_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash"});



app.get("/", (req, res) => {
  res.render("index.ejs");
});


app.get("/storychoicebuilder", (req, res) => {
  console.log("storybuilder test")
  res.render("storychoicebuilder.ejs");
});

app.get("/story", (req, res) => {
  console.log("ttesuhgreufh")
  const characterName = req.query.character_name;
  const storyTheme = req.query.story_theme; 
  console.log("testing type of " + typeof(characterName))
  const prompt = storyModule.checkParams(characterName, storyTheme)
  const text = generateContent(prompt).then(content => {
    console.log("Generated Content:", content);
    res.render("story.ejs", {
      story: content
    });
  }); 
  
});

async function generateContent(prompt) {
  try {
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = await response.text();
    return text;
  } catch (error) {
    console.error("Error generating content:", error);
  }
}




app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});



