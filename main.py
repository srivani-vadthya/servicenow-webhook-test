from fastapi import FastAPI
from models.servicenow_request import ServiceNowRequest
from connectors.servicenow_connector import process_servicenow

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "AI Connector Platform Running"
    }


@app.post("/servicenow")
async def servicenow_connector(
        payload: ServiceNowRequest):

    print("\n")
    print("================================")
    print("SERVICENOW INCIDENT RECEIVED")
    print("================================")
    print(payload)

    # Normalize
    normalized = process_servicenow(
        payload.model_dump()
    )

    print("\n")
    print("NORMALIZED INCIDENT")
    print(normalized.model_dump())

    # Temporary mock categorization
    categorization = {
        "category": "L1",
        "team": "Infrastructure"
    }

    print("\n")
    print("CATEGORIZATION")
    print(categorization)

    return {
        "status": "success",
        "normalized":
            normalized.model_dump(),
        "categorization":
            categorization
    }