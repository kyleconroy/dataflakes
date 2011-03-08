""" Utilities for calculating stats about cereals """

def rdi(cereal):
    """ Based off a 2,000 c diet """
    m = 2.0 / float(cereal["cups_per_serving"])
    if m <= 0:
        m = 1

    result = [
        {"name":"Fat", "amount": m * float(cereal["fat"]),
         "rdi": 65},
        {"name":"Sodium", "amount": m * float(cereal["sodium"]),
         "rdi": 2300},
        {"name":"Potassium", "amount": m * float(cereal["potassium"]),
         "rdi": 4700},
        {"name":"Fiber", "amount": m * float(cereal["dietary_fiber"]),
         "rdi": 25},
        {"name":"Calories", "amount": m * float(cereal["calories"]),
         "rdi": 2000},
        {"name":"Protein", "amount": m * float(cereal["protein"]),
         "rdi": 50},
        {"name":"Carbohydrates", "amount": m * (float(cereal["complex_carbohydrates"]) + float(cereal["sugars"])),
         "rdi": 300},
        ]

    return [k for k in result if k["amount"] >= 0]


