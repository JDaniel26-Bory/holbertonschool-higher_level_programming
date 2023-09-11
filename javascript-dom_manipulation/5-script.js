// references of the HTML
const update_header = document.querySelector("#update_header");


// Events 
update_header.addEventListener("click", () => {
    const header = document.querySelector("header");
    header.textContent = "New Header!!!";
});
