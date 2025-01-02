from pydantic import BaseModel, EmailStr, field_validator, ValidationError, Field
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
    employee_id: UUID = uuid4
    elected_benefits: bool


# VALIDATION SECTION ------------------------------------------------------
    @field_validator("salary")
    def validate_account_id(value):
        if value <=0:
            raise ValueError(f"salary must be positive, you returned {value}")
        return value
    

    @field_validator("date_of_birth")
    def age_checker(value):
        today = date.today()
        entry_age = today.year - value.year
        if entry_age < 18:
            raise ValueError(f"you must be at least 18 years, you are {entry_age} years old")
        return value
#----------------------------------------------------------------------------
user = Employee(
    name='Winner',
    email='onubawinner@042gmail.com',
    date_of_birth=date(2002,5,11), 
    salary=50000,
    department=Departments.IT, 
    employee_id="123e4567-e89b-12d3-a456-426614174000",
    elected_benefits=True
    )

# working with dicts

employee_dict = {
    "name":'Winner', 
    'email':'onubawinner@042gmail.com',
    'date_of_birth':"2002-05-11", 
    'salary':"50000",
    'department':'IT', 
    'elected_benefits':True
}

# print(Employee.model_validate(employee_dict))
# print('---------------------------------')
# print(Employee(**employee_dict))

# working with JSONS

employee_json = """
    {"name":"Winner", 
    "email":"onubawinner042@gmail.com",
    "date_of_birth":"2002-05-11", 
    "salary":50000,
    "department":"IT", 
    "employee_id":"123e4567-e89b-12d3-a456-426614174000",
    "elected_benefits":true}
    """
json_to_pyd = Employee.model_validate_json(employee_json)
print(json_to_pyd)
print('--------------------------------')
print(user.model_dump_json())



