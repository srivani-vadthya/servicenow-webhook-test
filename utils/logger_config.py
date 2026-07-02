import logging

from connectors.servicenow_connector import NORMALIZER_URL


def get_logger():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger(
        "connector-platform"
    )


logger = get_logger()
logger.info(
    "Calling centralized normalizer..."
)

logger.info(
    f"URL: {NORMALIZER_URL}"
)

logger.info(
    "Normalizer response:"
)

logger.info(
    json.dumps(
        response.json(),
        indent=4
    )
)