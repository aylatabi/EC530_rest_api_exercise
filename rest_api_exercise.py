import requests

BASE_URL = "https://api.fda.gov/food/event.json"

def get_food_events(industry, limit=5):
    payload = {
        "search": f"products.industry_name:{industry}",
        "limit": limit
    }
    r = requests.get(BASE_URL, params=payload)
    if r.status_code != 200:
        print(f"Error: {r.status_code}")
        print(r.json())
        return None
    return r.json()

def print_reactions(data):
    for result in data["results"]:
        print("Reactions:")
        for reaction in result.get("reactions", []):
            print(f"  - {reaction}")
        print("---")

def print_products(data):
    for result in data["results"]:
        for product in result.get("products", []):
            print(product.get("name_brand", "Unknown brand"))
        print("---")

def list_industries():
    payload = {
        "count": "products.industry_name.exact"
    }
    r = requests.get(BASE_URL, params=payload)
    if r.status_code != 200:
        print(f"Error: {r.status_code}")
        return
    for result in r.json()["results"]:
        print(result["term"], "-", result["count"])

def main():
    print("Available industries:")
    list_industries()
    print()

    industry = input("Enter a product industry: ")
    data = get_food_events(industry, limit=5)

    if data and "results" in data:
        print_reactions(data)
        print_products(data)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()