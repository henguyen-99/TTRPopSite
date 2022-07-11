alert("Welcome to the TTR Population Checker!")

function extendNav() {
    let nav = document.getElementById("navigation");

    if(nav.className === "nav-container") {
        nav.className += " responsive";
    }

    else {
        nav.className = "nav-container";
    }
}