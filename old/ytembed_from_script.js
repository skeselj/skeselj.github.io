console.log("Starting 'text/javascript'");

// Prevent page from refreshing when form is submitted.
function handleForm(event) {
    event.preventDefault();
}
form_el = document.getElementById("ytembed_config_form");
form_el.addEventListener('submit', handleForm);

function UpdateInfo() {
    ytid = document.getElementById("ytid-property").value;
    start_t = document.getElementById("start-property").value;
    end_t = document.getElementById("end-property").value;

    new_src = `https://www.youtube.com/embed/${ytid}?start=${start_t}&end=${end_t}`;
    console.log('new_src = ' + new_src);
    document.getElementById('ytembed_iframe').src = new_src;
}

// By default, set the ytid to a Historius Civils video.
var ytid = "LOCBWh5Iwm4";

// Setup default.
var iframe = document.createElement('iframe');   // Of type iframe.
iframe.setAttribute("id", "ytembed_iframe");

iframe.width = "560";
iframe.height = "315";
iframe.src = `https://www.youtube.com/embed/${ytid}`;
iframe.frameborder = "0";
iframe.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";

document.body.appendChild(iframe);

console.log("Ending 'text/javascript'");