from fastapi import FastAPI, File
from PIL import Image
import io
from serpapi import GoogleSearch
from compareimages import imagematching
import numpy
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)


@app.post('/uploadImage')
def uploadImage(file: bytes = File(...)):
    global image
    image = Image.open(io.BytesIO(file)).convert('RGB')

@app.post('/data')
def getdata(productname: str = ''):
    # image = Image.open(io.BytesIO(file)).convert('RGB')
    open_cv_image = numpy.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    params = {
        "q": productname,
        "tbm": "shop",
        "location": "Dallas",
        "hl": "en",
        "gl": "in",
        "api_key": "b2bbaacdf95234778b4aeefe981e23d97e838b5a65cd47b48994a5a46070020f"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]

    for i in shopping_results:
        i['distance'] = imagematching(open_cv_image, i['thumbnail'])
    shopping_results.sort(key=lambda x: x['distance'])
    newlist = sorted(shopping_results, key=lambda x: x['distance'])
    return newlist

