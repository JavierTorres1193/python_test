from product import Product

def main():
    product = Product(
        averageRating=2.1,
        images=[
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg",
        ],
        meetingPoint="Hotel Lobby"
    )

    print(product.to_json())

if __name__ == "__main__":
    main()