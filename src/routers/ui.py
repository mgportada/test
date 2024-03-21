from fastapi import APIRouter

from fastapi.responses import HTMLResponse, FileResponse

router = APIRouter(tags=["UI"])


@router.get("/ui/home", response_class=HTMLResponse)
async def show_home():
    htmldireccion = "./html/juego.html"
    return FileResponse(htmldireccion)
