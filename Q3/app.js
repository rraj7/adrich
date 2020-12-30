//const http = require("http");
const express = require("express")
const path = require("path")

const app = express();





function renderChart(data, labels) {
    var ctx = document.getElementById("myChart").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'This week',
                data: data,
            }]
        },
    });
    return myChart;
}

$("#renderBtn").click(
    function() {
        data = [20000, 14000, 12000, 15000, 18000, 19000, 22000];
        labels = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"];
        renderChart(data, labels);
    }
);

//app.use('/', require('./route/index'));
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + "/route/index.html"))
})


const PORT = process.env.PORT || 5000;
app.listen(PORT, console.log('Server started on port 5000'));