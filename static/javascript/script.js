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

    // Assuming graphingData is an array of objects with 'workOrder' and 'weight' keys
    const labels = graphingData.map(item => item.workOrder);
    const weightdata = graphingData.map(item => parseFloat(item.weight));
    const thicknessdata = graphingData.map(item => parseFloat(item.thickness));

    function getChartPadding() {
        // Check the window width and set padding accordingly
        return window.innerWidth > 1350 ? { top: 50, bottom: 50, left: 50, right: 50 } : { top: 0, bottom: 0, left: 0, right: 0 };
    }

    const weightChartData = {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Work Orders by Weight',
                data: weightdata,
                backgroundColor: 'rgba(199, 200, 245, 1)',
                // backgroundColor: 'rgba(75, 192, 192, 0.2)',
                // borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ensure the chart maintains the aspect ratio
            layout: {
                padding: {
                    top: 50,    // Space above the chart
                    bottom: 50, // Space below the chart
                    left: 50,   // Space to the left of the chart
                    right: 50   // Space to the right of the chart
                }
            },
            scales: {
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
                },
                tooltip: {
                    bodyFont: {
                        family: 'Outfit'
                    },
                    titleFont: {
                        family: 'Outfit'
                    }
                }
            }
        }
    };

    const thicknessChartData = {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Work Orders by Thickness',
                data: thicknessdata,
                backgroundColor: 'rgba(220, 252, 231, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Ensure the chart maintains the aspect ratio
            layout: {
                padding: {
                    top: 50,    // Space above the chart
                    bottom: 50, // Space below the chart
                    left: 50,   // Space to the left of the chart
                    right: 50   // Space to the right of the chart
                }
            },
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

    // Update padding on window resize
    window.addEventListener('resize', function() {
        chart.options.layout.padding = getChartPadding();
        chart.update();
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const dimensions = document.getElementById('scatterPlot').getContext('2d');

    // Map the graphingData to include workOrder, x (length), and y (width)
    const scatterDataPoints = graphingData.map(item => ({
        x: parseFloat(item.length),
        y: parseFloat(item.width),
        workOrder: item.workOrder
    }));

    function getChartPadding() {
        // Check the window width and set padding accordingly
        return window.innerWidth > 1350 ? { top: 50, bottom: 50, left: 50, right: 50 } : { top: 0, bottom: 0, left: 0, right: 0 };
    }

    const scatterPlotData = {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Width (mm) x Length (mm)',
                data: scatterDataPoints,
                backgroundColor: 'rgba(199, 200, 245, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: getChartPadding()
            },
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Width (mm)',
                        font: {
                            family: 'Outfit',
                            size: 16,
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'Outfit'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Length (mm)',
                        font: {
                            family: 'Outfit',
                            size: 16,
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
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const dataPoint = tooltipItem.raw;
                            return `Work Order: ${dataPoint.workOrder}\nWidth: ${dataPoint.y} mm\nLength: ${dataPoint.x} mm`;
                        }
                    },
                    bodyFont: {
                        family: 'Outfit'
                    },
                    titleFont: {
                        family: 'Outfit'
                    }
                }
            }
        }
    };

    // Create the chart
    let chart = new Chart(dimensions, scatterPlotData);

    // Update padding on window resize
    window.addEventListener('resize', function() {
        chart.options.layout.padding = getChartPadding();
        chart.update();
    });
});