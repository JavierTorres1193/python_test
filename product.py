import json

class Product:
    def __init__(self, averageRating: float, images:list, meetingPoint:str):
        self._averageRating = None
        self._images = None
        self._meetingPoint = None

        self.set_averageRating(averageRating)
        self.set_images(images)
        self.set_meetingPoint(meetingPoint)
    
    def set_averageRating(self, value:float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("average rating must be a positive number")
        self._averageRating = float(value)

    def set_images(self, value:list):
        if not all(isinstance(url,str) for url in value):
            raise ValueError("images must be a list of strings (URLs)")
        self._images = value

    def set_meetingPoint(self, value:str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("meetingPoint must be a non-empty string")
        self._meetingPoint = value.strip()


    def to_json(self):
        return json.dumps({
            "averageRating": self._averageRating,
            "images": self._images,
            "meetingPoint": self._meetingPoint
        }, indent=4)
    
