const YOUTUBE_LINK = "";  // Youtube link here
const API_KEY = "";       // API key here

var axios  = require('axios');
var data = JSON.stringify({"link": YOUTUBE_LINK});

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/api/v1/upload/youtube-link',
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

