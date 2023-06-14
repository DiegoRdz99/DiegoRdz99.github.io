$(document).ready(function () {
  // Remove gridlines 
  Chart.defaults.scale.gridLines.display = false;

  //Load CSV
  // d3.csv("HAM10000_metadata_cleaned.csv", function (d) {
  d3.csv("HAM10000_metadata_v2.csv", function (d) {
    return {
      age: +d.age,
      sex: d.sex,
      localization: d.localization,
      dxType: d.dx_type,
      cellType: d.cell_type

    }
  }).then(function (data) {
    generateAgeChart(data);
    barChartRender(data, 'genderChart', 'sex', 'bar', 'genderCellType');
    barChartRender(data, 'localizationChart', 'localization', 'bar', 'localizationCellType');
    barChartRender(data, 'dxTypeChart', 'dxType', 'bar', 'dxTypeCellType')
    // barChartRender(data, 'skinLesionTypeChart', 'cellType', 'bar', '')
  });

  let generateAgeChart = function (data) {
    let ctx = $('#ageChart')[0].getContext('2d')

    let histogram = function (data) {
      const x = d3.scaleLinear().domain([0, 100])

      return d3.histogram().value(function (d) {
        return d.age
      }).thresholds(10).domain([0, 100])(data)
    }

    let bins = histogram(data)

    let ageChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: _.range(10, 101, 10),
        datasets: [{
          data: _.map(bins, function (d) {
            return d.length
          }),
          backgroundColor: '#3c65bb',
          borderColor: 'black'
        }]

      },
      options: {
        legend: {
          display: false
        },
        title: {
          display: false
        }
      }
    });

    //Events
    $('#ageCellType').on('change', function (e) {
      let cellType = $(this).val();

      let bins = histogram(cellType ? _.where(data, {
        cellType: cellType
      }) : data)

      ageChart.data.datasets[0].data = _.map(bins, function (d) {
          return d.length
        }),
        ageChart.update()

    })
  };

});

function barChartRender(data, canvas, variable, chartType, dropdown) {
  let ctx = $('#' + canvas)[0].getContext('2d');
  let scales = chartType === 'bar' ? {
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
  } : {
    yAxes: [{
      ticks: {
        callback: function (value) {
          return decamelize(value)
        }
      }
    }],

    xAxes: [{
      ticks: {
        beginAtZero: true
      }
    }]
  }
  
  let groupedData = sort(_.chain(data).countBy(variable).value())

  let chart = new Chart(ctx, {
    type: chartType,
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
      scales: scales
    }
  });

  //Events
  $('#' + dropdown).on('change', function (e) {
    let cellType = $(this).val();

    if (cellType) {
      let groupedData =  sort(_.chain(data).where({
        cellType: cellType
      }).countBy(variable).value())

      chart.data.labels = _.pluck(groupedData, 'label');
      chart.data.datasets[0].data = _.pluck(groupedData, 'value')
      chart.update()

    } else {
      let groupedData =  sort(_.chain(data).countBy(variable).value())

      chart.data.labels = _.pluck(groupedData, 'label');
      chart.data.datasets[0].data = _.pluck(groupedData, 'value')
      chart.update()

    }


    
  })
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

  _.mapObject(obj, function(val, key) {
    arr.push({
      label: key,
      value: val
    })
  });

  return _.sortBy(arr, 'value')
}