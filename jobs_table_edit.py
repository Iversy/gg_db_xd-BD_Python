from functions import *
from strings_table_edit import strings_delete_request


def jobs_send_request(value, salary, error):
    salary = salary.get()
    value = value.get()
    columns = ["jobtitle", "salary"]

    if not value or not salary:
        error['text'] = "Ошибка: Введено пустое значение"
        print("hahaa")
        return
    if db.strict_search("job_titles", "jobtitle", value):
        error['text'] = "Ошибка: Должность уже существует"
        print("Job already exists")
        return
    
    try:
        int(salary)
    except Exception:
        error['text'] = "Ошибка: Введено не число"
        print("NaN")
        return
    
    try:
        db.insert("job_titles", columns, value, salary)
    except Exception:
        error['text'] = "Ошибка -1"
        print("Error -1")
        return
        
    

def jobs_delete_request(value, error):
    value = value.get()
    
    if not (key := db.strict_search("job_titles", "jobtitle", value)[0][0]):
        error['text'] = "Ошибка: Должность не найдена"
        print("Job doesn't exist")
        return

    if key:
        try:
            db.delete("job_titles", "id_jobtitle", key)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")

    strings_delete_request(job_entry=costil(key))
        
def jobs_change_request(id_column,value, salary, error):
    key = id_column.get()
    value = value.get()
    salary = salary.get()

    if not value or not salary:
        error['text'] = "Ошибка: Введено пустое значение"
        print("Null")
        return
    
    try:
        int(salary)
    except Exception:
        error['text'] = "Ошибка: Введено не число"
        print("NaN")
        return


    if key:
        try:
            db.update("job_titles", ["id_jobtitle", key], ["jobtitle", "salary"], value, salary)
        except Exception:
            error['text'] = "Ошибка -1"
            print("Error key")