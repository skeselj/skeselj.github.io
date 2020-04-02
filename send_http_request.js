console.log("Starting 'text/javascript'");

function handleForm(event) {
    event.preventDefault();
}
form_el = document.getElementById("trigger_form");
form_el.addEventListener('submit', handleForm);

function Trigger() {
    console.log('Trigger');

    // Works when run online, but not for localhost.
    var url = 'https://skeselj.github.io/';
    console.log(` Sending GET request to ${url} `);

    response = httpGet(url);
    console.log(`The response is ${response}`);
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

console.log("Ending 'text/javascript'");
