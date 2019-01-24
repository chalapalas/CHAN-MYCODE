#!/usr/bin/env python3

# yaml is part of the standard library
import yaml

def main():
    ## Open a blob of YAML data
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")

    ## convert YAML into python data structures (lists and dictionaries)
    pyyammy = yaml.load(yammyfile)

    # display our new python data
    print(pyyammy)

main()
