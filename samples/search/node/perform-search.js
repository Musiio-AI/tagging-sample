const API_KEY = "";     // Your API Key here
const TRACK_ID = "";    // Track ID here
const SEARCH_TEXT = ""; // Search text here
const PAGE = 0;         // the page number
const ITEMS_PER_PAGE = 50;  // number of items per page

var axios = require('axios');
var data = JSON.stringify(
    {
        "id": TRACK_ID,
        "text": SEARCH_TEXT,
        "page": PAGE,
        "items": ITEMS_PER_PAGE
    }
);

var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/v1/search/perform',
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
