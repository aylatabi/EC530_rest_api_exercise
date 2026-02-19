import requests

r = requests.get("https://api.fda.gov/food/event.json", params={
    "count": "products.industry_name.exact"
})

data = r.json()

for result in data["results"]:
    print(result["term"])