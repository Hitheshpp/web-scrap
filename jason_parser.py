import json
from collections import Counter

def count_products_per_website(json_file):
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)

        merchants = [product['merchant'] for product in data['productList']]

        merchant_counts = Counter(merchants)

        result = dict(merchant_counts)

        print(json.dumps(result, indent=4))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    json_file = 'data (1).json'
    count_products_per_website(json_file)
