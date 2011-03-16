import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Calculate shelf values")
    parser.add_argument("input", type=str, help="Input json file")
    args = parser.parse_args()

    names = set()

    # Create name set
    for cereal in json.load(open(args.input)):
        for w in cereal["slug"].split("-"):
            names.add(w)

    results = dict((n, {"count":0, "calories":0, "sugars":0}) for n in names)

    # Fill up Results
    for cereal in json.load(open(args.input)):
        for w in cereal["slug"].split("-"):
            results[w]["count"] += 1
            results[w]["sugars"] += cereal["sugars"]
            results[w]["calories"] += cereal["calories"]

    def norm(k, v):
        return {
            "x": v["sugars"] / v["count"],
            "y": v["calories"] / v["count"],
            "z": v["count"],
            "h": k.title(),
            }

    # Filter and nomalize
    results = [ norm(k, v) for k, v in results.iteritems() if v["count"] >= 2]

    print json.dumps(results, indent=4)

if __name__ == "__main__":
    main()
