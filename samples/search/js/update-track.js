const API_KEY = ""; // Your API key here
const TRACK_ID = "";// Track ID here

var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var formdata = new FormData();
formdata.append("id", TRACK_ID);

// Optional parameters to put in, replace "" with customized values
formdata.append("primary_customer_track_id", "");
formdata.append("version", "");
formdata.append("title", "");
formdata.append("album", "");
formdata.append("artist", "");
formdata.append("year", "");
formdata.append("region", "");
formdata.append("language", "");
formdata.append("explicit", "");
formdata.append("genres", "");
formdata.append("moods", "");
formdata.append("style", "");
formdata.append("instruments", "");
formdata.append("description", "");
formdata.append("keywords", "");

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/catalog/track", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));