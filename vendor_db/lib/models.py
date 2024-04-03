from typing import Optional
from sqlmodel import Field, SQLModel

class Store(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    source: str 
    
    icon: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    categories: Optional[str] = None
    email: Optional[str] = None
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None
    nb_employee: Optional[int] = None
    ca: Optional[float] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    location: Optional[str] = None
    country_code: Optional[str] = None
    store_type: Optional[str] = None
    embed: Optional[str] = None


