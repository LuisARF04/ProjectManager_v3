document.addEventListener("DOMContentLoaded", function() {
    const lista = document.getElementById("lista-proyectos");
    const contador = document.getElementById("contador");

    if (lista) {
        const cantidad = lista.getElementsByTagName("li").length;
        contador.textContent = "Tienes " + cantidad + " proyecto(s) en tu lista.";
    }
});