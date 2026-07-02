from fastapi import FastAPI

from api.servicenow_connector_api import (
    router
)

app = FastAPI(

    title=
        "Connector Platform",

    version=
        "1.0.0"
)


@app.get("/")
def home():

    return {

        "message":
            "Connector Platform Running"
    }


app.include_router(
    router
)