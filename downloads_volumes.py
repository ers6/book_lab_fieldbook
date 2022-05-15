# turns a hathitrust metadata json file into a python dictionary so I can iterate thru all collection members
import requests
import json
import os

def main():
    infile_name = "chp_metadata.json"
    volume_ids = ""
    with open(infile_name) as json_file:
        metadata = json.load(json_file)['gathers']
    for volume in metadata: 
        the_argument = "htrc download -pg "+str(volume["htitem_id"])+"[2,3,4,5,6,7,8,9,10,11,12] -hfc -s -o workset/"+str(volume["htitem_id"])+"/"
        os.system(the_argument)
        

main()

