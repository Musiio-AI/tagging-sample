const API_KEY = ""; // Your API Key here
const TRACK_ID = "";// Track ID here

var axios = require('axios');
var data = JSON.stringify({"id": TRACK_ID});

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/v1/search/extract/search-features',
  auth: {
      username: API_KEY,
      password: ""
  },
  headers: { 
    'Content-Type': 'application/json'
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
