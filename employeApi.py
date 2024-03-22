import requests
import random 
class EmployeeApi:
    url = "https://x-clients-be.onrender.com"
    def __init__(self,url):
        self.url = url
    def get_token(self, user = 'bloom', password = 'fire-fairy'):
        creds = {'username': user,
             'password': password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        self.user_token = resp.json()["userToken"]
        return self.user_token

    def create_new_company(self, name, description):
        company = {"name": name, 
        "description": description}
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()["id"]
    

    def get_employee(self,company_id):
        params = {'company': company_id}
        response = requests.get(self.url + '/employee', params=params)
        return response.json()

    def add_employee(self, id, company_id, first_name, last_name, middle_name, mail, employee_url, phone, birthdate, is_active):
        employee_data = {
        "id": id,
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": company_id,
        "email": mail,
        "url": employee_url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": is_active
    }
        if company_id is None:
            company_id = self.create_new_company()
        if not all([first_name, last_name, company_id, mail, phone, birthdate]):
            raise ValueError("Не все обязательные поля заполнены")
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json=employee_data, headers=my_headers)
        return resp.json()
    
    def get_employee_id(self, id_get):
       resp = requests.get(self.url+f"/employee/{id_get.get('id')}")
       return resp.json()
    
    
    def change_employee(self, id, change_lastName, change_email, change_url, change_phone, change_active):
        change_employee = {
        "lastName": change_lastName,
        "email": change_email,
        "url": change_url,
        "phone": change_phone,
        "isActive": change_active
    }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url+f"/employee/{id.get('id')}", json=change_employee, headers=my_headers)
        return resp.json()
    

    