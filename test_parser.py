import unittest
from product import Product
from parser import parseProduct

class TestParseProduct(unittest.TestCase):
    
    def test_parse_product_with_valid_data(self):
        product_data = {
            "reviews": {
                "reviewCountTotals": [
                    {"rating": 5, "count": 2},
                    {"rating": 4, "count": 3}
                ]
            },
            "images": [
                {"variants": [
                    {"width": 200, "url": "image1_small.jpg"},
                    {"width": 800, "url": "image1_large.jpg"}
                ]},
                {"variants": [
                    {"width": 300, "url": "image2_small.jpg"},
                    {"width": 900, "url": "image2_large.jpg"}
                ]}
            ],
            "description": "This is a test description. Meeting point: Test Location\n\nMore details."
        }
        parsed_product = parseProduct(product_data)
        
        self.assertIsInstance(parsed_product, Product)
        self.assertEqual(parsed_product._averageRating, 4.4)
        self.assertEqual(parsed_product._images, ["image1_large.jpg", "image2_large.jpg"])
        self.assertEqual(parsed_product._meetingPoint, "Test location")
    
    def test_parse_product_with_no_reviews(self):
        product_data = {
            "reviews": {"reviewCountTotals": []},
            "images": [],
            "description": "No meeting point here."
        }
        parsed_product = parseProduct(product_data)
        
        self.assertEqual(parsed_product._averageRating, 0.0)
        self.assertEqual(parsed_product._images, [])
        self.assertEqual(parsed_product._meetingPoint, "")
    
    def test_parse_product_with_no_images(self):
        product_data = {
            "reviews": {"reviewCountTotals": [{"rating": 3, "count": 1}]},
            "images": [],
            "description": "Meeting point: Another Place\n\nSome details."
        }
        parsed_product = parseProduct(product_data)
        
        self.assertEqual(parsed_product._images, [])
        self.assertEqual(parsed_product._meetingPoint, "Another place")
    
    def test_parse_product_with_no_meeting_point(self):
        product_data = {
            "reviews": {"reviewCountTotals": [{"rating": 5, "count": 1}]},
            "images": [{"variants": [{"width": 500, "url": "image_large.jpg"}]}],
            "description": "No specific meeting point mentioned."
        }
        parsed_product = parseProduct(product_data)
        
        self.assertEqual(parsed_product._meetingPoint, "")
    
if __name__ == "__main__":
    unittest.main()