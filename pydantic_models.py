from pydantic import BaseModel

class Item(BaseModel):
    name:str
    alt_names:list[str]
    description:str
    short_description:str
    sellers:list[str]
    price:float
    rating:float
    tags:list[str]
    types:list[str]
    image_path:str
    alt_image_paths:list[str]
    item_folder:str