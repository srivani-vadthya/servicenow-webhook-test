# ServiceNow Connector

A FastAPI application that receives, processes, and stores ServiceNow incident webhook payloads in memory.

---

## Project Structure

```
servicenow-connector/
├── api/
│   └── servicenow_connector_api.py     # Route definitions (POST /servicenow, GET /latest, GET /payloads)
├── connectors/
│   └── servicenow_connector.py         # Payload processing logic (adds source field, logs, stores)
├── models/
│   └── servicenow_request_model.py     # Pydantic model for incoming ServiceNow payload validation
├── services/
│   └── payload_storage_service.py      # In-memory list-based payload storage service
├── utils/
│   └── logger_config.py                # Centralized logger configuration
├── main.py                             # FastAPI app entry point, router registration
└── requirements.txt                    # Python dependencies
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework for building the API |
| `uvicorn` | ASGI server to run the FastAPI app |
| `pydantic` | Request body validation via `BaseModel` |
| `requests` | HTTP client (available for outbound calls) |
| `Flask` | Listed in requirements but not used by this app |
| `gunicorn` | Listed in requirements, alternative WSGI server |

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Run

```bash
uvicorn main:app --reload
```

The app will start at `http://127.0.0.1:8000`.

Interactive API docs available at `http://127.0.0.1:8000/docs`.

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check — returns app running status |
| POST | `/servicenow` | Receive and store a ServiceNow incident payload |
| GET | `/latest` | Retrieve the most recently stored payload |
| GET | `/payloads` | Retrieve all stored payloads with count |

---

## Payload Schema

### POST `/servicenow` — Request Body

```json
{
  "incident": "INC0001234",
  "short_description": "Issue summary",
  "description": "Detailed description",
  "priority": "1",
  "caller": "john.doe",
  "assignment_group": "IT Support",
  "state": "New"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `incident` | string | Yes | Incident number (e.g. `INC0001234`) |
| `short_description` | string | Yes | Brief summary of the issue |
| `description` | string | Yes | Full description of the issue |
| `priority` | string | Yes | Priority level (e.g. `1`, `2`, `3`) |
| `caller` | string | No | User who raised the incident (defaults to `""`) |
| `assignment_group` | string | No | Team assigned to the incident (defaults to `""`) |
| `state` | string | No | Current state of the incident (defaults to `""`) |

### POST `/servicenow` — Response

```json
{
  "status": "success",
  "message": "Payload stored successfully",
  "payload_count": 1
}
```

### GET `/latest` — Response

Returns the last received payload with the `source` field appended:

```json
{
  "incident": "INC0001234",
  "short_description": "Issue summary",
  "description": "Detailed description",
  "priority": "1",
  "caller": "john.doe",
  "assignment_group": "IT Support",
  "state": "New",
  "source": "servicenow"
}
```

If no payloads have been received:

```json
{
  "message": "No payloads received"
}
```

### GET `/payloads` — Response

```json
{
  "count": 2,
  "payloads": [...]
}
```

---

## Request Flow

```
POST /servicenow
    └── servicenow_connector_api.py     # Validates request body via ServiceNowRequestModel
        └── servicenow_connector.py     # Adds source="servicenow", logs payload, saves to storage
            └── payload_storage_service.py  # Appends payload to in-memory list
```

---

## Logging

Logs are written to the console using Python's built-in `logging` module.

Format:
```
2024-01-01 12:00:00,000 | INFO | SERVICENOW CONNECTOR TRIGGERED
2024-01-01 12:00:00,001 | INFO | Timestamp: 2024-01-01 12:00:00.123456
2024-01-01 12:00:00,002 | INFO | RAW PAYLOAD RECEIVED
2024-01-01 12:00:00,003 | INFO | { ... payload json ... }
2024-01-01 12:00:00,004 | INFO | Payload Count: 1
```

Logger name: `connector-platform`

---

## Notes

- Payloads are stored in memory and will be lost on app restart.
- Each stored payload automatically includes a `source: "servicenow"` field.
- The app title is `Connector Platform` (version `1.0.0`), visible in the `/docs` Swagger UI.
