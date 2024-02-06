btn = document.querySelector("#custom");

// btn.addEventListener("click", function (e) {

// });
header = document.querySelector("#status");
color = document.querySelector(".security-item");
passwd = document.querySelector("#password").value;
if (passwd.length <= 5) {
  console.log("passwd");
} //else if (passwd.length == 5) color.style.background = "blue";
else {
  console.log("not");
}

logForm = document.querySelector(".logForm");
ref = document.querySelector(".ref");
logos = document.querySelector(".logos");
auth = document.querySelector(".auth");
logoContent = document.querySelector(".logoContent");
text = document.querySelector(".text");
create = document.querySelector("#create");
hide = document.querySelector("#pass");

ref.addEventListener("click", function (e) {
  e.preventDefault();
  logForm.style.display = "block";
  logForm.style.marginBottom = "3%";
  logForm.style.marginTop = "30%";
  logos.style.display = "none";
  auth.style.display = "none";
  text.style.display = "none";
  hide.style.display = "none";
  logoContent.style.marginTop = "5%";
});
create.addEventListener("click", function (e) {
  e.preventDefault();
  logForm.style.display = "none";
  logos.style.display = "block";
  auth.style.display = "block";
  text.style.display = "block";
});
