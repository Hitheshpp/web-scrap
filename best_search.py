import requests
from bs4 import BeautifulSoup
import json

def get_brand_positions(keyword, brands, site_url):
    search_url = f"{site_url}/ps/?q={keyword.replace(' ', '+')}"
    response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return {"error": f"Failed to fetch data for keyword '{keyword}'"}
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    products = soup.select("#siteLayout ul > li > div")
    positions = {brand.lower(): None for brand in brands}
    
    for index, product in enumerate(products[:100], start=1):
        product_name = product.select_one("h3 > a > span")  
        if product_name:
            product_text = product_name.text.lower()
            
            for brand in brands:
                if brand.lower() in product_text and positions[brand.lower()] is None:
                    positions[brand.lower()] = index
    
    return {"Keyword": keyword, "Position": positions}


def main():
    # Input
    keywords = ["hair fall shampoo", "conditioner", "shampoo","Anti-Dandruff"]
    brands = ["L'Oreal Paris", "Dove", "Tresemme"]
    site_url = "https://www.bigbasket.com"
    
    results = []
    for keyword in keywords:
        result = get_brand_positions(keyword, brands, site_url)
        results.append(result)
    
    # Output
    output = {"Result": results}
    with open("brand_positions.json", "w") as json_file:
        json.dump(output, json_file, indent=4)
    print(json.dumps(output, indent=4))

if __name__ == "__main__":
    main()
