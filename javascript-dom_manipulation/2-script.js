// references of the HTML
const red = document.querySelector('style')
const red_header = document.querySelector('#red_header');


// Events 
red_header.addEventListener('click', () => {
    red_header.classList.add("red");
})
