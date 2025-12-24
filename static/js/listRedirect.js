"use strict"

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".redirect-item").forEach(function (item) {
        item.addEventListener("click", function () {
            const href = item.dataset.href;
            if (href) {
                window.location.href = href;
            }
        });
    });
});
