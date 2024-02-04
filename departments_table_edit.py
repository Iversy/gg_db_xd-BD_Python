from functions import *
from strings_table_edit import strings_delete_request



def departments_send_request(value, error):
    value = value.get()
    columns = ["department"]

    if not value:
        error['text'] = "Ошибка: Введено пустое значение"
        print("hahaa")
        return
    if db.strict_search("departments", "department", value):
        error['text'] = "Ошибка: Такой отделение уже существует"
        print("Department already exists")
        return
    
    try:
        db.insert("departments", columns, value)
    except Exception:
        error['text'] = "Ошибка -1"
        print("Error")
        return
    


def departments_delete_request(value, error):
    value = value.get()
    
    
    if not (key := db.strict_search("departments", "department", value)):
        error['text'] = "Ошибка: Такого отделения не существует или введён пустой запрос"
        print("No value")
        return
    key = key[0][0]

    if key:
        try:
            db.delete("departments", "id_department", key)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
    
    strings_delete_request(kod_department=costil(key))
        
def departments_change_request(id_column,value, error):
    key = id_column.get()
    value = value.get()
    
    if not value:
        error['text'] = "Ошибка: Введено пустое значение"
        print("Null")
        return

    if key:
        try:
            db.update("departments", ["id_department", key], ["department"], value)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
    