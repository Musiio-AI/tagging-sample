const API_KEY = "";     // API Key here
const TRACK_ID = "";    // Track ID here

var axios = require('axios');

var config = {
  method: 'get',
  url: `https://api-us.musiio.com/v1/catalog/track?id=${TRACK_ID}`,
  auth: {
      username: API_KEY,
      password
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
