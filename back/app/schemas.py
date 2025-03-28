from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class AuthorBase(BaseModel):
    name: str

class Author(AuthorBase):
    id: int
    books: List["Book"] = []  
    class Config:
        from_attributes = True
        
class AuthorCreate(AuthorBase):
    pass

class GenreBase(BaseModel):
    name: str

class Genre(GenreBase):
    id: int
    books: List["Book"] = []
    class Config:
        from_attributes = True
        
class GenreCreate(GenreBase):
    pass

class BookBase(BaseModel):
    title: str
    description: str
    genre_id: Optional[int]  
    author_id: int
    release_date: Optional[date]  
    

class BookResponse(BaseModel):
    id: str  
    title: str
    description: str
    genre_name: str
    author_name: str
    author_id: int
    release_date: Optional[str] = None  
    favorites_count: int
    is_favorite: bool

    class Config:
        from_attributes = True 

    @classmethod
    def from_orm(cls, book):
        return cls(
            id=book.id,
            title=book.title,
            description=book.description,
            genre_id=book.genre_id,
            author_id=book.author_id,
            release_date=book.release_date.strftime("%Y-%m-%d") if book.release_date else None
        )
        
class Book(BookBase):
    id: int
    author: Optional[Author]  
    genre: Optional[Genre]
    class Config:
        from_attributes = True

class BookCreate(BookBase):
    pass

class UserCreate(BaseModel):
    nickname: str
    email: EmailStr
    password: str  

class UserLogin(BaseModel):
    nickname: str
    password: str
    
class UserOut(BaseModel):
    id: int
    nickname: str
    email: EmailStr
    role_id: int
    
    class Config:
        from_attributes = True

class RoleOut(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
class Token(BaseModel):
    access_token: str
    token_type: str
class PendingBookBase(BaseModel):
    title: str
    author_name: str
    
class PendingBookCreate(PendingBookBase):
    pass

class PendingBookUpdate(BaseModel):
    status_id: int


class PendingBookOut(PendingBookBase):
    id: int
    requsted_by: int
    status: str
    
    class Config:
        from_attributes = True


class GenreOut(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

