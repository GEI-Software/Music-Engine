// Funció per a canviar el color de fons quan es fa clic en un botó
function changeBackgroundColor() {
    document.body.style.backgroundColor = "lightblue";
}

// Funció per a mostrar un missatge d'alerta
function showAlert() {
    alert("Alert!");
}

// Funció per a fer alguna acció quan la pàgina es carrega completament
function onPageLoad() {
    console.log("Page loaded successfully.");
}

// Event listener per a detectar quan es fa clic en el botó
var button = document.getElementById("my-button");
button.addEventListener("click", changeBackgroundColor);

// Event listener per a detectar quan la pàgina es carrega completament
window.addEventListener("load", onPageLoad);
