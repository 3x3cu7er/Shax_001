register = document.querySelector("#register");

sign = document.querySelector("#signIn");
link1 = document.querySelector("#link1");
link2 = document.querySelector("#link2");
// sign.addEventListener("click", function (e) {
//   signUp.style.display = "block";
//   signUp.style.marginTop = "-25%";
//   register.style.display = "none";
// });
// signUp.addEventListener("click", function (e) {
//   signIn.style.display = "none";
//   register.style.display = "block";
// });

link1.addEventListener("click", function (e) {
  sign.style.display = "block";
  sign.style.marginTop = "25%";
  register.style.display = "none";
});
link2.addEventListener("click", function (e) {
  signIn.style.display = "none";
  register.style.display = "block";
});
