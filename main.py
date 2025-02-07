# main.py
from parser import parseProduct
import json

def main():
    try:
        with open('product_data.json', 'r') as f:
            data = json.load(f)
            products = data.get("products", [])

            if not products:
                print("No products found in the JSON file")
                return

            for product in products:
                status = product.get("status")
                if status == "ACTIVE":
                    parsed_product = parseProduct(product)
                    print(parsed_product.to_json())
    
    except FileNotFoundError:
        print("El archivo 'product_data.json' no se encuentra.")
    except json.JSONDecodeError:
        print("Hubo un error al parsear el archivo JSON.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()