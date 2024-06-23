import express from 'express';


const d = new Date(); 
let day = d.getDay(); 
console.log(day); 

var app = express();
var port = 3000; 
app.set('view engine', 'ejs'); 

function adviceGenerator(){ 
    let advice; 
    if (day > 0 & day < 6) { 
         advice = "Its a weekday, its time to work hard"
    } else { 
         advice = "Its a weekend, its time to relax"
    }
    return advice 
}
app.get("/", (req, res) => {
    const advice = adviceGenerator(); 
    res.render("index.ejs", {advices: advice});
});

app.listen(port, () => {
console.log('Server is listening on port ' + port);
}); 