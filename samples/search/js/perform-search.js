const API_KEY = "";     // Your API key here
const TRACK_ID = "";    // Track ID here
const SEARCH_TEXT = ""; // Search text input
const PAGE = 0;             // page number
const ITEMS_PER_PAGE = 50;  // items per page

var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", "Basic " + btoa(API_KEY + ":"));

var raw = JSON.stringify({ 
    "id": TRACK_ID, 
    "text": SEARCH_TEXT, 
    "page": PAGE, 
    "items": ITEMS_PER_PAGE
});

var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
};

fetch("https://api-us.musiio.com/v1/search/perform", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));