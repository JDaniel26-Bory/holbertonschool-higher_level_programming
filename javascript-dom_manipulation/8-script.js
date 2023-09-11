// references of the HTML
url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

// Fetch data from the URL
fetch(url)
    .then(function (response) {
        if (!response.ok) {
            throw new Error("Network Response was not ok");
        }
        // Parse the JSON Response
        return response.json();
    })
    .then(function(data) {
        hello.textContent = data.hello;
    })
    .catch(function(error) {
        console.error(error);
    });
