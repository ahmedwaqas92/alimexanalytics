$(function() {
    $('div[name="daterangediv"]').daterangepicker({
        opens: 'left',
        autoUpdateInput: false
    }, function(start, end, label) {
        $('#daterange').val(start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
    });
});

function toggleDropDown(event) {
    var dropDownList = document.getElementById('dropDownList');
    if (dropDownList) {
        if (dropDownList.style.visibility === 'visible') {
            dropDownList.style.visibility = 'hidden';
            document.removeEventListener('click', handleClickOutside);
        } else {
            dropDownList.style.visibility = 'visible';
            document.addEventListener('click', handleClickOutside);
        }
    } else {
        console.error("Element with id 'dropDownList' not found.");
    }

    // Prevent event from bubbling up to document click handler
    event.stopPropagation();
}

function handleClickOutside(event) {
    var dropDownList = document.getElementById('dropDownList');
    if (dropDownList && dropDownList.style.visibility === 'visible') {
        // Check if the click is outside the dropdown
        if (!dropDownList.contains(event.target) && event.target.id !== 'dropDownList') {
            dropDownList.style.visibility = 'hidden';
            document.removeEventListener('click', handleClickOutside);
        }
    }
}

// Prevent event from bubbling up to document click handler
document.addEventListener('DOMContentLoaded', function() {
    var dropDownList = document.getElementById('dropDownList');
    if (dropDownList) {
        dropDownList.addEventListener('click', function(event) {
            event.stopPropagation();
        });
    }
});

function toggleCheckbox(checkboxId) {
    var checkbox = document.getElementById(checkboxId);
    if (checkbox) {
        checkbox.checked = !checkbox.checked;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const newChart = document.getElementById('barChart').getContext('2d');

    const weightChartData = { 
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', "Mango", "Butter", "Silicon", "Diamond", 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', "Mango", "Butter"],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3, 3, 4, 1, 2, 12, 19, 3, 5, 2, 3, 3, 4],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ensure the chart maintains the aspect ratio
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    }
                }
            }
        }
    };

    const thicknessChartData = {
        type: 'bar',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange', "Mango", "Butter", "Silicon", "Diamond", 'Red', 'Blue'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3, 3, 4, 1, 2, 12, 19],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ensure the chart maintains the aspect ratio
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    }
                }
            }
        }
    };

    let chart = new Chart(newChart, weightChartData);

    window.selected = function(element, chartDataId) {
        // Get all li elements
        var lis = document.querySelectorAll('.visualizationTop li');
        
        // Remove the is-active class from all li elements
        lis.forEach(function(li) {
            li.classList.remove('is-active');
        });
        
        // Add the is-active class to the clicked li element
        element.classList.add('is-active');
        
        // Update the chart with the selected data
        chart.destroy();
        const chartData = chartDataId === 'weightChartData' ? weightChartData : thicknessChartData;
        chart = new Chart(newChart, chartData);
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('scatterPlot').getContext('2d');

    const scatterPlotData = {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                data: [
                    { x: -10, y: 0 },
                    { x: -5, y: 5 },
                    { x: 0, y: 10 },
                    { x: 5, y: 5 },
                    { x: 10, y: 0 },
                    { x: 7, y: 3 },
                    { x: -3, y: -7 },
                    { x: 1, y: 8 },
                    { x: -6, y: -3 },
                    { x: 9, y: 7 },
                    { x: -2, y: 6 },
                    { x: 4, y: -4 },
                    { x: 8, y: 2 },
                    { x: 2, y: -6 },
                    { x: -7, y: 4 },
                    { x: 6, y: -1 },
                    { x: -8, y: -5 },
                    { x: 3, y: 9 },
                    { x: 5, y: -2 },
                    { x: -4, y: 1 }
                ],
                backgroundColor: 'rgba(75, 192, 192, 1)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            family: 'Outfit'
                        }
                    }
                }
            }
        }
    };

    new Chart(ctx, scatterPlotData);
});