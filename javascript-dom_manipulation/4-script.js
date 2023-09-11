// references of the HTML
const add_item = document.querySelector("#add_item");

// Events
add_item.addEventListener("click", () => {
    const my_list = document.querySelector(".my_list");
    const newItem = document.createElement("li");
    newItem.textContent = "Item";
    my_list.appendChild(newItem);
});
