from fastapi import APIRouter
import requests
from config import settings
from urllib.parse import urljoin
from fastapi.responses import JSONResponse



router = APIRouter()

@router.post("/massive_insert")
def massive_insert(channelName : list[str]):
    res=[]

    try:
        url_retrieve_youtube_channel=urljoin(settings.BASE_URL_LOCAL if settings.LOCAL else settings.BASE_URL,settings.URL_RETRIEVE_YOUTUBE_CHANNEL)
        for item in channelName:
            params={"name":item }
            r=requests.get(url_retrieve_youtube_channel,params)
            res.append(r.content)
        return {"message": res}
    except Exception as e:
        return JSONResponse(e)