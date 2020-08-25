const API_KEY = ""; // Your API key here

var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/search/dictionary", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));