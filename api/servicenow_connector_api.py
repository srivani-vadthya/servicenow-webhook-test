from fastapi import APIRouter

from models.servicenow_request_model import (
    ServiceNowRequestModel
)

from connectors.servicenow_connector import (
    process_servicenow
)

from services.payload_storage_service import (
    payload_storage_service
)

router = APIRouter()


# ===================================
# Receive ServiceNow Incident
# ===================================
@router.post(
    "/servicenow"
)
def servicenow_connector(
        payload:
        ServiceNowRequestModel):

    return process_servicenow(
        payload.model_dump()
    )


# ===================================
# Latest Payload
# ===================================
@router.get(
    "/latest"
)
def latest_payload():

    payload = (
        payload_storage_service
        .get_latest_payload()
    )

    if payload is None:

        return {

            "message":
                "No payloads received"
        }

    return payload


# ===================================
# All Payloads
# ===================================
@router.get(
    "/payloads"
)
def payloads():

    return {

        "count":
            payload_storage_service
            .get_count(),

        "payloads":
            payload_storage_service
            .get_all_payloads()
    }