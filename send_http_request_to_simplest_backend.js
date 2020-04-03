//

function Trigger() {
    console.log('Trigger');

    var ip = '192.168.4.33';
    var url = `${ip}`;
    console.log(`Sending GET request to ${url}`);

    response = httpGet(url);
    console.log(`The response is ${response}`);
}

function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
