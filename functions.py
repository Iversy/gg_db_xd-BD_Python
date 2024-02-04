import tkinter as tk
from database_sql import *
import re

def update(table, result):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(result):
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
        
def is_valid_date(date):
    pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    return bool(pattern.match(date))

def costil(value):
    class Costil:
        def __init__(self, value):
            self.value = value
        def get(self):
            return self.value
    return Costil(value)

def persons_select(table, sex, *args):
    try:
        sel = table.selection()
        print(sel)
        items = table.item(sel[0])['values']
        print(items)
    except Exception:
        return
    options = ["мужской", "женский"]
    sex.current(options.index(items[3]))
    items.pop(3)
    args[-2]['state'] = 'normal'
    for i, item in enumerate(args):
        item.delete(0, tk.END)
        item.insert(0, items[i])
    args[-2]['state'] = 'readonly'
    

def any_select(table, *args):
    try:
        sel = table.selection()
        print(sel)
        items = table.item(sel[0])['values']
        print(items)
    except Exception:
        return
    
    for i, item in enumerate(args):
        item.delete(0, tk.END)
        item.insert(0, items[i])
   
def strings_select(table, id_column, record_column, number_column, date_column, job, job_id, department, department_id):
    try:
        sel = table.selection()
        print(sel)
        items = table.item(sel[0])['values']
        print(items)
        id_column.delete(0, tk.END)
        id_column.insert(0, items[0])
        record_column['state'] = 'normal'
        record_column.delete(0, tk.END)
        record_column.insert(0, items[1])
        record_column['state'] = 'readonly'
        number_column.delete(0, tk.END)
        number_column.insert(0, items[3])
        date_column['state'] = 'normal'
        date_column.delete(0, tk.END)
        date_column.insert(0, items[4])
        date_column['state'] = 'readonly'
        job['state'] = 'normal'
        job.delete(0, tk.END)
        job.insert(0, items[5])
        job['state'] = 'readonly'
        department['state'] = 'normal'
        department.delete(0, tk.END)
        department.insert(0, items[6])
        department['state'] = 'readonly'
        job_id.delete(0, tk.END)
        job_id.insert(0, items[7])
        department_id.delete(0, tk.END)
        department_id.insert(0, items[8])
    except Exception:
        return


def update_lists(sql_table, table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.view(sql_table)):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
        
def update_persons(table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.records_view()):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
    
def search_button(sql_table, value, table):
    if not value.get():
        update_lists(sql_table, table)
        return
    result = db.search(sql_table, value.get())
    update(table, result)
    
def search_records(value,table):
    if not value.get():
        update_persons(table)
        return
    result = db.search_records(value.get())
    update(table, result)


def search_strings(value, table):
    if not value.get():
        update_strings(table)
        return
    result = db.search_employed(value.get())
    update(table, result)

def update_person(table, wb_number, name, sex, date, edu, edu_id):
    if not wb_number.get():
        print("Не введен номер записи")
        return
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.view_person_table(wb_number.get())):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
    data = db.view_person_info(wb_number.get())[0]
    name.delete(0, tk.END)
    name.insert(0, data[0])
    date.delete(0, tk.END)
    date.insert(0, data[1])
    
    sex['text'] = data[2]
    edu_id.delete(0, tk.END)
    edu_id.insert(0, data[3])
    edu['state'] = "normal"
    edu.delete(0, tk.END)
    edu.insert(0, data[4])
    edu['state'] = "readonly"
    
def search_results(value, table):
    if not value.get():
        update_results(table)
        return
    result = db.search_results(value.get())
    update(table, result)

def change_person(wb_number, name, edu_id, sex, date, error, sex_entry):
    columns = ["name", "date_birth", "sex", "kod_education"]
    ids = ["id_record", wb_number.get()]
    if not is_valid_date(date.get()):
        error['text'] = "Ошибка: Неправрильный формат даты. Пример:1980-01-02"
        return
    if not name.get():
        error['text'] = "Ошибка: Не введено имя"
        return
    if not edu_id.get():
        error['text'] = "Ошибка: Не введено образование"
        return        
    if not sex.get():
        print(sex_entry['text'])
        sex = costil(sex_entry['text'])
    
    try:
        db.update("records_of_services", ids, columns, name.get(), date.get(), sex.get(), edu_id.get())
    except Exception:
        error['text'] = "Ошибка -1"
    
def update_results(table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.view_all()):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
        
def update_people(table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.count_records()):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
        
def get_avg_salary(message):
    message["text"] = f"Средняя зарплата = {db.avg_salary()[0][0]}"
    
def get_number_of_people(message):
    message["text"] = f"Количество сотрудников = {db.count_people()[0][0]}"
    
def update_records_choose(table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.view_records_part()):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)
    
    
def update_strings(table):
    for row in table.get_children():
        table.delete(row)
    for i, row in enumerate(db.view_employed()):    
        table.insert(parent='',index='end',iid=i,text='',
                    values=row)