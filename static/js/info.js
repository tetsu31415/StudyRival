var array_time = ['0.3' , '1.0', '1.2', '2.3', '0.3', '0.0', '1.5'];
var array_day = ['1' ,'2', '3', '4', '5', '6', '7'];

var ctx = document.getElementById('mychart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: array_day,
        datasets: [{
            label: "Studytime/day",
            backgroundColor: 'rgb(188, 255, 255)',
            borderColor: 'rgb(168, 255, 240)',
            data: array_time,
        }]
    },
    options: {}
});
