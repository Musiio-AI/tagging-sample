package com.example.tagging;    // Replace it with your own project group ID

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class ExtractTags {
    private static final String API_KEY = "";   // Your API key here
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
        String trackId = args[0];   // Input track ID as command argument "-Dexec.args='track id here'"
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.APPLICATION_JSON);
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();
        ObjectNode requestBody = mapper.createObjectNode();
        requestBody.put("id", trackId);
        ArrayNode tags = mapper.valueToTree(TAGS);
        requestBody.putArray("tags").addAll(tags);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toString(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}
