
// NavBar

const toggleButton = document.querySelector(".menu");
const menu = document.querySelector(".navbar-menu");

toggleButton.addEventListener("click", function () {
    menu.classList.toggle("active");
});

// Footer

// Toggle links menu
const linksHeading = document.querySelector(".container1 .heading");
const linksMenu = document.querySelector(".container1 .links");

var flinks =function () {
    if (linksMenu.id != "active") {
        linksMenu.setAttribute("id", "active");
    } else {
        linksMenu.setAttribute("id", "");
    }
};

// Toggle others menu
const othersHeading = document.querySelector(".container2 .heading");
const othersMenu = document.querySelector(".container2 .others");

var fothers= function () {
    if (othersMenu.id != "active") {
        othersMenu.setAttribute("id", "active");
    } else {
        othersMenu.setAttribute("id", "");
    }
};

// Toggle contact menu
const contactHeading = document.querySelector(".container3 .heading");
const contactMenu = document.querySelector(".container3 .contact");

var fcontacts= function () {
    if (contactMenu.id != "active") {
        contactMenu.setAttribute("id", "active");
    } else {
        contactMenu.setAttribute("id", "");
    }
};




