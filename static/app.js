const slideOverPanel = document.querySelector(".relative.z-50.lg\\:hidden");
const openButton = document.getElementById("openButton");
const closeButton = document.getElementById("closeButton");

openButton.addEventListener("click", function () {
  slideOverPanel.classList.remove("hidden");
});

closeButton.addEventListener("click", function () {
  slideOverPanel.classList.add("hidden");
});

const sideItemM = document.querySelectorAll(".sideItemM a");
const sideItemD = document.querySelectorAll(".sideItemD a");

sideItemM.forEach((aTag) => {
  aTag.addEventListener("click", function () {
    sideItemM.forEach((aTag) => {
      aTag.classList.remove("bg-gray-800", "text-white");
    });
    aTag.classList.add("bg-gray-800", "text-white");
  });
});

sideItemD.forEach((aTag) => {
  aTag.addEventListener("click", function () {
    sideItemD.forEach((aTag) => {
      aTag.classList.remove("bg-gray-800", "text-white");
    });
    aTag.classList.add("bg-gray-800", "text-white");
  });
});

const path = window.location.pathname;

if (path === "/") {
  sideItemM[0].classList.add("bg-gray-800", "text-white");
  sideItemD[0].classList.add("bg-gray-800", "text-white");
} else if (path === "/settings/") {
  sideItemM[4].classList.add("bg-gray-800", "text-white");
  sideItemD[4].classList.add("bg-gray-800", "text-white");
}
