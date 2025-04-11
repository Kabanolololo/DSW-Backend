from pydantic import BaseModel

# Schemat dla tokenu
class Token(BaseModel):
    access_token: str
    token_type: str
