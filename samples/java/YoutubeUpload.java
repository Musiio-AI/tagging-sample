package com.example.tagging;    // Replace it with your own project group ID

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class YoutubeUpload {
    private static final String API_KEY = "";       // Your API key here
    private static final String URL = "https://api-us.musiio.com/api/v1/upload/youtube-link";

    public static void main(String[] args) {
        String youtubeLink = args[0];    // Input Youtube link as command argument "-Dexec.args='youtube link here'"
        System.out.println(youtubeLink);
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.TEXT_PLAIN);
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();
        ObjectNode requestBody = mapper.createObjectNode();
        requestBody.put("link", youtubeLink);
        System.out.println(requestBody.toString());
        HttpEntity<String> request = new HttpEntity<>(requestBody.toString(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}