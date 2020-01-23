// Load the data
d3.json("/geoData").then(response => {
    console.log("start");
    
    var crashData = [];
    crashData = response;
    console.log(crashData);
  
// Make new arrays for x and y axes
    
    var date = crashData.map(d => d.Year);
    console.log(date);
  
    var Fatalities = crashData.map(d => d.Fatalities); 
    console.log(Fatalities);

// Make new array for x axis
     var firstYear = 1908;
     var finalYear = 2010;
     var numYearsToUse = finalYear-firstYear;
 
     crashPerYear = [];
 
      for (i = 0; i < numYearsToUse; i++){
        crashPerYear[i] = 0;
      }
      console.log(`crashPerYear.length = ${crashPerYear.length}`);

// APEX code       
// var options = {
//     series: [
//     {
//       name: "Crashes per year",
//       data: crashPerYear
//     // {
//     //   name: "Low - 2013",
//     //   data: [12, 11, 14, 18, 17, 13, 13]
//     // }
//     }],
//     chart: {
//     height: 450,
//     type: 'line',
//     dropShadow: {
//       enabled: true,
//       color: '77B6EA',
//       top: 18,
//       left: 7,
//       blur: 10,
//       opacity: 0.2
//     },
//     toolbar: {
//       show: false
//     }
//   },
//   colors: ['#77B6EA'],
//   dataLabels: {
//     enabled: true,
//   },
//   stroke: {
//     curve: 'smooth'
//   },
//   title: {
//     text: 'Plane Crashes Over the Last Century',
//     align: 'left',
//     color: '#999'
//   },
//   grid: {
//     borderColor: '#e7e7e7',
//     row: {
//       colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
//       opacity: 0.
//     },
//   },
//   markers: {
//     size: 1
//   },
//   xaxis: {
//     categories: crashPerYear,
//     title: {
//       text: 'Year',
//       color: '#e7e7e7'
//     }
//   },
//   yaxis: {
//     title: {
//       text: 'Fatalities',
//       color: "#77B6EA",
//     },
//     min: 0,
//     max: 105
//   },
//   legend: {
//     position: 'top',
//     horizontalAlign: 'right',
//     floating: true,
//     offsetY: -25,
//     offsetX: -5
//   }
//   };

//   var chart2 = new ApexCharts(document.querySelector("#chart2"), options);
//   chart2.render();

 });