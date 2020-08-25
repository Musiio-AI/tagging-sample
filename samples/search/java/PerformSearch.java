package com.example.search;    // Replace it with your own project group ID

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ObjectNode;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.client.RestTemplate;

public class PerformSearch {
    private static final String API_KEY = "";   // Your API Key here
    private static final String URL = "https://api-us.musiio.com/v1/search/perform";

    public static void main(String[] args) {
        String trackId = args[0]; // input track ID in command: "-Dexec.args='track id here...'"
        String searchText = "";
        int page = 0;
        int items = 50;
        try {
            searchText = args[1];
            page = Integer.parseInt(args[2]);
            items = Integer.parseInt(args[3]);
        } catch (NumberFormatException e) {
            System.err.println("Please enter integer values for 3rd and 4th arguments if needed");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Use default values for optional arguments");
        }
        HttpHeaders headers = HeadersUtils.createHeaders(API_KEY, "");
        headers.setContentType(MediaType.APPLICATION_JSON);
        RestTemplate restTemplate = new RestTemplate();
        ObjectMapper mapper = new ObjectMapper();
        ObjectNode requestBody = mapper.createObjectNode();
        requestBody.put("id", trackId);
        requestBody.put("text", searchText);
        requestBody.put("page", page);
        requestBody.put("items", items);
        HttpEntity<String> request = new HttpEntity<>(requestBody.toString(), headers);
        String response = restTemplate.postForObject(URL, request, String.class);
        System.out.println(response);
    }
}
