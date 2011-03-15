import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Calculate shelf values")
    parser.add_argument("input", type=str, help="Input json file")
    args = parser.parse_args()
    cereals = json.load(open(args.input))

    categories = [
        "count",
        "calories",
        "protein",
        "fat",
        "sodium",
        "dietary_fiber",
        "complex_carbohydrates",
        "sugars",
        "potassium",
        ]
    results = dict((c, [0, 0, 0]) for c in categories)

    # Count it up
    for cereal in cereals:
        n = cereal["display_shelf"] - 1
        for cat in categories:
            if cat == "count":
                results[cat][n] += 1
            else:
                results[cat][n] += cereal[cat]

    # Average
    for k, v in results.iteritems():
        if k is not "count":
            for i, l in enumerate(v):
                results[k][i] = v[i] / results["count"][i]


    results = [ v for v in results.itervalues() ]

    print json.dumps(results)

if __name__ == "__main__":
    main()
