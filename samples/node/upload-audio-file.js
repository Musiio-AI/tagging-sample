const API_KEY = "";     // API key here
const AUDIO_PATH = "";  // Audio file path here

var axios = require('axios');
var FormData = require('form-data');
var fs = require('fs');
var data = new FormData();
data.append('audio', fs.createReadStream(AUDIO_PATH));

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/api/v1/upload/file',
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
