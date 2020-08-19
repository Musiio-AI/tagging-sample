const API_KEY = "";

var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/catalog/info", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));