import json
def task() -> float:
    with open('input.json') as file:
        data = json.load(file)
    sum_product = sum([item["score"] * item["weight"] for item in data])
    sum_product = round(sum_product, 3)
    return sum_product
print(task())
