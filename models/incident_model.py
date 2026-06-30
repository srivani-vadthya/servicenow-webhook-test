from pydantic import BaseModel


class NormalizedIncident(BaseModel):

    source: str

    ticket_id: str

    title: str

    description: str

    priority: str

    severity: str

    metadata: dict