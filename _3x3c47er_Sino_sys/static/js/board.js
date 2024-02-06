// explore = document.querySelector("#explore");
message = document.querySelector("#message");
_man = document.querySelector("#man");

wall_close = document.querySelector(".wall-close");
man = document.querySelector(".man");
// exp = document.querySelector(".exp");
msg = document.querySelector(".msg");
settings = document.querySelector(".settings");
display = document.querySelector(".display");
navigations = document.querySelector(".navigations");
man_close = document.querySelector(".man-close");
// ex_close = document.querySelector(".ex-close");
ms_close = document.querySelector(".ms-close");
_default = document.querySelector("#default");
wallpaper = document.querySelector("#wallpaper");

wall_close.addEventListener("click", function (e) {
  settings.style.display = "none";
});

display.addEventListener("click", function (e) {
  navigations.style.display = "block";
});

// exp.addEventListener("click", function (e) {
//   show = ["none", "block"];

//   explore.style.display = show[1];
//   explore.style.className = "opacity";
// });

msg.addEventListener("click", function (e) {
  show = ["none", "block"];

  message.style.display = "block";
});

// ex_close.addEventListener("click", function (e) {
//   show = ["none", "block"];
//   explore.style.display = show[0];
// });

ms_close.addEventListener("click", function (e) {
  show = ["none", "block"];
  message.style.display = show[0];
});

man.addEventListener("click", function (e) {
  show = ["none", "block"];

  _man.style.display = show[1];
});

man_close.addEventListener("click", function (e) {
  show = ["none", "block"];
  _man.style.display = show[0];
});

wallpaper.onchange = (e) => {
  if (wallpaper.files[0])
    _default.src = URL.createObjectURL(wallpaper.files[0]);
};

_default.addEventListener("click", function (e) {
  e.preventDefault();
  settings.style.display = "block";
});
