<?php

$curl = curl_init();

$apiKey = "";    // Replace with your API Key. Required
$track_id = "";  // Replace with the track ID. Required
$customer_track_id = "";
$primary_customer_track_id = "";
$version = "";
$title = "";
$album = "";
$artist = "";
$year = "";
$region = "";
$language = "";
$explicit = "";
$genre = "";
$moods = "";
$style = "";
$instruments = "";
$description = "";
$keywords = "";

$requestBody = array(
  'id' => $track_id,
  'customer_track_id' => $customer_track_id,
  'primary_customer_track_id' => $primary_customer_track_id,
  'version' => $version,
  'title' => $title,
  'album' => $album,
  'artist' => $artist,
  'year' => $year,
  'region' => $region,
  'language' => $language,
  'explicit' => $explicit,
  'genre' => $genre,
  'moods' => $moods,
  'style' => $style,
  'instruments' => $instruments,
  'description' => $description,
  'keywords' => $keywords
);

$authHeader = $apiKey.":"."";
$encodedAuthHeader = base64_encode($authHeader);

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api-us.musiio.com/v1/catalog/track",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "PUT",
  CURLOPT_POSTFIELDS => $requestBody,
  CURLOPT_HTTPHEADER => array(
    "Authorization: Basic ".$encodedAuthHeader
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
?>