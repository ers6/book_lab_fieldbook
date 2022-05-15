# Documentation for HTRC Funding Data 

## Dependencies: 

Both programs must be run on a HTRC data capsule in "secure" mode. Files must be saved in the "secure_volume" on the VM to ensure they will not be lost
after you switch to maintenance. 
The program relies on the following libraries (all of which are included on the VM)- json, requests, os, and csv. 

## Workflow:

Navigate to the terminal in the data capsule. Be sure you are in the secure_volume folder before running anything. Then run downloads_volumes.py and scrapes_funding_data.py
This is what the shell script should look like: 
Cd /media 
Cd secure_volume
Python 3 downloads_volumes.py --
Python3 scrapes_funding_data.py 

## Limitations:

Note that downloads_volumes.py is only downloading the 58 volumes right now by iterating through their json metadata file. To download other volumes, use
a different HTRC collection. It also is only downloading the first 12 pages of the volumes right now. If funding info is not in these pages, it will not
be captured.

Note that scrapes_funding_data.py is currently scraping the 5 lines before, the line including, and the 20 lines after the string "copyright." If funding
information is not on the copyright page, it will not be captured. 


## Note:

"Funding Gentrification" is the write-up of the experiment. 
