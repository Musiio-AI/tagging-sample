package com.example.search;     // Replace it with your own project group ID

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class GetSearchDictionary {
    private static final String API_KEY = "";       // Your API key
    private static final String URL = "https://api-us.musiio.com/v1/search/dictionary";
    public static void main(String[] args) {
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        RestTemplate restTemplate = new RestTemplate();
        HttpEntity<String> requestEntity = new HttpEntity<>(headers);
        ResponseEntity<String> response = restTemplate.exchange(URL, HttpMethod.GET, requestEntity, String.class);
        System.out.println(response.getBody());
    }
}