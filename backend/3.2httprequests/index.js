import express from "express";

const app = express();
const port = 3000; 

app.get("/", (req, res) => {
    res.send("<h1>hello word</h1>")
}); 

app.get("/contact", (req, res) => {
    res.send("<h1>Contact Me</h1>")
}); 

app.get("/about", (req, res) => {
    res.send("<h1>About Me</h1>")
}); 
app.put("/user/sammy", (req, res) => {
    res.sendStatus(200);
});
app.patch("/user/sammy", (req, res) => {
    res.sendStatus(200);
});
app.delete("/user/sammy", (req, res) => {
    res.sendStatus(200);
});

app.listen(port, () =>{
    console.log(`Server started on port ${port}`);
});