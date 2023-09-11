// references of the HTML
const character = document.querySelector("#character");
url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

// Fetch data from the URL
fetch(url)
    .then(function (Response) {
        if (!Response.ok) {
            throw new Error("Network Response was not ok");
        }

        // Parse the JSON Response
        return Response.json();
    })
    .then(function(data) {

        const characterNanme = data.name;
        character.textContent = characterNanme;
    })
    .catch(function(error) {
        console.error(error);
    });
