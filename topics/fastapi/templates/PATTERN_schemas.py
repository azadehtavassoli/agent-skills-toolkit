from pydantic import BaseModel, Field

class SampleRequest(BaseModel):
    """
    Request schema with strict validation.
    """
    input_value: str = Field(..., min_length=1, description="Input string")

    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
    }


class SampleResponse(BaseModel):
    """
    Response schema.
    """
    message: str
