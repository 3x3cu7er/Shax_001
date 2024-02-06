setting = document.querySelector(".settings");
close = document.querySelector(".close");
subSet = document.querySelector("#settings");

changer = 0;
setting.addEventListener("click", function (e) {
  show = ["none", "block"];
  //   changer += 1;
  //   if (changer >= show.length) {
  //     changer = 0;
  //   }
  subSet.style.display = show[1];
});

close.addEventListener("click", function (e) {
  show = ["none", "block"];
  subSet.style.display = show[0];
});
