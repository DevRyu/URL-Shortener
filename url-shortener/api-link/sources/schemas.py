from pydantic import BaseModel, constr, HttpUrl


class UrlValidation(BaseModel):
    url: HttpUrl
