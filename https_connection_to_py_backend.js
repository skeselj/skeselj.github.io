// Library function to send request.

function SendRequest() {
    var addr = `https://192.168.4.33:4443`;
    console.log(`Sending GET request to ${addr}`);

    response = httpGet(addr);
    console.log(`The response is ${response}`);
}

function httpGet(addr) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", addr, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

