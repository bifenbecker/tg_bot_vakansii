from tools.wrappers.forms import SimpleForm
from apps.test.views.FormStep0View import Step0
from apps.test.views.FormStep1View import Step1
from pydantic import BaseModel, field_validator, Field
from typing import Optional


class Person(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=18)

    @field_validator('name')
    def name_less_then_siz(cls, name):
        if len(name) > 6:
            raise ValueError('Name must be less than 6')
        return name


class ExampleForm(SimpleForm):
    Schema = Person
    VIEWS = [
        Step0,
        Step1
    ]

    def save_data(self):
        print("SAVE DATA")
