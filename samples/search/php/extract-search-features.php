<?php

$curl = curl_init();

$apiKey = "";    // Replace with your API Key
$trackID = "";  // Replace with track ID

$requestBody = json_encode( array( "id"=> $trackID ) );
$authHeader = $apiKey.":"."";
$encodedAuthHeader = base64_encode($authHeader);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api-us.musiio.com/v1/search/extract/search-features",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS =>$requestBody,
  CURLOPT_HTTPHEADER => array(
    "Content-Type: application/json",
    "Authorization: Basic ".$encodedAuthHeader
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>