from pydantic import BaseModel


class ServiceNowRequestModel(BaseModel):

    incident: str

    short_description: str

    description: str

    priority: str

    caller: str = ""

    assignment_group: str = ""

    state: str = ""