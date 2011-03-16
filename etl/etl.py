import argparse
import csv
import json
import re

MANUFACTURER = {
    "A": "American Home Food Products",
    "G": "General Mills",
    "K": "Kellogs",
    "N": "Nabisco",
    "P": "Post",
    "Q": "Quaker Oats",
    "R": "Ralston Purina",
    }

NORMAL_FIELDS = [
    "calories",
    "protein",
    "fat",
    "sodium",
    "dietary_fiber",
    "complex_carbohydrates",
    "sugars",
    "potassium",
    ]

# From http://djangosnippets.org/snippets/29/
def slugify(inStr):
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for","from","is", "in", "into", "like", "of", "off", "on", "onto","per","since", "than", "the", "this", "that", "to", "up", "via","with"];
    for a in removelist:
        aslug = re.sub(r'\b'+a+r'\b','',inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug

def manufacturer(abbr):
    """Given an abbriviation, return a dictionary"""
    if abbr == -1:
        return {"name": "Unknown"}
    else:
        return {"name":MANUFACTURER[abbr]}

def cereal(row):
    """Given a row of values, return a dictionary"""
    name = row[0].replace("_", " ")
    return {
        "name": name,
        "slug": slugify(name),
        "manufacturer": manufacturer(row[1]),
        "type": "hot" if row[2] == "H" else "cold",
        "calories": float(row[3]),
        "protein": float(row[4]),
        "fat": float(row[5]),
        "sodium": float(row[6]),
        "dietary_fiber": float(row[7]),
        "complex_carbohydrates": float(row[8]),
        "sugars": float(row[9]),
        "potassium": float(row[11]),
        "display_shelf": int(row[10]),
        "vitamins_minerals": int(row[12]),
        "serving_weight": float(row[13]),
        "cups_per_serving": float(row[14]),
        }

def norm(cereal):
    """
    Normal a cearl's data based to 1 cup
    """
    m = 1.0 / abs(cereal["cups_per_serving"])
    for k, v in cereal.iteritems():
        if k in NORMAL_FIELDS and v >= 0:
            cereal[k] = v * m
    cereal["cups_per_serving"] = 1
    return cereal

def main():
    parser = argparse.ArgumentParser(description="Turn the cereal csv file into usable json files")
    parser.add_argument("csvfile", type=str, help="The csv file to read")
    parser.add_argument("-n", "--normalize", default=False, action="store_true")
    args = parser.parse_args()
    cerealReader = csv.reader(open(args.csvfile), delimiter=" ")
    if args.normalize:
        cereals = [norm(cereal(c)) for c in cerealReader if c[0] is not -1]
    else:
        cereals = [cereal(c) for c in cerealReader if c[0] is not -1]
    print json.dumps(cereals, indent=4)

if __name__ == "__main__":
    main()
