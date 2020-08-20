package com.example.tagging;    // Replace it with your own project group ID

import com.github.cliftonlabs.json_simple.JsonObject;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class AudioLinkUpload {
    private static final String AUDIO_LINK = "";    // Your audio link here
    private static final String API_KEY = "";       // Your API key
    private static final String URL = "https://api-us.musiio.com/api/v1/upload/audio-link";
    public static void main(String[] args) {
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.TEXT_PLAIN);
        RestTemplate restTemplate = new RestTemplate();
        JsonObject requestBody = new JsonObject();
        requestBody.put("link", AUDIO_LINK);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toJson(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}