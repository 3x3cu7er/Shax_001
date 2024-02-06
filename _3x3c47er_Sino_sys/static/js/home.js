var counter = 0;

// menu = document.querySelector("#menu");
// menu.addEventListener("click", function (e) {
//   e.preventDefault();
//   submenu = document.querySelector(".element");
//   submenu.style.display = "block";
// });
settings = document.querySelector(".settings");
setting = document.querySelector("#settings");
setting.addEventListener("click", function (e) {
  e.preventDefault();
  settings.style.display = "block";
});

// submenu = document.querySelector(".element");
// submenu.addEventListener("mouseover",function(e){
//     submenu.style.display = "block";
// });

timer = document.querySelector("#timer");
time = document.querySelector("#timer span");

timer.addEventListener("mouseover", function (e) {
  counter = 0;
  time.innerHTML = setInterval(() => {
    counter += 1;
  }, 1000);

  time.style.color = "greenyellow";
  time.style.marginRight = "5px";
});

incomingMessage = document.querySelector(".incoming");
Nmsg = document.querySelector(".numOfMsg");

incomingMessage.addEventListener("mouseover", function (e) {
  Nmsg.innerHTML = parseInt(Math.random().toFixed(3) * 100);
});

Nmsg.addEventListener("click", function (e) {
  e.preventDefault();
  alert("msg is working");
});

// function incoming(){
//     inBody = document.createElement("div");
//     inBody.className = "from";
//     content = document.createElement("h5");
//     content.innerHTML = "Incoming message"
//     inBody.appendChild(content);
// }
// function outgoing(){
//     type = document.querySelector("#type").value;
//     inBody = document.createElement("div");
//     inBody.className = "to";
//     content = document.createElement("h5");
//     inBody.appendChild(content);
//     content.innerHTML = type;
// }

// send = document.querySelector("#send");

// send.addEventListener('click', function(e){
//     outgoing();
// })

sending = document.querySelector("#sending");
sending.addEventListener("click", function (e) {
  //sending
  info = document.querySelector("#type").value;
  sender = document.querySelector(".display");
  _to = document.createElement("div");
  _to.className = "to";
  _to.style.marginTop = ".4rem";
  _to.innerHTML = info;
  sender.appendChild(_to);

  // _from = document.createElement("div");
  // _from.className = "from";
  // _from.style.marginTop = "2rem";
  // _from.innerHTML = "Not working..";
  // sender.appendChild(_from);
});

//wallpaper settings

// change = document.querySelector(".change");

// change.addEventListener("click", function (e) {
//   backDisplay = document.querySelector(".chatdisplay");
//   wall = document.querySelector(".wallpaper").value;
//   backDisplay.style.background = `${wall}`;
// });

let m = document.querySelector(".year");
let d = document.querySelector(".month");
let dte = document.querySelector(".date");

function time() {
  dt = new Date();
  day = dt.getYear();
  mth = dt.getMonth();
  da = dt.getDate();

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

  dte.innerHTML = da;
  m.innerHTML = mth;
  d.innerHTML = day;
}
setInterval(time, 1000);
