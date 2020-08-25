const API_KEY = "";     // API key here
const AUDIO_LINK = "";  // Audio link here

var axios = require('axios');
var data = JSON.stringify({"link": AUDIO_LINK});

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/api/v1/upload/audio-link',
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
