const API_KEY = "";         // Your API key here
const YOUTUBE_LINK = "";    // Youtube link here

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var raw = JSON.stringify({ "link": YOUTUBE_LINK });

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/search/upload/youtube-link", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));