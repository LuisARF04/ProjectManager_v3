"use strict"

function toggleDescription(id) {
    const el = document.getElementById(id);
    
    if (el.classList.contains("truncate-2-lines")) { 
        el.classList.remove("truncate-2-lines"); 

    } else {
        el.classList.add("truncate-2-lines"); 
    }
}