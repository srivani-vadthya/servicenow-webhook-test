import datetime
import json
import requests
import os

from utils.logger_config import (
    logger
)

from services.payload_storage_service import (
    payload_storage_service
)

NORMALIZER_URL = os.getenv(
    "NORMALIZER_URL"
)

def process_servicenow(
        payload):

    # identify source
    payload[
        "source"
    ] = "servicenow"

    # store raw payload
    payload_storage_service.save_payload(
        payload
    )

    # call centralized normalizer
    try:

        response = requests.post(
            NORMALIZER_URL,
            json=payload,
            timeout=30
        )

        normalized = response.json()

    except Exception as ex:

        logger.error(
                f"Normalizer error: {ex}"
        )

        normalized = {

        "status":
            "failed",

        "error":
            str(ex)
        }