from fastapi import FastAPI, Depends
from .schemas import TreeCountRequest
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base, RequestLog
import requests
import json

app = FastAPI()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tree_count/")
async def tree_count(request: TreeCountRequest,
                     db: Session = Depends(get_db)):
    url = r"http://overpass-api.de/api/interpreter"
    mydata = f'''[out:json][date:'{request.year}-01-01T00:00:00Z'][maxsize:2000000000];
    area["name"="{request.city}"]->.searchArea;(node["natural"="tree"](area.searchArea);); out count;'''
    x = requests.post(url, data=mydata)
    data = json.loads(x.text)
    trees = data['elements'][0]['tags']['total']
    new_city = RequestLog(
        city=request.city,
        country=request.country,
        year=request.year,
        trees=trees
    )
    db.add(new_city)
    db.commit()
    return {"city": request.city, "country": request.country, "year": request.year, "tree_count": trees}
