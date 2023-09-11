// references of the HTML
url = "https://swapi-api.hbtn.io/api/films/?format=json";
const list_movies = document.querySelector("#list_movies");

// Fetch data from the URL
fetch(url)
    .then(function (respose) {
        if (!respose.ok) {
            throw new Error("Network Response was not ok");
        }
        // Parse the JSON Response
        return respose.json();
    })
    .then(function(data) {
        const movies = data.results;

        movies.forEach(function(movie) {

            const movieTitle = movie.title;
            const listItem = document.createElement("li");
            listItem.textContent = movieTitle
            list_movies.appendChild(listItem);

        });
    })
    .catch(function(error) {
        console.error(error);
    });
