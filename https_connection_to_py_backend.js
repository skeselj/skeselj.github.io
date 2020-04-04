//

function Trigger() {
    console.log('Trigger');

    var ip = '192.168.4.33';
    var url = `http://${ip}:8080`;
    console.log(`Sending GET request to ${url}`);

    response = httpGet(url);
    console.log(`The response is ${response}`);
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    // xmlHttp.setRequestHeader('Access-Control-Allow-Headers', '*');  // doesn't work.. probably need to write this in the script.
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

