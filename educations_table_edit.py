from functions import *
from persons_table_edit import persons_delete_request


def ed_select(table, id_column, ed_column):
    try:
        sel = table.selection()
    except Exception:
        return
    print(sel)
    items = table.item(sel[0])['values']
    print(items)
    id_column.delete(0, tk.END)
    ed_column.delete(0, tk.END)

    id_column.insert(0, items[0])
    ed_column.insert(0, items[1])

def educations_send_request(value, error):
    value = value.get()
    columns = ["education"]

    if not value:
        error['text'] = "Ошибка: Пустой запрос"
        print("No Education given")
        return
    
    if db.strict_search("educations", "education", value):
        error['text'] = "Ошибка: Такое образование уже есть"
        print("Education already exists")
        return
    
    try:
        db.insert("educations", columns, value)
    except Exception:
        error['text'] = "Ошибка -1"
        print("Error")
        return
        
    

def educations_delete_request(value, error):
    edu = value.get()
    
    if not (key := db.strict_search("educations", "education", edu)):
        error['text'] = "Ошибка: Такого образования не существует или введён пустой запрос"
        print("No value")
        return
    print(key)
    key = key[0][0]
    print(key)
    if key:
        try:
            db.delete("educations", "id_education", key)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
   
    persons_delete_request(education_id=costil(key))
            
    
        
def educations_change_request(id_column,value, error):
    key = id_column.get()
    value = value.get()
    
    if not value:
        error['text'] = "Ошибка: Выберите образование"
        print("Null")
        return
    if not (key := db.strict_search("educations", "education", value)):
        error['text'] = "Ошибка: Выберите образование"
        print("No value")
        return
    
    if key:
        try:
            db.update("educations", ["id_education", key], ["education"], value)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")
    