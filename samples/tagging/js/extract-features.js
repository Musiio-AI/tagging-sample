const API_KEY = ""; // API Key here
const TRACK_ID = "";// Track ID here

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var raw = JSON.stringify({ 
    "id": TRACK_ID, 
    "tags": [
        "CONTENT TYPE", 
        "GENRE V3", 
        "MOOD", 
        "BPM", 
        "KEY", 
        "KEY SHARP", 
        "ENERGY", 
        "INSTRUMENTATION"
    ] 
});

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("https://api-us.musiio.com/api/v1/extract/tags", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));