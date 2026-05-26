from pydantic import BaseModel


class ToolOutput(BaseModel):

    success: bool
    result: str
    