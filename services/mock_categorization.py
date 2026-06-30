def categorize(incident):

    text = (
        incident.title +
        " " +
        incident.description
    ).lower()

    # Infrastructure incidents
    if (
        "cpu" in text or
        "memory" in text or
        "disk" in text or
        "server" in text
    ):

        return {

            "category":
                "L1",

            "subcategory":
                "Infrastructure",

            "confidence":
                0.95,

            "assigned_agent":
                "L1-Agent"
        }

    # Database incidents
    if (
        "oracle" in text or
        "database" in text or
        "sql" in text
    ):

        return {

            "category":
                "L2",

            "subcategory":
                "Database",

            "confidence":
                0.91,

            "assigned_agent":
                "Database-Agent"
        }

    return {

        "category":
            "L2",

        "subcategory":
            "Application",

        "confidence":
            0.85,

        "assigned_agent":
            "Application-Agent"
    }