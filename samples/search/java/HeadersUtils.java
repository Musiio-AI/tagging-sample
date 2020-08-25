package com.example.search;    // Replace it with your own project group ID

import org.springframework.http.HttpHeaders;
import org.springframework.util.Base64Utils;

import java.nio.charset.StandardCharsets;

public class HeadersUtils {

    public static HttpHeaders createHeaders(String username, String password) {
        String auth = username + ":" + password;
        byte[] encodedAuth = Base64Utils.encode(auth.getBytes(StandardCharsets.US_ASCII));
        String authHeader = "Basic " + new String(encodedAuth);
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.set("Authorization", authHeader);
        return httpHeaders;
    }
}
