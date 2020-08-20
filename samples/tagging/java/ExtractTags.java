package com.example.tagging;    // Replace it with your own project group ID

import com.github.cliftonlabs.json_simple.JsonObject;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class ExtractTags {
    private static final String TRACK_ID = "";
    private static final String API_KEY = "";
    private static final String URL = "https://api-us.musiio.com/api/v1/extract/tags";
    private static final String[] TAGS = new String[]{
        "CONTENT TYPE", 
        "GENRE V3", 
        "MOOD", 
        "BPM", 
        "KEY",
        "KEY SHARP", 
        "ENERGY", 
        "INSTRUMENTATION"
    };

    public static void main(String[] args) {
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.APPLICATION_JSON);
        RestTemplate restTemplate = new RestTemplate();
        JsonObject requestBody = new JsonObject();
        requestBody.put("id", TRACK_ID);
        requestBody.put("tags", TAGS);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toJson(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}
