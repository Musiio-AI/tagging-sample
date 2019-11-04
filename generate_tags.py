import os
import json
import codecs
import requests
import argparse
import time

from pathlib import Path
from tenacity import retry, stop_after_attempt, wait_exponential
from multiprocessing import Lock
from multiprocessing.pool import ThreadPool
from functools import partial
from constants import TAGS, KEY, TAG_URL, UPLOAD_URL


class Tagger():

    def __init__(self):
        self.__completed = 0
        self.__mutex = Lock()

    def __checkTagSelection(self, tag_selection):
        """
        Check whether the tags provided by the user are valid Musiio tags
        :param tag_selection: list - A list containing the type of tags to tag the track for
        :return: tag_selection: list - A list containing the type of tags to tag the track for
        """

        tag_selection = list(map(lambda x: x.upper(), tag_selection))

        for tag in tag_selection:

            if tag not in TAGS:
                e = 'ERROR: "{}" is not a valid tag type'.format(tag)
                print(e)
                return ValueError(e)

        return tag_selection


    def __listFiles(self, source_path):
        """
        Recursively check the provided path for audio tracks and return it in a list
        :param source_path: string - The path where audio tracks are stored
        :return: files: list - A list containing the paths to each audio track
        """

        files = []
        for r, d, f in os.walk(source_path):
            for file_name in f:
                if '.m4a' in file_name or '.mp3' in file_name or '.wav' in file_name:
                    files.append(os.path.join(r, file_name))

        if len(files) == 0:
            e = "ERROR: No '.mp3', '.wav', or '.m4a' files found in the provided source folder"
            print(e)
            return ValueError(e)

        return files


    @retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=2, min=4, max=60))
    def __uploadFile(self, file_name, api_key=None):
        """
        Makes a POST request to upload the given audio track
        :param file_name: string - The path where the audio track is stored
        :param api_key: str - Your API key provided by Musiio
        :return: feature_id: string - A unique ID for this audio track
        """

        data = open(file_name, 'rb')
        url = UPLOAD_URL

        response = requests.post(url, files={"audio": data}, auth=(api_key, ""))

        json_data = response.json()
        feature_id = json_data["id"]
        return feature_id


    @retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=2, min=4, max=60))
    def __tagFile(self, feature_id, tag_selection, api_key=None):
        """
        Makes a POST request to tag the given audio track
        :param feature_id: string - A unique ID for this audio track
        :param tag_selection: list - A list containing the type of tags to tag the track for
        :param api_key: str - Your API key provided by Musiio
        :return: tags: list - A list of tags for this audio track
        """

        url = TAG_URL
        data = {
            "id": feature_id,
            "tags": tag_selection
        }
        response = requests.post(url, json=data, auth=(api_key, ""))

        json_data = response.json()
        tags = json_data["tags"]
        return tags


    def __processFile(self, destination_path, tag_selection, gui, api_key, file_name):
        """
         Uploads the given audio track, tags it, and saves the tags in a json file located in the destination path
         :param destination_path: string - The path where tag json files are saved
         :param tag_selection: list - A list containing the type of tags to tag the track for
         :param gui: boolean - Whether the GUI is being used
         :param api_key: str - Your API key provided by Musiio
         :param file_name: string - The path where the audio track is stored
         :return: 1 if successful, 0 if unsuccessful
         """

        feature_id = self.__uploadFile(file_name, api_key)

        if feature_id:
            features = self.__tagFile(feature_id, tag_selection, api_key)
            file_type = file_name.split(".")[-1]
            out_file = file_name.replace(file_type, "json")
            out_file = out_file.split(os.sep)[-1]
            out_path = os.path.join(destination_path, out_file)

            with codecs.open(out_path, "w", "utf-8") as file:
                file.write(json.dumps(features))

            if gui:

                self.__mutex.acquire()
                self.__completed += 1
                self.__mutex.release()

            return 1

        return 0


    def __tagFiles(self, file_list, destination_path, tag_selection, gui=False, api_key=None):
        """
         Creates a ThreadPool to tag the given list of audio tracks
         :param file_list: list - A list containing the paths to each audio track
         :param destination_path: string - The path where tag json files are saved
         :param tag_selection: list - A list containing the type of tags to tag the track for
         :param gui: boolean - Whether the GUI is being used
         :param api_key: str - Your API key provided by Musiio
         """

        with ThreadPool(5) as pool:
            process = partial(self.__processFile, destination_path, tag_selection, gui, api_key)
            _ = pool.map(process, file_list)



    def __updateProgressBar(self, progress, progress_str, file_list):
        """
         Updates the progress bar. Only applicable if GUI is used
         :param progress: tkinter Progressbar type object
         :param progress_str: string - Progressbar text
         :param file_list: list - A list containing the paths to each audio track
         :param api_key: str - Your API key provided by Musiio
         """
        t = 0

        while progress["value"] != 100:
            progress["value"] = self.__completed / len(file_list) * 100
            progress.update()
            progress_str.set('In Progress' + (t * '.'))

            t += 1
            if t == 4:
                t = 0

            time.sleep(0.5)


    def tagFilesTask(self, source_path, destination_path, tag_selection=None, progress=None, progress_str=None, api_key=None):
        """
        Tag tracks in source folder and save the tags in the destination folder
        :param source_path: string - The path where tracks are stored
        :param destination_path: string - The path where tag json files are saved
        :param tag_selection: list - A list containing the type of tags to tag the track for
        :param progress: tkinter Progressbar type object. Only used in GUI
        :param progress_str: string - Progressbar text. Only used in GUI
        :param api_key: str - Your API key provided by Musiio
        """

        # Check if destination path is valid
        if not os.path.isdir(destination_path):
            e = "ERROR: '{}' is not a valid path".format(destination_path)
            print(e)
            return ValueError(e)

        # Check and list files in source path recursively
        target_path = Path(source_path)
        files = self.__listFiles(target_path)

        if type(files) == ValueError:
            return ValueError(files)

        # Using GUI
        if progress and progress_str:

            progress['value'] = 0
            with ThreadPool(2) as pool:
                pool.apply_async(self.__tagFiles, (files, destination_path, tag_selection, True, api_key))
                pool.apply_async(self.__updateProgressBar(progress, progress_str, files))

            progress_str.set('')

        # Using cmd line arguments
        else:
            api_key = KEY
            tag_selection = self.__checkTagSelection(tag_selection)
            if type(tag_selection) == ValueError:
                return ValueError(tag_selection)

            self.__tagFiles(files, destination_path, tag_selection, False, api_key)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Sort Tags')

    parser.add_argument('--source-path', dest='source_path',
                        help='The path to the folder containing tracks to be tagged')

    parser.add_argument('--destination-path', dest='destination_path',
                        help='The path where json tag files will be saved')

    parser.add_argument('--tag-selection', nargs='+', dest='tag_selection', default=TAGS,
                        help='The type of tags to tag each audio file for')

    args = parser.parse_args()

    tagger = Tagger()

    tagger.tagFilesTask(source_path=args.source_path, destination_path=args.destination_path, tag_selection=args.tag_selection)
