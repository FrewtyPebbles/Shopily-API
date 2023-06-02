from fastapi import FastAPI, UploadFile, Form, File
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from os import getenv, listdir, mkdir
import os
from pydantic_models import Item


load_dotenv()
if not os.path.exists(getenv("ITEM_FOLDER")):
   mkdir(getenv("ITEM_FOLDER"))

VER = "0.1.0"
app = FastAPI()
app.mount("/static", StaticFiles(directory=getenv("ITEM_FOLDER")), name="static")



mongo_client = AsyncIOMotorClient(getenv("DB_HOST"))
db = mongo_client[getenv("DB_NAME")]


@app.get("/")
async def root():
    return {"message": f"Shopily API v{VER}"}

@app.post("/item")
async def add_item(
                    name:str = Form(...),
                    alt_names:list[str] = Form(...),
                    description:str = Form(...),
                    short_description:str = Form(...),
                    sellers:list[str] = Form(...),
                    price:float = Form(...),
                    rating:float = Form(...),
                    tags:list[str] = Form(...),
                    types:list[str] = Form(...),
                    main_img: UploadFile = File(...),
                    alt_imgs: list[UploadFile] = File(...)):
    item = Item(
        name=name,
        alt_names=alt_names,
        description=description,
        short_description=short_description,
        sellers=sellers,
        price=price,
        rating=rating,
        tags=tags,
        types=types,
        image_path="",
        alt_image_paths=[],
        item_folder=""
    )
    edited_item = item.dict()
    parent_dir = f"{edited_item['name']}{len(listdir(getenv('ITEM_FOLDER')))}"
    edited_item["item_folder"] = parent_dir
    mkdir(f"{getenv('ITEM_FOLDER')}/{parent_dir}")
    mkdir(f"{getenv('ITEM_FOLDER')}/{parent_dir}/main")
    image_path = f"{getenv('ITEM_FOLDER')}/{parent_dir}/main/{main_img.filename}"
    edited_item["image_path"] = image_path
    with open(image_path, "wb") as f_obj2:
        f_obj2.write(main_img.file.read())

    for file in alt_imgs:
        alt_img_path = f"{getenv('ITEM_FOLDER')}/{parent_dir}/{file.filename}"
        edited_item["alt_image_paths"].append(alt_img_path)
        with open(alt_img_path, "wb") as f_obj2:
            f_obj2.write(file.file.read())
    #make query.
    result = await db.item.insert_one(edited_item)
    return {"id": str(result.inserted_id)}