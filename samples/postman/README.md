## Postman Collection

If you don't have postman, download here: https://www.postman.com/downloads/

Here is the collection public URL:

https://www.getpostman.com/collections/2d47eb75d66a50ed4308

## How to set up postman samples

1. Download postman and install it.
2. Open postman, at the top left corner click on "Import" button
3. Choose "Link" tab
4. Copy paste the collection public link in and click "Continue"
5. Press "Import" to import the collection
6. You will see the collection folder appears on the left-side panel. Click to expand to see individual request query.
7. Now you need to add your API key in to authorize your request. Click on the "three dots" icon on the right of the collection folder tab when your mouse hovers on it. Click "Edit". Under the "Authorization" tab, select "Basic Auth" and copy paste your **Tagging API key** into the "username" field. Leave the "password" field empty. Click "Update" to update your collection.

Now you are all set and it is time to use the sample.

## Upload Audio File

1. Click on "Upload Audio File" query under your collection. On the main panel, click on "Body" and select "form-data"
2. Input KEY as "audio" and press "Select Files" under VALUE to select an audio file to be uploaded
3. Press "**Send**" to send the request.

You will receive response at the bottom panel

## Upload YouTube Link

1. Click on "Upload YouTube Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR YOUTUBE LINK HERE"
   }
   ```

3. Press "**Send**" to send the request.

You will receive response at the bottom panel

## Upload Audio Link

1. Click on "Upload Audio Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR AUDIO LINK HERE"
   }
   ```
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

## Extract Tags

1. Click on "Extract Tags" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
       "id": "TRACK ID HERE",
       "tags": ["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]
   }
   ```
   You can add or remove tags from the array in the sample above to customize the tags you want to receive
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel
