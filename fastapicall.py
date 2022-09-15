from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from serpapi import GoogleSearch
from compareimages import imagematching
import numpy

app = FastAPI()


# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     image = Image.open(io.BytesIO(file)).convert('RGB')
#     open_cv_image = numpy.array(image)
#     open_cv_image = open_cv_image[:, :, ::-1].copy()
#     a = imagematching(open_cv_image)
#     return float(a)


@app.post('/data')
def getdata(productname: str = '', file: bytes = File(...)):
    image = Image.open(io.BytesIO(file)).convert('RGB')
    open_cv_image = numpy.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    params = {
        "q": productname,
        "tbm": "shop",
        "location": "Dallas",
        "hl": "en",
        "gl": "us",
        "api_key": "b2bbaacdf95234778b4aeefe981e23d97e838b5a65cd47b48994a5a46070020f"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    for i in shopping_results:
        i['distance'] = imagematching(open_cv_image, i['thumbnail'])
    return shopping_results
