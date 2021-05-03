# -*- coding: utf-8 -*-
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", include_in_schema=False, response_class=HTMLResponse)
async def index(request: Request):
    """
    Home page view.
    """
    data = {"request": request}
    return templates.TemplateResponse("/index.html", data)


# May move this to template. You'll want to place to place this:
# <link rel="icon" type="image/png \
# href="{{ url_for('static', path="/static/img/favicon.ico") }}"
# We'll do this after Tailwind implementation.
@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    """
    favicon view.
    """
    return RedirectResponse(url="/static/img/favicon.ico")
