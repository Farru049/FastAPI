from pydantic import EmailStr, BaseModel

class UserBase(BaseModel):
    name:str
    age:int
    email:EmailStr
    
class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    
    class config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: int
    description:str | None = None

class ReviewsBase(BaseModel):
    content: str
    rating:str
    