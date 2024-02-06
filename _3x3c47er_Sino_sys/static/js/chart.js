const ctx = document.getElementById("dataRep");
const tracking = document.getElementById("tracking");
const chartContainer = document.getElementById("chartContainer");

new Chart(ctx, {
  type: "line",
  data: {
    labels: ["1st year", "2nd year", "3rd year", "4th year"],
    datasets: [
      {
        label: "Performance",
        data: [42, 69, 70, 15],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

new Chart(chartContainer, {
  type: "bar",
  data: {
    labels: ["1st year", "2nd year", "3rd year", "4th year"],
    datasets: [
      {
        label: "Progress",
        data: [12, 19, 3, 5],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});

new Chart(tracking, {
  type: "polarArea",
  data: {
    labels: ["Year 1", "Year 2", "Year 3", "Year 4"],
    datasets: [
      {
        label: "Tracks",
        data: [12, 19, 3, 5],
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
});
// let chart = new frappe.Chart("#tracking", {
//   // or DOM element
//   data: {
//     labels: [
//       "12am-3am",
//       "3am-6am",
//       "6am-9am",
//       "9am-12pm",
//       "12pm-3pm",
//       "3pm-6pm",
//       "6pm-9pm",
//       "9pm-12am",
//     ],

//     datasets: [
//       {
//         name: "Some Data",
//         chartType: "bar",
//         values: [25, 40, 30, 35, 8, 52, 17, -4],
//       },
//       {
//         name: "Another Set",
//         chartType: "bar",
//         values: [25, 50, -10, 15, 18, 32, 27, 14],
//       },
//       {
//         name: "Yet Another",
//         chartType: "line",
//         values: [15, 20, -3, -15, 58, 12, -17, 37],
//       },
//     ],

//     yMarkers: [{ label: "Marker", value: 70, options: { labelPos: "left" } }],
//     yRegions: [
//       {
//         label: "Region",
//         start: -10,
//         end: 50,
//         options: { labelPos: "right" },
//       },
//     ],
//   },

//   title: "My Awesome Chart",
//   type: "axis-mixed", // or 'bar', 'line', 'pie', 'percentage'
//   height: 300,
//   colors: ["purple", "#ffa3ef", "light-blue"],

//   tooltipOptions: {
//     formatTooltipX: (d) => (d + "").toUpperCase(),
//     formatTooltipY: (d) => d + " pts",
//   },
// });
