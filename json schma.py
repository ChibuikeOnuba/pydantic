from app import Employee, user, Departments
from uuid import UUID, uuid4
from datetime import date
from enum import Enum
from pydantic import BaseModel, Field, EmailStr

Employee.model_json_schema()


# FURTHER VALIDATION TECHNIQUES

class newEmployee(BaseModel):
    employee_id: UUID = Field(default=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".@yahoo\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(gt=0, repr=False, alias="compensation")
    department: Departments
    elected_benefits: bool

new_user = Employee(
    name="Frames",
    email="onubawinner042@yahoo.com",
    date_of_birth=date(2005,5,11),
    salary=50,
    department=Departments.SALES,
    elected_benefits=True
)

print(new_user)