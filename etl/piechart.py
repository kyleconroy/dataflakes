import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Calculate individual pie charts")
    parser.add_argument("input", type=str, help="Input json file")
    args = parser.parse_args()

    results = {}
    for k, c in json.load(open(args.input)).iteritems():
        results[c["slug"]] = [
            float(c["sugars"]),
            float(c["complex_carbohydrates"]),
            float(c["dietary_fiber"]),
            float(c["protein"]),
            float(c["fat"]),
            float(c["sodium"]) / 1000,
            float(c["potassium"]) / 1000,
            ]

    print json.dumps(results, indent=4)

if __name__ == "__main__":
    main()

import json
