import requests
from employeeTable import employeeTable
import datetime
import requests
from employeApi import EmployeeApi

db_connection_string = "postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet"
url = "https://x-clients-be.onrender.com"
sql = employeeTable(db_connection_string)
api = EmployeeApi(url)


def test_create_new_employee():
    name = "ООО Мадагкскар"
    description = "Туры в Африку"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    employee_before = sql.get_employee_id(company_id)
    api.add_employee(
        id="3158",
        first_name="Sasha",
        last_name="Morgan",
        middle_name="Ivanovich",
        company_id= company_id,
        mail="datch@example.com",
        employee_url="http://example.com",
        phone="8976493208",
        birthdate= '2024-03-22T12:24:58.028Z',
        is_active=True
    )
    employee_id = sql.get_employee_max_id()
    employee_after = sql.get_employee_id(company_id)
    assert len(employee_after) > len(employee_before)
    assert sql.get_company()[-1]["name"] == "ООО Мадагкскар"
    assert sql.get_company()[-1]["description"] == "Туры в Африку"
    assert sql.get_employee()[-1]["first_name"] == 'Sasha'
    assert sql.get_employee()[-1]["last_name"] == 'Morgan'
    assert sql.get_employee()[-1]["middle_name"] == 'Ivanovich'
    assert sql.get_employee()[-1]["email"] == None
    assert sql.get_employee()[-1]["avatar_url"] == 'http://example.com'
    assert sql.get_employee()[-1]["phone"] == '8976493208'
    assert sql.get_employee()[-1]["birthdate"] == datetime.date(2024, 3, 22)
    assert sql.get_employee()[-1]["is_active"] == True
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)


def test_change_employee():
    name = "ООО Лянча"
    description = "Итальянские машины"
    sql.create_company(name, description)
    company_id = sql.get_max_id_company()
    employee_before = sql.get_employee_id(company_id)
    employee = api.add_employee(
        id="3158",
        first_name="Павел",
        last_name="Брашалов",
        middle_name="Дмитриевич",
        company_id= company_id,
        mail="pizza@example.com",
        employee_url="http://ya.ru",
        phone="88709087654",
        birthdate= '2024-03-22T12:24:58.028Z',
        is_active=True
    )
    api.change_employee(
        id = employee,
        change_lastName = "Брюлов" ,
        change_email = "samurai@cyber.ru", 
        change_url = "https://www.google.ru/", 
        change_phone = "89763215423",
        change_active = False
    )
    employee_id = sql.get_employee_max_id()
    assert sql.get_company()[-1]["name"] == "ООО Лянча"
    assert sql.get_company()[-1]["description"] == "Итальянские машины"
    assert sql.get_employee()[-1]["last_name"] == 'Брюлов'
    assert sql.get_employee()[-1]["email"] =='samurai@cyber.ru'
    assert sql.get_employee()[-1]["avatar_url"] == 'https://www.google.ru/'
    assert sql.get_employee()[-1]["phone"] == '88709087654'
    assert sql.get_employee()[-1]["is_active"] == False
    sql.delete_employee(employee_id)
    sql.delete_company(company_id)