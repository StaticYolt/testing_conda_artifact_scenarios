import argparse
import os
import json

bdict = {"csx": {"info1": "value1", "info2": "value2"},
         "srx": {"info1": "value1", "info2": "value2"},
         }
def main():
    curr_bdict = {}

    parser = argparse.ArgumentParser(description='Parses Json and passes arguments to download-artifacts-sh')
    parser.add_argument("-b", "--beamline_acronym", help="Example csx")
    args = parser.parse_args()


    curr_bdict = bdict.get(args.beamline_acronym, {})
    if curr_bdict:
        print(curr_bdict)
if __name__ == "__main__":
    main()





    # match args.beamline_acronym:
    #     case "csx":
    #         curr_bdict = bdict.get("csx")
    #     case "srx":
    #         pass
    #         curr_bdict = bdict.get("srx")
    #     case _:
    #         pass
