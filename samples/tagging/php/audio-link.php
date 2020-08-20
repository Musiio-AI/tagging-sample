<?php

$curl = curl_init();

$apiKey = "";    // Replace with your API Key
$audioLink = "";  // Replace with Audio Link to be tagged

$requestBody = json_encode( array( "link"=> $audioLink ) );
$authHeader = $apiKey.":"."";
$encodedAuthHeader = base64_encode($authHeader);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api-us.musiio.com/api/v1/upload/audio-link",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => $requestBody,
  CURLOPT_HTTPHEADER => array(
    "Authorization: Basic ".$encodedAuthHeader,
    "Content-Type: application/json"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>