from typing import List


class Category:
    id: int
    name: str

    def __init__(self, id: int) -> None:
        self.id = id
        self.name = "ACategory"


class PetRequest:
    id: int
    category: Category
    name: str
    photo_urls: List[str]
    tags: List[Category]
    status: str

    def __init__(self, id: int, category: Category) -> None:
        self.id = id
        self.category = category
        self.name = "Buster"
        self.photoUrls = ["www.url_to_photo.com"]
        self.tags = list()
        self.status = "Available"
