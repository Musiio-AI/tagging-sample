const API_KEY = "";     // Your API Key here
const AUDIO_PATH =  ""; // Audio file path here

var axios = require('axios');
var FormData = require('form-data');
var fs = require('fs');
var data = new FormData();
data.append('track', fs.createReadStream(AUDIO_PATH));
data.append('customer_track_id', '');
data.append('primary_customer_track_id', '');
data.append('version', '');
data.append('title', '');
data.append('album', '');
data.append('artist', '');
data.append('year', '');
data.append('region', '');
data.append('language', '');
data.append('explicit', '');
data.append('genre', '');
data.append('moods', '');
data.append('style', '');
data.append('instruments', '');
data.append('description', '');
data.append('keywords', '');

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/v1/catalog/track',
  auth: {
      username: API_KEY,
      password: ""
  },
  headers: { 
    ...data.getHeaders()
  },
  data : data
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
