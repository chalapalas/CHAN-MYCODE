#!/usr/bin/env python3

# json is part of the standard library
import json

def main():
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    ## display our python data (a list containing two dictionaries)
    print(hitchhikers)

    ## Create the json string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print(jsonstring)

main()
