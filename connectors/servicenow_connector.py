from models.incident_model import (
    NormalizedIncident
)


def map_priority(priority):

    mapping = {
        "1": "critical",
        "2": "high",
        "3": "medium",
        "4": "low",
        "5": "info"
    }

    return mapping.get(
        priority,
        "unknown"
    )


def process_servicenow(payload):

    incident = NormalizedIncident(

        source="servicenow",

        ticket_id=
            payload.get(
                "incident",
                ""
            ),

        title=
            payload.get(
                "short_description",
                ""
            ),

        description=
            payload.get(
                "description",
                ""
            ),

        priority=
            payload.get(
                "priority",
                ""
            ),

        severity=
            map_priority(
                payload.get(
                    "priority",
                    ""
                )
            ),

        metadata={

            "caller":
                payload.get(
                    "caller",
                    ""
                ),

            "assignment_group":
                payload.get(
                    "assignment_group",
                    ""
                ),

            "state":
                payload.get(
                    "state",
                    ""
                )
        }
    )

    return incident 