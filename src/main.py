import uvicorn
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/templates")


async def homepage(request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "version": "0.0.1"}
    )


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
        Mount("/static", app=StaticFiles(directory="src/static"), name="static"),
    ],
)

if __name__ == "__main__":
    uvicorn.run("src.main:app")  # pragma: no cover
