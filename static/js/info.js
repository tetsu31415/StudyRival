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
