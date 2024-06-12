from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class UserPost(UserBase):
    id: int

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
