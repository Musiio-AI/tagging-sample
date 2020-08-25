const AUDIO_LINK = "";  // Audio link here
const API_KEY = "";     // API key here

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var raw = JSON.stringify({"link":AUDIO_LINK});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/api/v1/upload/audio-link", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));