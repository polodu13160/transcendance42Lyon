from pydantic import BaseModel



class HttpErrorSchema(BaseModel):
    code: int
    reason: str | None
    explain: str | None


