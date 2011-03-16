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

    count = [
        "calories",
        "count",
        ]


    mgrams = [
        "sodium",
        "potassium",
        ]

    grams = [
        "protein",
        "fat",
        "dietary_fiber",
        "complex_carbohydrates",
        "sugars",
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


    output = {
        "grams":{
            "data":[],
            "yaxis":[],
            },
        "mgrams":{
            "data":[],
            "yaxis":[],
            },
        "count":{
            "data":[],
            "yaxis":[],
            },
        }

    for k, v in results.iteritems():
        title = k.replace("_", " ").title()
        if k in grams:
            o = output["grams"]
        elif k in mgrams:
            o = output["mgrams"]
        else:
            o = output["count"]
        o["data"].append(v)
        o["yaxis"].append(title)


    print json.dumps(output, indent=4)

if __name__ == "__main__":
    main()
