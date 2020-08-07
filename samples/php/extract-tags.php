<?php

$curl = curl_init();

$apiKey = "";    // Replace with your API Key
$trackId = "";  // Replace with Id of the track

$includeTags = array("CONTENT TYPE", "GENRE V2", "MOOD", "BPM", "KEY SHARP", "ENERGY", "INSTRUMENTATION", "HIT POTENTIAL");
$requestBody = json_encode( array( "id"=>$trackId , "tags"=> $includeTags ) );

$authHeader = $apiKey.":"."";
$encodedAuthHeader = base64_encode($authHeader);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api-us.musiio.com/api/v1/extract/tags",
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