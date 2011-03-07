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

def manufacturer(abbr):
    """Given an abbriviation, return a dictionary"""
    if abbr == -1:
        return {"name": "Unknown"}
    else:
        return {"name":MANUFACTURER[abbr]}


def slugify(inStr):
    removelist = ["a", "an", "as", "at", "before", "but", "by", "for","from","is", "in", "into", "like", "of", "off", "on", "onto","per","since", "than", "the", "this", "that", "to", "up", "via","with"];
    for a in removelist:
        aslug = re.sub(r'\b'+a+r'\b','',inStr)
    aslug = re.sub('[^\w\s-]', '', aslug).strip().lower()
    aslug = re.sub('\s+', '-', aslug)
    return aslug

def cereal(row):
    """Given a row of values, return a dictionary"""
    name = row[0].replace("_", " ")
    return {
        "name": name,
        "slug": slugify(name),
        "manufacturer": manufacturer(row[1]),
        "type": "hot" if row[2] == "H" else "cold",
        "calories": { "amount": row[3], "unit": "grams" },
        "protein": { "amount": row[4], "unit": "grams" },
        "fat": { "amount": row[5], "unit": "grams" },
        "sodium": { "amount": row[6], "unit": "milligrams" },
        "dietary_fiber": {"amount": row[7], "unit": "grams"},
        "complex_carbohydrates": {"amount": row[8], "unit": "grams"},
        "sugars": {"amount": row[9], "unit": "grams"},
        "display_shelf": row[10],
        "potassium": {"amount": row[11], "unit": "milligrams"},
        "vitamins_minerals": row[12],
        "serving_weight": {"amount": row[13], "unit": "ounces"},
        "cups_per_serving": row[14],
        }

def main():
    parser = argparse.ArgumentParser(description="Turn the cereal csv file into usable json files")
    parser.add_argument("csvfile", type=str, help="The csv file to read")
    args = parser.parse_args()
    cerealReader = csv.reader(open(args.csvfile), delimiter=" ")
    cereals = dict( (cereal(c)["slug"], cereal(c)) for c in cerealReader if c[0] is not -1)
    print json.dumps(cereals, indent=4)

if __name__ == "__main__":
    main()
