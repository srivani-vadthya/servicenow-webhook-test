# from flask import Flask, request, jsonify
# import datetime
# import logging
# import sys

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s | %(levelname)s | %(message)s',
#     handlers=[logging.StreamHandler(sys.stdout)]
# )

# logger = logging.getLogger(__name__)

# app = Flask(__name__)

# @app.route("/")
# def home():

#     logger.info("HOME ENDPOINT CALLED")

#     return {
#         "message": "ServiceNow Webhook Server Running"
#     }


# @app.route("/incident", methods=["POST"])
# def incident():

#     logger.info("")
#     logger.info("===================================")
#     logger.info("SERVICENOW INCIDENT RECEIVED")
#     logger.info("===================================")

#     logger.info(
#         f"Time: {datetime.datetime.now()}"
#     )

#     data = request.get_json()

#     logger.info(
#         f"Payload: {data}"
#     )

#     response = {
#         "status": "success",
#         "message": "Incident received",
#         "incident": data.get("incident"),
#         "triggered": True
#     }

#     logger.info(
#         f"Response: {response}"
#     )

#     logger.info("===================================")

#     return jsonify(response), 200


# @app.errorhandler(Exception)
# def handle_error(error):

#     logger.exception(
#         f"ERROR OCCURRED: {error}"
#     )

#     return jsonify({
#         "status": "error",
#         "message": str(error)
#     }), 500


# if __name__ == "__main__":
#     logger.info("APPLICATION STARTED")
#     app.run(
#         host="0.0.0.0",
#         port=5000
#     )