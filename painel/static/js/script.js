//Menu Mobile

const menuMobile = document.querySelector(".menu-mobile");
const body = document.querySelector("body");
const menu = document.querySelector(".menu");

menuMobile.addEventListener("click", () => {
  menuMobile.classList.contains("bi-list")
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x", "bi-list");

  body.classList.toggle("menu-nav-active");
});

menu.addEventListener("click", () => {
  menu.classList.contains("bi-arrow-left-circle-fill")
    ? menu.classList.replace(
        "bi-arrow-left-circle-fill",
        "bi-arrow-right-circle-fill"
      )
    : menu.classList.replace(
        "bi-arrow-right-circle-fill",
        "bi-arrow-left-circle-fill"
      );
});

// Botão loading

const btn_Loading = document.querySelector(".btnLoading");
const loading = document.querySelector("#loading");

document.addEventListener("DOMContentLoaded", function (event) {
  loading.style.display = "none";
});
