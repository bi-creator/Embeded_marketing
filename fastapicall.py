from fastapi import FastAPI
from serpapi import GoogleSearch
from compareimages import imagematching

app = FastAPI()


@app.get('/data')
def getdata(productname: str = ''):

    params = {
        "q": productname,
        "tbm": "shop",
        "location": "Dallas",
        "hl": "en",
        "gl": "us",
        "api_key": "b2bbaacdf95234778b4aeefe981e23d97e838b5a65cd47b48994a5a46070020"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    # distance = imagematching(testimage,imagecomp)
    # print(distance[0])
    return shopping_results
