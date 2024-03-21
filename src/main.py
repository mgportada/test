import os
import uvicorn
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
import routers

host = os.environ.get("host", "localhost")
port = int(os.environ.get("port", "8000"))


app = FastAPI()
app.include_router(routers.usuario)
app.include_router(routers.quiz)


@app.get("/", response_class=RedirectResponse, include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)
