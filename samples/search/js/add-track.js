// fileInput is the input element on your webpage
/* HTML
<input type="file" id="fileInput">
<script>
    var fileInput = document.getElementById("fileInput");
</script>
*/

const API_KEY = ""; // Your API key here

var myHeaders = new Headers();
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var formdata = new FormData();
formdata.append("track", fileInput.files[0], "file");

// Optional parameters to put in, replace "" with customized values
formdata.append("customer_track_id", "");
formdata.append("primary_customer_track_id", "");
formdata.append("version", "");
formdata.append("title", "");
formdata.append("album", "");
formdata.append("artist", "");
formdata.append("year", "");
formdata.append("region", "");
formdata.append("language", "");
formdata.append("explicit", "");
formdata.append("genre", "");
formdata.append("moods", "");
formdata.append("style", "");
formdata.append("instruments", "");
formdata.append("description", "");
formdata.append("keywords", "");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/catalog/track", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));