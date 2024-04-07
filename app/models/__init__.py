from typing import Union

from pydantic import BaseModel, validator, field_validator


class ConverterRequest(BaseModel):
    number: Union[int, str]


class ConverterResponse(BaseModel):
    arabic: int
    roman: str


class User(BaseModel):
    name: str
    age: int
    adult: bool = None

    @field_validator("age")
    def age_must_be_valid(cls, value):
        if value < 0 or value > 100:
            raise ValueError('Age must be between 0 and 100')
        return value

    @field_validator('adult')
    def determine_adult(cls, v, values):
        if 'age' in values:
            return values['age'] >= 18
        return None


class BigJson(BaseModel):
    """Использует модель User."""
    user: User




"""
    @field_validator("age")
    def validateAge(cls, age, values):
        if 0 < age < 100:
            if age > 18:
                values.adult = True
                return age, values.adult
            else:
                values.adult = False
                return age, values.adult
        else:
            raise ValueError("Error")
"""

# class UserRequest(BaseModel):
#     name: str
#     message: str
#
#
# class User(BaseModel):
#     name: str
#     age: str
#     is_adult: bool
#     message: str = None
#
#
# class UserResponse(BaseModel):
#     pass
