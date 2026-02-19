import requests

def get_food_events(industry, limit=5):
    r = requests.get("https://api.fda.gov/food/event.json", params={
        "search": f"products.industry_name:{industry}",
        "limit": limit
    })
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

def main():
    industry = input("Enter a product industry (e.g. Vitamins, Dairy): ")
    data = get_food_events(industry, limit=5)

    if "results" in data:
        print_reactions(data)
        print_products(data)
    else:
        print("No results found or bad request.")
        print(data)

if __name__ == "__main__":
    main()