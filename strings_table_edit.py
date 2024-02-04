from functions import *

def strings_send_request(record_column, date_column, job_entry, kod_department, error):
    record_column = record_column.get()
    date_column = date_column.get()
    job_entry = job_entry.get()
    kod_department = kod_department.get()
    columns = ["kod_record", "number", "date_string", "kod_jobtitle", "kod_department"]
    

    if not record_column or not date_column or not job_entry or not kod_department:
        error['text'] = "Ошибка: Введено пустое значение"
        print("hahaa")
        return

    try:
        int(record_column)
        int(job_entry)
        int(kod_department)
    except Exception:
        error['text'] = "Ошибка: Введено не число"
        print("NaN")
        return
    
    if db.strict_search("strings", "date_string", date_column):
        error['text'] = "Ошибка: В один день принимаем одного сотрудника!"
        print("Date already exists")
        return
    
    if not db.strict_search("records_of_services", "id_record", record_column):
        print("No such id record")
        return
    if not db.strict_search("job_titles", "id_jobtitle", job_entry):
        print("No such id job")
        return
    if not db.strict_search("departments", "id_department", kod_department):
        print("No such id department")
        return
    
    number_column = db.get_max_number(record_column)[0][0] + 1

    try:
        db.insert("strings", columns, record_column, number_column, date_column, job_entry, kod_department)
    except Exception:
        error['text'] = "Ошибка -1"
        print("Error")
        return
        
    

def strings_delete_request(id_column=None, record_column=None, number_column=None, date_column=None, job_entry=None, kod_department=None, error=None):
    id_column = id_column.get() if id_column else None
    record_column = record_column.get() if record_column else None
    number_column = number_column.get() if number_column else None
    date_column = date_column.get() if date_column else None
    job_entry = job_entry.get() if job_entry else None
    kod_department = kod_department.get() if kod_department else None

    if id_column:
        try:
            db.delete("strings", "id_string", id_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
    if record_column:
        try:
            db.delete("strings", "kod_record", record_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error record")
    if number_column:
        try:
            db.delete("strings", "number", number_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error number")
    if date_column:
        try:
            db.delete("strings", "date_string", date_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error date")
    if job_entry:
        try:
            db.delete("strings", "kod_jobtitle", job_entry)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error job")
    if kod_department:
        try:
            db.delete("strings", "kod_department", kod_department)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error department")
            
        
def strings_change_request(id_column, record_column, number_column, date_column, job_entry, kod_department, error):
    id_column = id_column.get()
    record_column = record_column.get()
    number_column = number_column.get()
    date_column = date_column.get()
    job_entry = job_entry.get()
    kod_department = kod_department.get()
    
    if not record_column or not number_column or not date_column or not job_entry or not kod_department:
        error['text'] = "Ошибка: Введено пустое значение"
        print("Null")
        return
    
    try:
        int(record_column)
        int(number_column)
        int(job_entry)
        int(kod_department)
    except Exception:
        error['text'] = "Ошибка: Введено не число"
        print("NaN")
        return
    
    if not db.strict_search("records_of_services", "id_record", record_column):
        print("No such id record")
        return
    if not db.strict_search("job_titles", "id_jobtitle", job_entry):
        print("No such id job")
        return
    if not db.strict_search("departments", "id_department", kod_department):
        print("No such id department")
        return
    

    if id_column:
        try:
            db.update("strings", ["id_string", id_column], ["kod_record", "number", "date_string", "kod_jobtitle", "kod_department"], 
                      record_column, date_column, job_entry, kod_department)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error")