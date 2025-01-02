from app import Employee, user

Employee.model_json_schema()
{
    '$defs': {
        'Department': {
            'enum':['HR', 'IT', 'SALES', 'ENGINEERING'],
            'title': 'Department'
            'type': 'string'
        }
    },

}