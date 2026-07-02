import datetime
import json

from utils.logger_config import (
    logger
)

from services.payload_storage_service import (
    payload_storage_service
)


def process_servicenow(
        payload: dict):

    logger.info("")
    logger.info(
        "=" * 60
    )

    logger.info(
        "SERVICENOW CONNECTOR TRIGGERED"
    )

    logger.info(
        "=" * 60
    )

    logger.info(
        f"Timestamp: "
        f"{datetime.datetime.now()}"
    )

    payload["source"] = (
        "servicenow"
    )

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

    logger.info(
        f"Payload Count: "
        f"{payload_storage_service.get_count()}"
    )

    logger.info(
        "=" * 60
    )

    return {

        "status":
            "success",

        "message":
            "Payload stored successfully",

        "payload_count":
            payload_storage_service.get_count()
    }