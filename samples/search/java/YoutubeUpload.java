package com.example.search;    // Replace it with your own project group ID

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class YoutubeUpload {
    private static final String API_KEY = "";       // Your API key here
    private static final String URL = "https://api-us.musiio.com/v1/search/upload/youtube-link";

    public static void main(String[] args) {
        String youtubeLink = args[0];  // input youtube link in command: "-Dexec.args='youtube link here'"
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.TEXT_PLAIN);
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();
        ObjectNode requestBody = mapper.createObjectNode();        
        requestBody.put("link", youtubeLink);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toString(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}