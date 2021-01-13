#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee(dict):

    Employees = []

    def __init__(self, position=None, name=None, surname=None, plz=None, city=None, phonenumber=None, organisation = None, qualification = None, image=None, street=None, personalwebsite = None, email=None, xing=None):
        dict.__init__(self)
        self["Funktion"] = position
        self["Nachname"] = surname
        self["Vorname"] = name
        self["PLZ (Geschäft)"] = plz
        self["Ort (Geschäft)"] = city
        self["Telefon (Geschäft)"] = phonenumber
        self["Organisation"] = organisation
        self["Qualifikation"] = qualification
        self["Bild"] = image
        self["Strasse"] = street
        self["Eigene Website"] = personalwebsite
        self["EMail"] = email
        self["Xing"] = xing
        
    
    def get_info(self):
        employee_str = ""
        separator_counter = 1

        for key, value in self.items():
            if key == "surname":
                separator = " "
            elif separator_counter < len(self.items()):
                separator = ", "
            else:
                separator = ""

                employee_str += key + ": " + value + separator

            separator_counter += 1

        return employee_str

    def add_employee(self):
        Employee.Employees.append(self)

    # to call a Class Method without self
    @staticmethod
    def get_employees():
        return Employee.Employees


# In[ ]:


#for copy&paste purposes
#Employee(position=position, name=name, surname=surname, plz=plz, city=city, phonenumber=phonenumber, organisation = organisation, qualification = qualification, image=image, street=street, personalwebsite = personalwebsite, email=email, xing=xing).add_employee()

#atList = ["image", "surname", "name", "phonenumber", "position", "street", "city", "plz"]
#employeeAdd = get_employee_add_string(atList)
#print(employeeAdd)


# In[ ]:


position=None
name=None
surname=None
plz=None
city=None
phonenumber=None
organisation = None
qualification = None
image=None
street=None
personalwebsite = None
email=None
xing=None

