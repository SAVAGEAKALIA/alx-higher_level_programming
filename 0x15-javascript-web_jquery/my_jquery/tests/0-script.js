document.addEventListener("DOMContentLoaded", function () {
    const myHeaderelement = document.querySelector("header")
    if (myHeaderelement) {
        myHeaderelement.style.color = "#FF0000";
    } else {
        console.log("Header element not found.");
    }
});