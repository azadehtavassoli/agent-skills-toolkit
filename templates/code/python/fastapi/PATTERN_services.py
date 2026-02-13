from app.schemas import SampleRequest, SampleResponse

class SampleService:
    """
    Business logic layer.
    All heavy logic should live here, not in routes.
    """

    async def process(self, payload: SampleRequest) -> SampleResponse:
        # core logic goes here
        # example: basic transformation
        return SampleResponse(
            message=f"processed: {payload.input_value}"
        )
