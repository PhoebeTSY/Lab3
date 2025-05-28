import employee_info as employeeinfo

def get_employees_by_age_range():
    expected_results = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    ]
    result = employeeinfo.get_employees_by_age_range()

    assert(result == expected_results)

def test_calculate_average_salary():
    expected_results = 60166.67
    result = employeeinfo.calculate_average_salary()

    assert(result == expected_results)

def test_get_employees_by_dept():
    expected_results = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000},
    ]
    result = employeeinfo.get_employees_by_dept('Sales')

    assert(result == expected_results)

