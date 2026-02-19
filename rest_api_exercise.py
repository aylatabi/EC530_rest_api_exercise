import requests


r = requests.get("https://api.fda.gov/food/enforcement.json", params={
    "search": "report_date:[20040101 TO 20131231]",
    "limit": 1
})

data = r.json()
for result in data["results"]:
    print(result["country"])
    
