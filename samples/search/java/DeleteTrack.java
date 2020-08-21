package com.example.search;     // Replace it with your own project group ID

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class DeleteTrack {
    private static final String API_KEY = "";       // Your API key
    private static final String URL = "https://api-us.musiio.com/v1/catalog/track?id=";
    public static void main(String[] args) {
        String trackId = args[0];   // input track ID in command: "-Dexec.args='track id here'"
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        RestTemplate restTemplate = new RestTemplate();
        HttpEntity<String> requestEntity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(URL + trackId, HttpMethod.DELETE, requestEntity, String.class);
        System.out.println(response.getBody());
    }
}