import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Calculate individual pie charts")
    parser.add_argument("input", type=str, help="Input json file")
    args = parser.parse_args()

    results = {}
    for c in json.load(open(args.input)):
        results[c["slug"]] = [
            c["fat"],
            c["sugars"],
            c["sodium"] / 1000,
            c["potassium"] / 1000,
            c["dietary_fiber"],
            c["protein"],
            c["complex_carbohydrates"],
            ]

    print json.dumps(results, indent=4)

if __name__ == "__main__":
    main()
