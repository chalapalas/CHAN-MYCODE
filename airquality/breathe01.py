#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

LOOKUPAPI = 'http://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=85383&date=2019-01-24&distance=25&API_KEY=F87E3C94-4EFA-4329-9EC9-6BF5E63E7B13' #Replace me with AirNow's Generated URL

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)

    # display the methods available to our new object
    print( dir(r) )

main()
