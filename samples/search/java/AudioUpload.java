package com.example.search;    // Replace it with your own project group ID

import org.springframework.core.io.FileSystemResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

import java.io.File;

public class AudioUpload {
    private static final String API_KEY = "";       // Your API key
    private static final String URL = "https://api-us.musiio.com/v1/search/upload/file";
    public static void main(String[] args) {
        String audioPath = args[0];     // input audio path in command "-Dexec.args='audio path here'"
        File audioFile = new File(audioPath);
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);
        MultiValueMap<String, Object> requestBody = new LinkedMultiValueMap<>();
        FileSystemResource audioFileResource = new FileSystemResource(audioFile);
        requestBody.add("audio", audioFileResource);
        HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(requestBody, headers
        );
        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> response = restTemplate.postForEntity(URL, requestEntity, String.class);
        System.out.println(response.getBody());
    }
}
