"use strict"

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle-btn").forEach(function (btn) {
        btn.addEventListener("click", function () {
            const icon = btn.querySelector("i");
            if (btn.getAttribute("aria-expanded") === "true") {
                icon.classList.remove("bi-chevron-down");
                icon.classList.add("bi-chevron-up");
                btn.innerHTML = '<i class="bi bi-chevron-up"></i> Ocultar tareas';
            } else {
                icon.classList.remove("bi-chevron-up");
                icon.classList.add("bi-chevron-down");
                btn.innerHTML = '<i class="bi bi-chevron-down"></i> Ver tareas';
            }
        });
    });
});
