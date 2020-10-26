# Node.js Samples

## Set up dependencies

```bash
cd samples/tagging/node
npm install
```

## Upload Audio File

Open the [upload-audio-file.js](upload-audio-file.js) file, replace `API_KEY` `AUDIO_PATH` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service.

To run:
```bash
node upload-audio-file.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

**For large files**

[Axios](https://github.com/axios/axios) has a default request body size of [2000 bytes](https://github.com/axios/axios#request-config). To change that, simply modify `maxBodyLength` in the configuration as one of the `Axios` request function arguments like this:

```js
var config = {
  method: 'post',
  url: 'https://api-us.musiio.com/api/v1/upload/file',
  auth: {
    username: API_KEY,
    password: ""
  },
  headers: {
    ...data.getHeaders()
  },
  data : data,
  maxBodyLength: 10000 // specify the request body length here!
};
```

## Upload YouTube Link

Open the [upload-youtube-link.js](upload-youtube-link.js) file, replace `API_KEY` `YOUTUBE_LINK` with your own API key and the youtube track link.
This script uploads the youtube track onto Musiio Tagging Service.

To run:
```bash
node upload-youtube-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

## Upload Audio Link

Open the [upload-audio-link.js](upload-audio-link.js) file, replace `API_KEY` `AUDIO_LINK` with your own API key and the youtube track link.
This script uploads the youtube track onto Musiio Tagging Service.

To run:
```bash
node upload-audio-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

## Extract Tags

Open the [extract-tags.js](extract-tags.js) file, replace `API_KEY` `TRACK_ID` with your own API key and the Track ID generated after the upload.
This script will run the Tagging Service and return the tagging results.

```bash
node extract-tags.js
```

The response will be printed out in the console.