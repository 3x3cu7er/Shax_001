login = document.querySelector("#login");
content = document.querySelector("#message");

req_close = document.querySelector(".req-close");
login.addEventListener("click", function (e) {
  show = ["none", "block"];

  content.style.display = show[1];
});

req_close.addEventListener("click", function (e) {
  show = ["none", "block"];
  content.style.display = show[0];
});
