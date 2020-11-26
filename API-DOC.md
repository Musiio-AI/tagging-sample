# Tagging API

## Index

1. [Introduction](#introduction)
2. [API Documentation](#api)
    * Audio Upload
        - [Upload Audio File](#uploadFile)
        - [Upload Audio URL](#uploadAudioLink)
    * [Extract Tags](#extractTags)
    * API Usage
        - [Get Usage for Date Range](#usageDateRange)
        - [Daily Aggregated Usage](#dailyUsage)
        - [Monthly Aggregated Usage](#dailyUsage)
    * [Register Feedback for Tags](#feedback)
3. [List of Tag Outputs](#listTags)

## <a name="introduction">Introduction</a>

This document outlines the specifications of the Musiio Tagging API.

### API Endpoint

https://api-us.musiio.com/v1/tagging

### Authentication

For authentication, pass the API key in the HTTP auth header as
*username* and keep the *password* field blank.

### Supported Audio Formats

- MP3
- M4A
- WAV
- WMA
- ALAC
- FLAC
- OGG
- AAC
- MP4
- MP2
- AIFF
- AIF
- AIFC

### HTTP Error Codes

The API uses [standard HTTP error codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) along with custom error codes as shown below:

#### Standard HTTP Error Codes

| HTTP Error Code | Explanation                                                  |
| :-------------: | :----------------------------------------------------------- |
|     **400**     | The server could not understand the request due to invalid syntax. |
|     **401**     | Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response. |
|     **403**     | The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401, the client's identity is known to the server. |
|     **404**     | The server can not find the requested resource. |
|     **408**     | The server timed out waiting for the request. |
|     **413**     | Request entity is larger than limits defined by server. |
|     **500**     | A generic error message, given when an unexpected condition was encountered. |
|     **503**     | The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. |

#### Custom Error Codes

| HTTP Error Code | Explanation                                                  |
| :-------------: | ------------------------------------------------------------ |
|     **461**     | The uploaded seed track (either from a file upload or a youtube link) was too short in duration |
|     **462**     | An error was encountered while trying to post a youtube link |
|     **466**     | Customer account cannot access the requested resource because there are no active subscriptions |

---

## <a name="api">API Documentation</a>

### <a name="uploadfile">[POST] /upload/file</a>

Uploads and performs feature extraction on an audio file. Supported formats are ["wav", "mp3", "m4a"].
The method accepts one "audio" file.

Request
- file with key "audio"

Response - Json

```json
{
    "version": "integer",
    "success": "boolean",
    "id": "string",
    "error": ["string", null]
}
```

### <a name="uploadAudioLink">[POST] /upload/audio-link</a>

Performs feature extraction on a given URL to a track
(can be a Youtube/SoundCloud link as well)

Request - JSON

```json
{
    "link": "string"
}
```

Response - JSON

```json
{
    "version": "integer",
    "success": "boolean",
    "id": "string",
    "error": ["string", null]
}
```

---

### <a name="extractTags">[POST] /extract/tags</a>

Extracts tags for an already uploaded track. Requires the id returned for an uploaded track. <br>
Valid values for tags are: "CONTENT TYPE", "GENRE", "GENRE V2", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "KEY FLAT", "ENERGY", "INSTRUMENTATION"

Request - JSON
```json
{
	"id": string,
	"tags": [string, ...]
}
```

Response - JSON
```json
{
	"tags": [{
		"type": string,
		"name": string,
		"score": integer
	}, {}, ...],
	"success": boolean,
	"error": string
}
```

Example Response
```json
{
	"success": true,
	"tags": [{
		"type": "CONTENT TYPE",
		"score": 100,
		"name": "music"
	}, {
		"type": "QUALITY",
		"score": 2,
		"name": "high"
	}],
	"version": 1
}
```

---

### <a name="usageDateRange">[POST] /usage</a>

Get API usage volume for all method calls within the specified time period.
An empty object return data for the last calendar month.

Request - JSON
```json
{
	"start_date": "yyyy-mm-dd",
	"end_date": "yyyy-mm-dd"
}
```

Response - JSON
```json
{
	"usage": [{
   		"type": "TAG",
 		"value": "GENRE",
   		"count": integer
	},
	{
 		"type": "TAG",
 		"value": "CONTENT TYPE",
   		"count": integer
	}
		...
	],
	"success": boolean,
	"error": string
}
```

### <a name="dailyUsage">[GET] /usage/daily?year=yyyy&month=mm&tag=name</a>

Get daily aggregated tagging usage for a particular tag.

Sample request:

```/usage/daily?year=2020&month=11&tag=BPM```

Response:
```json
{
    "usage":
    [
        {
          "day": "1",
          "count": 2
        }
    ],
    "total-usage": 25
}
```

### <a name="monthlyUsage">[GET] /usage/monthly?year=yyyy&tag=name</a>

Get monthly aggregated tagging usage for a particular tag.

Sample request:

```/usage/monthly?year=2020&tag=BPM```

Response:
```json
{
    "usage":
    [
        {
          "month": "1",
          "count": 2
        }
    ],
    "total-usage": 25
}
```

---

### <a name="feedback">[POST] /feedback</a>

Records feedback on the tagging AI performance.
This feedback will be used to correct errors and to improve future versions of the AI.

Valid values for tag type are:
`"CONTENT TYPE", "GENRE", "GENRE V2", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "KEY FLAT", "ENERGY", "INSTRUMENTATION"`

The `track_id` should be replaced by the id returned from the upload request for the song the feedback is for.

- The rejected array are tags that were incorrect for the track_id for the specified tag type.

- The confirmed array are tags that were correct for the track_id for the specified tag type.

#### Structure
Request - JSON

```json
{
    "feedback": {
        "{{track_id}}": {
            "tag_type": string,
            "rejected": [string, ...],
            "confirmed": [string, ...]
        }
    }
}
```
Response - JSON

```json
{
    "message": string,
    "success": boolean,
    "version": integer,
    "error": ["string", null]
}
```

#### Example
Request
```json
{
    "feedback": {
        "TMP_123456": {
            "tag_type": "GENRE V3",
            "rejected": ["jazz", "blues"],
            "confirmed": ["pop", "indie"]
        }
    }
}
```

Response
```json
{
    "message": "feedback registered successfully",
    "success": true,
    "version": 1
}
```

---

## <a name="listTags">List of Tag Outputs</a>

| FIELD "type"                                                               | FIELD "name"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | FIELD "score"                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **"CONTENT TYPE"**                                                                                                             | "music", "speech", or "unknown"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 0-100 (match probability)                                                                                                                                                                                                  |
| **"QUALITY"**                                                                                                                  | "low", "medium", "high", or "very high"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 0-100 (quality score). *The score reflects the perceived recording and mastering level of the audio, ranging from 0 to 100.* The thresholds for the score are: "very high" >= 85, "high" >= 70, "medium" >= 40, "low" < 40 |
| **"GENRE"**                                                                                                                    | "blues", "chill", "classical", "easy listening", "disco", "funk", "pop", "rnb", "soul", "hiphop", "jazz", "electronic", "house", "techno", "trance", "indie", "folk", "country", "metal", or "rock"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0-100 (match probability)                                                                                                                                                                                                  |
| **"GENRE SECONDARY"**                                                                                                          | "blues", "chill", "classical", "easy listening", "disco", "funk", "pop", "rnb", "soul", "hiphop", "jazz", "electronic", "house", "techno", "trance", "indie", "folk", "country", "metal", or "rock"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0-100 (match probability)                                                                                                                                                                                                  |
| **"GENRE V3"** **Returns up to 4 different tags with the same field type.*                                                     | "80s Pop", "Adult Contemporary", "Afro", "Afrobeat", "Afropop", "Alternative Hip Hop", "Alternative R&B", "Alternative Rock", "Ambient", "Bebop", "Bluegrass", "Blues", "Blues Rock", "Breakbeat", "Classic Blues", "Classic Country", "Classic Metal", "Classic Rock", "Classical", "Classical Instruments", "Classical Vocals", "Contemporary Pop", "Country", "Country Pop & Rock", "Dance R&B", "Dancehall", "Death Metal", "Disco", "Downtempo", "Drum & Bass", "Dub", "Dubstep", "Early Soul", "Easy Listening", "EDM", "Electro Pop", "Electronic", "Folk", "Funk", "Gospel", "Hard Rock", "Hardcore", "Heavy Metal", "Hip Hop", "House", "Indian", "Indie", "Indie Rock", "Indietronica", "Industrial", "J-Pop", "J-Rock", "Jazz", "Jazz Fusion", "Latin", "Latin Pop", "Mandopop", "Metal", "Metalcore", "Neo Soul", "Nu Metal", "Old School Hip Hop", "Pop", "Pop Rap", "Pop Rock", "Punk", "Punk Rock", "R&B", "Reggae", "Reggaeton", "Rock", "Rock & Roll", "Salsa", "Ska", "Smooth Jazz and Vocal Jazz", "Soul", "Smooth R&B", "Swing", "Synthwave", "Techno", "Thrash Metal", "Trance", "Trap", "UK Grime"| 0-100 (match probability)                                                                                                                                                                                                  |
| **"MOOD"**                                                                                                                     | "angry", "dark", "dramatic", "energetic", "exciting", "happy", "majestic", "neutral", "powerful", "quirky", "relaxed", "romantic", "sad", "scary", or "tense"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0-100 (match probability)                                                                                                                                                                                                  |
| **"MOOD SECONDARY"**                                                                                                           | "angry", "dark", "dramatic", "energetic", "exciting", "happy", "majestic", "neutral", "powerful", "quirky", "relaxed", "romantic", "sad", "scary", or "tense"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0-100 (match probability)                                                                                                                                                                                                  |
| **"MOOD VALENCE"**                                                                                                             | "negative", "neutral",or "positive"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0-100 (match probability)                                                                                                                                                                                                  |
| **"BPM"**                                                                                                                      | "<=60", "61", â¦ , "179" or ">=180"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | bpm value (integer in range 60-180)                                                                                                                                                                                        |
| **"BPM ALT"**                                                                                                                  | "<=60", "61", â¦ , "179" or ">=180"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | bpm value (integer in range 60-180)                                                                                                                                                                                        |
| **"BPM VARIATION"**                                                                                                            | "small", "medium", or "large"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1-3                                                                                                                                                                                                                        |
| **"KEY"**                                                                                                                      | "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B", "7A", "7B", "8A", "8B", "9A", "9B", "10A", "10B", "11A", "11B", "12A", "12B"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 0-100 (match probability)                                                                                                                                                                                                  |
| **"KEY SECONDARY"***                                                                                                           | "1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B", "6A", "6B", "7A", "7B", "8A", "8B", "9A", "9B", "10A", "10B", "11A", "11B", "12A", "12B"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 0-100 (match probability)                                                                                                                                                                                                  |
| **"KEY SHARP"**                                                                                                                | "G# minor", "B major", "D# minor", "F# major", "A# minor", "C# major", "F minor", "G# major", "C minor", "D# major", "G minor", "A# major", "D minor", "F major",  "A minor", "C major",  "E minor", "G major",  "B minor", "D major",  "F# minor", "A major", "C# minor", "E major"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 0-100 (match probability)                                                                                                                                                                                                  |
| **"KEY SHARP SECONDARY"***                                                                                                     | "G# minor", "B major", "D# minor", "F# major", "A# minor", "C# major", "F minor", "G# major", "C minor", "D# major", "G minor", "A# major", "D minor", "F major",  "A minor", "C major",  "E minor", "G major",  "B minor", "D major",  "F# minor", "A major", "C# minor", "E major"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 0-100 (match probability)                                                                                                                                                                                                  |
| **"KEY FLAT"**                                                                                                                 | "Ab minor", "B major", "Eb minor", "Gb major", "Bb minor", "Db major", "F minor", "Ab major", "C minor", "Eb major", "G minor", "Bb major", "D minor", "F major",  "A minor", "C major","E minor", "G major", "B minor", "D major", "Gb minor", "A major", "Db minor", "E major"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0-100 (match probability)                                                                                                                                                                                                  |
| **"KEY FLAT SECONDARY"***                                                                                                      | "Ab minor", "B major", "Eb minor", "Gb major", "Bb minor", "Db major", "F minor", "Ab major", "C minor", "Eb major", "G minor", "Bb major", "D minor", "F major",  "A minor", "C major","E minor", "G major", "B minor", "D major", "Gb minor", "A major", "Db minor", "E major"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 0-100 (match probability)                                                                                                                                                                                                  |
| **"ENERGY"**                                                                                                                   | "very low", "low", "medium", "high", or "very high"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 0-100 (match probability)                                                                                                                                                                                                  |
| **"ENERGY VARIATION"**                                                                                                         | "small", "medium", or "large"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 1-3                                                                                                                                                                                                                        |
| **"INSTRUMENTATION"**                                                                                                          | "vocal", or "instrumental"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 0-100 (match probability)                                                                                                                                                                                                  |
| **"VOCAL PRESENCE"**                                                                                                           | "none", "low", "medium", or "high"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 1-4                                                                                                                                                                                                                        |
| **"VOCAL GENDER"**                                                                                                             | "male", "female", "mixed"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 0-100 (match probability)                                                                                                                                                                                                  |
| **"INSTRUMENT"**  The type = "INSTRUMENT" tag can occur *multiple times*, since multiple simultaneous positives are possible.  | "percussion", "electric guitar", "bass guitar", "acoustic guitar", "piano" "strings", "brass"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 0-100 (match probability)                                                                                                                                                                                                  |

### Key Translations

##### KEYS_SHARP
<br />

|    Key    |   Translation   |
| --------- | --------------- |
| **1A**    | G# minor    |
| **2A**    | D# minor    |
| **3A**    | A# minor    |
| **4A**    | F minor     |
| **5A**    | C minor     |
| **6A**    | G minor     |
| **7A**    | D minor     |
| **8A**    | A minor     |
| **9A**    | E minor     |
| **10A**   | B minor     |
| **11A**   | F# minor    |
| **12A**   | C# minor    |
| **1B**    | B major     |
| **2B**    | F# major    |
| **3B**    | C# major    |
| **4B**    | G# major    |
| **5B**    | D# major    |
| **6B**    | A# major    |
| **7B**    | F major     |
| **8B**    | C major     |
| **9B**    | G major     |
| **10B**   | D major     |
| **11B**   | A major     |
| **12B**   | E major     |

<br />

##### KEYS_FLAT

<br />

| Key              |   Translation   |
| ---------------- | --------------- |
| **1A**               | Ab minor    |
| **2A**               | Eb minor    |
| **3A**               | Bb minor    |
| **4A**               | D minor     |
| **5A**               | C minor     |
| **6A**               | G minor     |
| **7A**               | D minor     |
| **8A**               | A minor     |
| **9A**               | E minor     |
| **10A**              | B minor     |
| **11A**              | Gb minor    |
| **12A**              | Db minor    |
| **1B**               | B major     |
| **2B**               | Gb major    |
| **3B**               | Db major    |
| **4B**               | Ab major    |
| **5B**               | Eb major    |
| **6B**               | Bb major    |
| **7B**               | F major     |
| **8B**               | C major     |
| **9B**               | G major     |
| **10B**              | D major     |
| **11B**              | A major     |
| **12B**              | E major     |
