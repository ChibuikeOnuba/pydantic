from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from uuid import uuid4, UUID
from enum import Enum
from datetime import date

class Departments(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"


class Employee(BaseModel):
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Departments
    employee_id: int
    elected_benefits: bool

    @field_validator("employee_id")
    def validate_account_id(value):
        if value <=0:
            raise ValueError(f"account_id must be positive {value}")
        return value

user = Employee(name='Winner', email='onubawinner@042gmail.com',date_of_birth=date(2002,5,11), salary=50000, department=Departments.IT, elected_benefits=True)
print(user)

