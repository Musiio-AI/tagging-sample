package com.example.search;    // Replace it with your own project group ID

import com.github.cliftonlabs.json_simple.JsonObject;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class ExtractSearchFeatures {
    private static final String TRACK_ID = "";  // Your Track ID here
    private static final String API_KEY = "";   // Your API Key here
    private static final String URL = "https://api-us.musiio.com/v1/search/extract/search-features";

    public static void main(String[] args) {
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.APPLICATION_JSON);
        RestTemplate restTemplate = new RestTemplate();
        JsonObject requestBody = new JsonObject();
        requestBody.put("id", TRACK_ID);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toJson(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}
