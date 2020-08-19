const API_KEY = "";     // API KEY here
const YOUTUBE_LINK = "";// Youtube link here

var axios = require('axios');
var data = JSON.stringify({"link": YOUTUBE_LINK});

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/v1/search/upload/youtube-link',
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
