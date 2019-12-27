KEY = "Replace With Your API KEY"

BASE_URL = "Replace with Your API URL"

TAG_URL = BASE_URL + "/api/v1/extract/tags"

UPLOAD_URL = BASE_URL + "/api/v1/upload/file"

VALID_TAGS = ["CONTENT TYPE", "QUALITY", "GENRE", "GENRE SECONDARY", "GENRE V2", "BPM", "BPM ALT", "BPM VARIATION", "KEY", "KEY SECONDARY", "MOOD", "MOOD SECONDARY",
              "MOOD VALENCE", "ENERGY", "ENERGY VARIATION", "INSTRUMENTATION", "VOCAL PRESENCE", "VOCAL GENDER", "INSTRUMENT"]

TAGS = ["CONTENT TYPE", "GENRE", "GENRE V2", "BPM", "KEY", "MOOD", "ENERGY", "INSTRUMENTATION"]

KEY_MAPPING = {
    "1A": "Ab minor",
    "2A": "Eb minor",
    "3A": "Bb minor",
    "4A": "F minor",
    "5A": "C minor",
    "6A": "G minor",
    "7A": "D minor",
    "8A": "A minor",
    "9A": "E minor",
    "10A": "B minor",
    "11A": "F# minor",
    "12A": "Db minor",
    "1B": "B major",
    "2B": "F# major",
    "3B": "Db major",
    "4B": "Ab major",
    "5B": "Eb major",
    "6B": "Bb major",
    "7B": "F major",
    "8B": "C major",
    "9B": "G major",
    "10B": "D major",
    "11B": "A major",
    "12B": "E major"
}