let h = document.querySelector(".hr");
let m = document.querySelector(".min");
let s = document.querySelector(".sec");
let d = document.querySelector(".dy");

function time() {
  dt = new Date();
  hr = dt.getHours() + 5;
  min = dt.getMinutes();
  sec = dt.getSeconds();
  day = dt.getDay();

  switch (day) {
    case 0:
      day = "Sunday";
      break;
    case 1:
      day = "Monday";
      break;
    case 2:
      day = "Tuesday";
      break;
    case 3:
      day = "Wednesday";
      break;
    case 4:
      day = "Thursday";
      break;
    case 5:
      day = "Friday";
      break;
    case 6:
      day = "Saturday";
      break;
  }

  if (hr < 10) {
    hr = "0" + hr;
  }
  if (min < 10) {
    min = "0" + min;
  }
  if (sec < 10) {
    sec = "0" + sec;
  }

  h.innerHTML = hr;
  m.innerHTML = min;
  s.innerHTML = sec;
  d.innerHTML = day;
}
setInterval(time, 1000);
