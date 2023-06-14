$(document).ready(function () {
  // Remove gridlines 
  Chart.defaults.scale.gridLines.display = false;

  //Load CSV
  d3.csv("HAM10000_metadata_v2.csv", function (d) {
    return {
      age: +d.age,
      sex: d.sex,
      localization: d.localization,
      dxType: d.dx_type,
      cellType: d.cell_type

    }
  }).then(function (data) {
    let ctx = $('#cellTypeChart')[0].getContext('2d')

    let groupedData = sort(_.chain(data).countBy('cellType').value())

    let chart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: _.pluck(groupedData, 'label'),
        datasets: [{
          data: _.pluck(groupedData, 'value'),
          backgroundColor: '#3c65bb',
          borderColor: 'black'
        }]

      },
      options: {
        sort: true,
        legend: {
          display: false
        },
        title: {
          display: false
        },
        scales: {
          xAxes: [{
            ticks: {
              callback: function (value) {
                return decamelize(value)
              }
            }
          }],

          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    });
  });

  // //Load confusion matrix
  // d3.csv('../models/alexnet/test_result.csv').then(function (data) {
  //   // let confusion_matrix = calculate_confusion_matrix(data)
  //   let confusion_matrix = [[10, 189],[98,129]]
  //   labels = ['Actinic keratoses', 'Basal call carcinoma', 'Benign keratosis-like lesions', 'Dermatofibroma', 'Melanocytic nevi', 'Melanoma', 'Vascular lesions']
  //   Matrix({
  //     container: '#alexNetCM',
  //     data: confusion_matrix,
  //     labels: labels,
  //     start_color : '#ffffff',
  //     end_color : '#e67e22'
  //   })
  // })

});

var layout1 = {title: 'AlexNet - Matriz de Confusión'}

var data1 = [
  {
    z: [[50.77,13.85,10.77,4.62,12.31,7.69,0],
        [10.68,70.87,5.83,0.97,7.77,3.88,0],
        [3.64,3.18,61.82,0.45,23.64,7.27,0],
        [0,8.70,13.04,30.43,39.13,8.70,0],
        [0.82,1.12,1.49,0.22,93.14,2.98,0.22],
        [3.14,1.79,6.28,1.79,31.39,55.16,0.45],
        [0,7.14,0,0,14.29,0,78.57]

      ],
    x: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    y: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    type: 'heatmap',
    hoverongaps: false,
    colorscale: 'Viridis'
  }
];

var layout2 = {title: 'AlexNet con pesos - Matriz de Confusión'}

var data2 = [
  {
    z: [[34.46,15.38,12.31,3.08,7.69,23.08,0],
        [6.80,75.73,3.88,0.97,9.71,2.91,0],
        [3.18,3.64,55.45,0.45,20.45,16.82,0],
        [0,8.70,17.39,30.43,30.43,13.04,0],
        [0.37,1.27,1.42,0.15,89.19,7.46,0.15],
        [1.35,2.24,5.38,0.90,19.28,70.40,0.45],
        [0,7.14,0,0,14.29,0,78.57]
      ],
    x: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    y: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    type: 'heatmap',
    hoverongaps: false,
    colorscale: 'Viridis'
  }
];


var layout3 = {title: 'ResNet - Matriz de Confusión'}

var data3 = [
  {
    z: [[24.62,13.85,32.31,0,29.23,0,0],
        [1.94,44.66,11.65,0,36.89,2.91,1.94],
        [0.91,1.82,48.18,0,44.09,5,0],
        [0,0,13.04,0,78.26,8.70,0],
        [0,0.52,2.91,0,95.15,1.42,0],
        [1.35,1.36,18.39,0,49.33,29.15,0.45],
        [0,7.14,0,0,71.43,0,21.43]
      ],
    x: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    y: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    type: 'heatmap',
    hoverongaps: false,
    colorscale: 'Viridis'
  }
];

var layout4 = {title: 'ResNet con pesos - Matriz de Confusión'}

var data4 = [
  {
    z: [[27.69,15.38,13.85,0,18.46,24.62,0],
        [0.97,35.92,9.71,0,32.04,20.39,0.97],
        [0.91,1.82,40.45,0,36.36,20.45,0],
        [0,4.35,13.04,0,69.57,13.04,0],
        [0.15,0.37,1.34,0,88.29,9.84,0],
        [0.90,0,6.73,0,31.39,60.99,0],
        [0,8.14,3.57,0,64.29,3.57,21.43]
      ],
    x: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    y: ['Queratosis actínica','Carcinoma de células basales','Queratosis seborreica','Dermatofibroma','Lunar','Melanoma','Lesiones vasculares'],
    type: 'heatmap',
    hoverongaps: false,
    colorscale: 'Viridis'
  }
];

Plotly.newPlot('cf1', data1, layout1);
Plotly.newPlot('cf2', data2, layout2);
Plotly.newPlot('cf3', data3, layout3);
Plotly.newPlot('cf4', data4, layout4);

function calculate_confusion_matrix(data) {
  let confusion_matrix = zeros(7, 7, 0)
  _.each(data, (row) => {
    confusion_matrix[row.Actual][row.Predicted] += 1
  })

  return confusion_matrix
}

function zeros(w, h) {
  return Array.from(new Array(h), _ => Array(w).fill(0))
}

function decamelize(str) {
  var words = str.match(/[A-Za-z][a-z]*/g);
  return words.map(capitalize).join(' ');
}

function capitalize(word) {
  return word.charAt(0).toUpperCase() + word.substring(1)
}

function sort(obj) {
  let arr = []

  _.mapObject(obj, function (val, key) {
    arr.push({
      label: key,
      value: val
    })
  });

  return _.sortBy(arr, 'value')
}