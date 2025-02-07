from product import Product

def parseProduct(product_data):

    reviews = product_data.get("reviews", {}).get("reviewCountTotals", [])
    total_reviews = sum(review.get("count", 0) for review in reviews)
    if total_reviews > 0:
        averageRating = round(sum(review.get("rating", 0) * review.get("count", 0) for review in reviews) / total_reviews, 2)
    else:
        averageRating = 0.0


    images = []
    for image in product_data.get("images", []):
        largest_variant = max(image.get("variants", []), key=lambda x: x.get("width", 0))
        images.append(largest_variant.get("url"))

    description = product_data.get("description", "")
    meeting_point_start = description.find("Meeting point: ")
    if meeting_point_start != -1:
        meeting_point_end = description.find("\n\n", meeting_point_start)
        meetingPoint = description[meeting_point_start + len("Meeting point: "):meeting_point_end].strip().capitalize()
    else:
        meetingPoint = ""

    return Product(averageRating, images, meetingPoint)