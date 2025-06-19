from fastapi import HTTPException, status


class HTTPAliasNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Alias not found",
            headers=None
        )
