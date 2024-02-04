from functions import *
from strings_table_edit import strings_delete_request


def persons_send_request(value_column, date_column, sex, education_id, error):
    value_column = value_column.get()
    date_column = date_column.get()
    sex = sex.get()
    education_id = education_id.get()
    
    columns = ["name", "date_birth", "sex", "kod_education"]
    
   
    

    if not value_column or not date_column or not sex or not education_id:
        error['text'] = "Ошибка: Введено пустое значение"
        print("hahaa")
        return
    
    if not is_valid_date(date_column):
        error['text'] = "Ошибка: Неправрильный формат даты. Пример:1980-01-02"
        print("Date is not valid. Example: 1980-01-02")
        return
    
    try:
        int(education_id)
    except Exception:
        error['text'] = "Ошибка NaN"
        print("NaN")
        return

    
    if not db.strict_search("educations", "id_education", education_id):
        error['text'] = "Ошибка: Выберите образование"
        print("No such id")
        return
    
    try:
        db.insert("records_of_services", columns, value_column, date_column, sex, education_id)
    except Exception:
        error['text'] = "Ошибка -1"
        print("Error")
        return
        
    

def persons_delete_request(id_column=None, value_column=None, date_column=None, sex=None, education_id=None, error=None):
    id_record = id_column.get() if id_column else None
    value_column = value_column.get() if value_column else None
    date_column = date_column.get() if date_column else None
    sex = sex.get() if sex else None
    education_id = education_id.get() if education_id else None
    if id_record:
        try:
            db.delete("records_of_services", "id_record", id_record)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
    if value_column:
        try:    
            db.delete("records_of_services", "name", value_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error name")
    if date_column:
        try:
            db.delete("records_of_services", "date_birth", date_column)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error date")
    if sex:
        try:
            db.delete("records_of_services", "sex", sex)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error sex")
    if education_id:
        try:
            db.delete("records_of_services", "kod_education", education_id)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error education")
            
    strings_delete_request(record_column=id_column)
            
    
            
        
def persons_change_request(id_column, value_column, date_column, sex, education_id, error):
    id_column = id_column.get()
    value_column = value_column.get()
    date_column = date_column.get()
    sex = sex.get()
    education_id = education_id.get()
    if not value_column or not date_column or not sex or not education_id:
        error['text'] = "Ошибка: Введено пустое значение"
        print("Null")
        return
    
    try:
        int(education_id)
    except Exception:
        error['text'] = "Ошибка NaN"
        print("NaN")
        return
    
    if not db.strict_search("educations", "id_education", education_id):
        error['text'] = "Ошибка: Выберите образование"
        print("No such id")
        return
    

    if id_column:
        try:
            db.update("records_of_services", ["id_record", id_column], ["name", "date_birth", "sex", "kod_education"], 
                      value_column, date_column, sex, education_id)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error")
