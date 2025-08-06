from fastapi import APIRouter
import requests
from config import settings
from urllib.parse import urljoin



router = APIRouter()

@router.post("/massive_insert")
def massive_insert(channelName : list[str]):
    res=[]
    url=urljoin(settings.BASE_URL,settings.URL_RETRIEVE_YOUTUBE_CHANNEL)
    for item in channelName:
        params={"name":item}
        res.append(requests.get(url,params))
    return res