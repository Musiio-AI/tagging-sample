# PHP Samples

## Upload Audio File

[audio-upload.php](audio-upload.php)

Open the file, replace `$apiKey` `$audioPath` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php audio-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

## Upload YouTube Link

[youtube-upload.php](youtube-upload.php)

Open the file, replace `$apiKey` `$youtubeUrl` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php youtube-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

## Upload Audio Link

[upload-audio-link.php](upload-audio-link.php)

Open the file, replace `$apiKey` `$audioLink` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php upload-audio-link.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

## Extract Tags

[extract-tags.php](extract-tags.php)

Open the file, replace `$apiKey` `$trackId` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.

```bash
php extract-tags.php
```

The response will be printed out in the console.