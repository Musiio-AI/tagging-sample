<?php

$curl = curl_init();

$apiKey = "";    // Replace with your API Key. Required
$track_id = "";  // Replace with the track ID. Required
$authHeader = $apiKey.":"."";
$encodedAuthHeader = base64_encode($authHeader);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api-us.musiio.com/v1/catalog/track?id=".$track_id,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Basic ".$encodedAuthHeader
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>