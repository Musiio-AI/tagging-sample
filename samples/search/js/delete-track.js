const API_KEY = ""; // Your API key here
const TRACK_ID = "";// Track ID here

var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var requestOptions = {
  method: 'DELETE',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/catalog/track?id=" + TRACK_ID, requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));