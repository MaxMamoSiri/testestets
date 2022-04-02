import argparse
import os
import functions
global artist 

artist = functions.loadCSV()
## List of dictionaries ! 
print(functions.search('Romare Bearde', artist))