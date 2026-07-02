import os
import json
import requests

from utils.logger_config import logger

from services.payload_storage_service import (
    payload_storage_service
)

NORMALIZER_URL = os.getenv(
    "NORMALIZER_URL"
)


def process_servicenow(
        payload):

    payload[
        "source"
    ] = "servicenow"

    logger.info(
        "RAW PAYLOAD RECEIVED"
    )

    logger.info(
        json.dumps(
            payload,
            indent=4
        )
    )

    payload_storage_service.save_payload(
        payload
    )

    try:

        logger.info(
            "Calling centralized normalizer..."
        )

        logger.info(
            f"URL: {NORMALIZER_URL}"
        )

        response = requests.post(
            NORMALIZER_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        normalized = response.json()

        logger.info(
            "Normalizer response:"
        )

        logger.info(
            json.dumps(
                normalized,
                indent=4
            )
        )

    except Exception as ex:

        logger.error(
            f"Normalizer failed: {ex}"
        )

        normalized = {

            "status":
                "failed",

            "error":
                str(ex)
        }

    return {

        "status":
            "success",

        "raw_payload":
            payload,

        "normalized":
            normalized
    }