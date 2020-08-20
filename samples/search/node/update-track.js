const API_KEY = "";     // API Key here
const TRACK_ID = "";    // Track ID here

var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();
data.append('id', TRACK_ID);
data.append('primary_customer_track_id', '');
data.append('version', '');
data.append('title', '');
data.append('album', '');
data.append('artist', '');
data.append('year', '');
data.append('region', '');
data.append('language', '');
data.append('explicit', '');
data.append('genres', '');
data.append('moods', '');
data.append('style', '');
data.append('instruments', '');
data.append('description', '');
data.append('keywords', '');

var config = {
  method: 'put',
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
