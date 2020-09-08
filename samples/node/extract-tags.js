const API_KEY = "";     // API Key here
const TRACK_ID = "";    // Track ID here

var axios = require('axios');
var data = JSON.stringify(
    {
        "id": TRACK_ID,
        "tags":
        [
            "CONTENT TYPE",
            "GENRE V3",
            "MOOD",
            "BPM",
            "KEY",
            "KEY SHARP",
            "ENERGY",
            "INSTRUMENTATION"
        ]
    }
);

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/api/v1/extract/tags',
  auth: {
      username: API_KEY,
      password: ''
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
