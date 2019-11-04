import os
import csv
import json
import argparse
from constants import VALID_TAGS

def getTagsInFolder(tags_path):
    """
    Check the provided folder for json files and return it in a list
    :param tags_path: string - The path where tag jsons are stored
    :return: tags: list - A list containing the paths to each tag json
    """

    if not os.path.isdir(tags_path):
        e = 'ERROR: The system cannot find the path specified: {}'.format(tags_path)
        print(e)
        return ValueError(e)

    tags = list()

    for file in os.listdir(tags_path):
        if file[-5:] == ".json":
            tags.append(file)

    if len(tags) == 0:
        e = 'ERROR: No tags found in the provided folder'
        print(e)
        return ValueError(e)

    return tags

def checkValidTags(tags_types):
    """
    Check if the tag types provided by the user are valid Musiio tags
    :param tags_types: string - The tag types to extract from each tag json file
    """

    tags_types = list(map(lambda x: x.upper(), tags_types))

    if len(tags_types) == 0:
        e = 'ERROR: No Tags Provided'
        print(e)
        return ValueError(e)

    for tag in tags_types:
        if tag not in VALID_TAGS:
            e = 'ERROR: "{}" is not a valid tag name'.format(tag)
            print(e)
            return ValueError(e)

    return tags_types

def createHeader(tags_types):
    """
    Creates the text for the headers in the first row of the CSV file
    :param tags_types: string - The tag types to extract from each tag json file
    """

    tags_types_len = len(tags_types)

    for i in range(tags_types_len):
        tags_types.insert((i*2) + 1, "SCORE")

    tags_types.insert(0, "TRACK TITLE")

def checkInstruments(tags_types):
    """
    Modifies the header accordingly if instrument tags are required
    :param tags_types: string - The tag types to extract from each tag json file
    """
    if "INSTRUMENT" in tags_types:
        instrument_index = tags_types.index("INSTRUMENT") + 2

        for i in range(6):
            tags_types.insert(instrument_index, "INSTRUMENT")
            tags_types.insert(instrument_index + 1, "SCORE")

def checkTags(csv_writer, tags_path, file, tags_types, tags_list):
    """
    Opens a given json file, checks through the given tag types, and writes it to the CSV file
    :param csv_writer: csv file
    :param tags_path: string - The path where tag jsons are stored
    :param file: string - The path to the tag json file
    :param tags_types: string - The tag types to extract from each tag json file
    :param tags_list: list - A list where tag values are written to and then subsequently written to the CSV
    """

    with open(tags_path + '/' + file, 'r') as t:

        tags = json.load(t)
        instrument = 0

        # iterate through this tag file
        for tag in tags:

            type = tag['type']
            score = tag['score']
            name = tag['name']

            try:
                index = tags_types.index(type)
            except:
                continue

            if type == "INSTRUMENT":
                index = index + instrument
                instrument += 2

            index_score = index + 1
            tags_list[index] = name
            tags_list[index_score] = score

        csv_writer.writerow(tags_list)


def sortTags(tags_path, tags_csv, tags_types, progress=None):
    """
    Generate a CSV file of all the tags located in the provided folder
    :param tags_path: string - The path where tag jsons are stored
    :param tags_csv: string - The path where csv file will be saved
    :param tags_types: string - The tag types to extract from each tag json file
    :param progress: tkinter Progressbar type object. Only used in GUI
    """

    # check if tag names provided by the user are valid
    tags_types = checkValidTags(tags_types)
    if type(tags_types) == ValueError:
        return ValueError(tags_types)

    # create first row headers for csv file
    createHeader(tags_types)
    checkInstruments(tags_types)

    # get all valid tag json files from the path provided
    tags = getTagsInFolder(tags_path)
    if type(tags) == ValueError:
        return ValueError(tags)

    tags_csv = os.path.join(tags_csv, 'tags.csv')

    # initialise progress bar if using GUI
    if progress:
        progress['maximum'] = 100
        progress['value'] = 0

    with open(tags_csv, 'w', newline='') as csv_file:

        # creates headers
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(tags_types)

        # iterate through tags in the folder
        for file in tags:

            tags_list = list()

            for each in range(len(tags_types)):
                tags_list.append("")

            track = file[:-5]
            tags_list[0] = track

            checkTags(csv_writer, tags_path, file, tags_types, tags_list)

            # update progress bar if using GUI
            if progress:
                progress["value"] += (1 / len(tags)) * 100
                progress.update()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate CSV File Containing Tags')

    parser.add_argument('--tags-path', dest='tags_path',
                        help='The path to the folder containing tags')

    parser.add_argument('--tags-csv', dest='tags_csv',
                        help='The path to where csv file will be written')

    parser.add_argument('--tags-types', nargs='+', dest='tags_types',
                        help='The type of tags to extract from each file')

    args = parser.parse_args()

    sortTags(tags_path=args.tags_path, tags_csv=args.tags_csv, tags_types=args.tags_types)