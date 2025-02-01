from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict, EmailStr, field_validator



class ContactBase(BaseModel):
    first_name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    phone_number: str = Field(min_length=6, max_length=20)
    birthday: date
    additional_data: Optional[str] = Field(max_length=150)

    @field_validator('birthday')
    def validate_birthday(cls, v):
        if v > date.today():
            raise ValueError('Birthday cannot be in the future')
        return v

class ContactResponse(ContactBase):
    id: int
    created_at: datetime | None
    updated_at: Optional[datetime] | None
   
    model_config = ConfigDict(from_attributes=True)


class ContactBirthdayRequest(BaseModel):
    days: int = Field(ge=0, le=366)

    # @field_validator('month')
    # def validate_month(cls, v):
    #     if v < 1 or v > 12:
    #         raise ValueError('Month must be between 1 and 12')
    #     return v

    # @field_validator('day')
    # def validate_day(cls, v):
    #     if v < 1 or v > 31:
    #         raise ValueError('Day must be between 1 and 31')
    #     return v
