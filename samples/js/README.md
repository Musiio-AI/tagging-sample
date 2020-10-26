# Javascript Samples

JavaScript (frontend) tagging samples are to be integrated with a frontend web application.
Constants required are to be passed in. Response will be logged in web client console.

## Upload Audio File

[upload-audio-file.js](upload-audio-file.js)

Input required `API_KEY`

Input file needs to be obtained from the `<input>` tag, as shown in the example below:

 ```html
<input type="file" id="fileInput">
...
<script>
    var fileInput = document.getElementById("fileInput");
</script>
 ```

## Upload YouTube Link

[upload-youtube-link.js](upload-youtube-link.js)

Input required `API_KEY`, `YOUTUBE_LINK`.

## Upload Audio Link

[upload-audio-link.js](upload-audio-link.js)

Input required `API_KEY`, `AUDIO_LINK`.

## Extract Tags

[extract-tags.js](extract-tags.js)

Input required `API_KEY`, `TRACK_ID`.

Available tags:

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`
