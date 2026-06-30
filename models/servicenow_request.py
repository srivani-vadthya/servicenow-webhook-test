from pydantic import BaseModel


class ServiceNowRequest(BaseModel):

    incident: str

    short_description: str

    description: str

    priority: str

    caller: str = ""

    assignment_group: str = ""

    state: str = ""