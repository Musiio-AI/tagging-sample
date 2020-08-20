const API_KEY = ""; // Your API Key here

var axios = require('axios');

var config = {
  method: 'get',
  url: 'https://api-us.musiio.com/v1/catalog/info',
  auth: {
      username: API_KEY,
      password: ""
  }
};

axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});
