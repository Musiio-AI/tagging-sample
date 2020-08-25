package com.example.tagging;    // Replace it with your own project group ID


import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class AudioLinkUpload {
    private static final String API_KEY = "";       // Your API key
    private static final String URL = "https://api-us.musiio.com/api/v1/upload/audio-link";
    public static void main(String[] args) {
        String audioLink = args[0];      // Input audio link as command argument "-Dexec.args='audio link here'"
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.TEXT_PLAIN);
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();
        ObjectNode requestBody = mapper.createObjectNode();
        requestBody.put("link", audioLink);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toString(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}