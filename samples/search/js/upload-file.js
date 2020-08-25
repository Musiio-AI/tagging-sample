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
formdata.append("audio", fileInput.files[0], "file");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/search/upload/file", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));