# подключаем библиотеку для работы с базой данных
import sqlite3    
"""
CREATE TABLE IF NOT EXISTS educations (id_education INTEGER Not Null, education TEXT Not Null, PRIMARY KEY(id_education));)

CREATE TABLE IF NOT EXISTS job_titles (id_jobtitle INTEGER Not Null UNIQUE, jobtitle TEXT Not Null, salary INTEGER CHECK(salary>0) DEFAULT 0, PRIMARY KEY(id_jobtitle));

CREATE TABLE IF NOT EXISTS departments (id_department INTEGER Not Null UNIQUE, department TEXT Not Null, PRIMARY KEY(id_department));

CREATE TABLE IF NOT EXISTS records_of_services (id_record TEXT(16) Not Null UNIQUE, name TEXT Not Null, date_birth DATE Not Null, sex TEXT(8) Not Null, kod_education INTEGER Not Null, PRIMARY KEY(id_record), FOREIGN KEY (kod_education) REFERENCES educations(id_education));

CREATE TABLE IF NOT EXISTS strings (id_string INTEGER Not Null, kod_record TEXT(16) Not Null, number INTEGER Not Null CHECK(number>0), date_string DATE Not Null, kod_jobtitle INTEGER Not Null, kod_department INTEGER Not Null, PRIMARY KEY(id_string), FOREIGN KEY (kod_record) REFERENCES records_of_services(id_record), FOREIGN KEY (kod_jobtitle) REFERENCES job_titles(id_jobtitle), FOREIGN KEY (kod_department) REFERENCES departments(id_department));


"""
# создаём класс для работы с базой данных
class DB:                        
    # конструктор класса
    def __init__(self):           
        # соединяемся с файлом базы данных
        self.conn = sqlite3.connect("employee.db")  
        # создаём курсор для виртуального управления базой данных
        self.cur = self.conn.cursor()    
        # если нужной нам таблицы в базе нет — создаём её
        self.cur.execute(             
            "CREATE TABLE IF NOT EXISTS educations (id_education INTEGER Not Null, education TEXT Not Null, PRIMARY KEY(id_education));")
        self.cur.execute(             
            "CREATE TABLE IF NOT EXISTS job_titles (id_jobtitle INTEGER Not Null UNIQUE, jobtitle TEXT Not Null, salary INTEGER CHECK(salary>0) DEFAULT 0, PRIMARY KEY(id_jobtitle));") 
        self.cur.execute(             
            "CREATE TABLE IF NOT EXISTS departments (id_department INTEGER Not Null UNIQUE, department TEXT Not Null, PRIMARY KEY(id_department));") 
        self.cur.execute(             
            "CREATE TABLE IF NOT EXISTS records_of_services (id_record INTEGER Not Null UNIQUE, name TEXT Not Null, date_birth DATE Not Null, sex TEXT(8) Not Null, kod_education INTEGER Not Null, PRIMARY KEY(id_record), FOREIGN KEY (kod_education) REFERENCES educations(id_education));") 
        self.cur.execute(             
            "CREATE TABLE IF NOT EXISTS strings (id_string INTEGER Not Null, kod_record INTEGER Not Null, number INTEGER Not Null CHECK(number>0), date_string DATE Not Null, kod_jobtitle INTEGER Not Null, kod_department INTEGER Not Null, PRIMARY KEY(id_string), FOREIGN KEY (kod_record) REFERENCES records_of_services(id_record), FOREIGN KEY (kod_jobtitle) REFERENCES job_titles(id_jobtitle), FOREIGN KEY (kod_department) REFERENCES departments(id_department));") 

        # сохраняем сделанные изменения в базе
        self.conn.commit()  

    # деструктор класса
    def __del__(self):        
        # отключаемся от базы при завершении работы
        self.conn.close()   
   
    # просмотр всех записей
    def view(self, table):        
        self.cur.execute(f"SELECT * FROM {table}")
        return self.cur.fetchall()

    def view_all(self):
        query = ("SELECT "
            "id_record, "
            "name, "
            "date_birth, "
            "sex, "
            "e.education, "
            "number, "
            "date_string, "
            "j.jobtitle, "
            "j.salary, "
            "d.department "
        "FROM "
        "    strings s "
        "    JOIN records_of_services ros ON s.kod_record = ros.id_record "
        "    JOIN educations e ON ros.kod_education = e.id_education "
        "    JOIN job_titles j ON s.kod_jobtitle = j.id_jobtitle "
        "    JOIN departments d ON s.kod_department = d.id_department;")
        self.cur.execute(query)
        return self.cur.fetchall()

    # добавляем новую запись
    def insert(self, table, columns, *args):
        query = ", ".join("?"*len(args))
        columns = ", ".join(columns)
        print(columns)
        print(*args)
        self.cur.execute(f"INSERT INTO {table}({columns}) VALUES ({query})", args)
        self.conn.commit()
        

    def update(self, table, id, keys, *args ):   
        keys.append("")
        keys = "=?, ".join(keys)[:-2]
        print(keys)
        self.cur.execute(f"UPDATE {table} SET {keys} WHERE {id[0]}=?", (*args, id[1],))
        self.conn.commit()
    
    def delete(self, table, key, value):             
        self.cur.execute(f"delete from {table} where {key}=?", (value,))
        self.conn.commit()

    def search(self, table, value):
        columns = self.column_names(table)
        value = [f"%{value}%"]*len(columns)

        if_query =  " LIKE ? OR ".join(columns) + " LIKE ?"
        query = f"SELECT * FROM {table} WHERE {if_query}"

        self.cur.execute(query, (*value,))
        return self.cur.fetchall()

    def strict_search(self, table, key, value):
        query = f"SELECT * FROM {table} WHERE {key}=?"
        self.cur.execute(query, (value,))
        return self.cur.fetchall()
    
    def search_results(self, value):
        columns = ["id_record", "name", "date_birth", "sex", "e.education", "number ", "date_string", "j.jobtitle", "j.salary", "d.department"]
        value = [f"%{value}%"]*len(columns)
        columns_part = ", ".join(columns)
        from_part = ("FROM "
        "    strings s "
        "    JOIN records_of_services ros ON s.kod_record = ros.id_record "
        "    JOIN educations e ON ros.kod_education = e.id_education "
        "    JOIN job_titles j ON s.kod_jobtitle = j.id_jobtitle "
        "    JOIN departments d ON s.kod_department = d.id_department")

        if_part =  " LIKE ? OR ".join(columns) + " LIKE ?"
        query = f"SELECT {columns_part} {from_part} WHERE {if_part}"

        self.cur.execute(query, (*value,))
        return self.cur.fetchall()

    def column_names(self, table):
        self.cur.execute(f"PRAGMA table_info({table})")
        return [i[1] for i in self.cur.fetchall()]
    
    def avg_salary(self):
        query = ("SELECT AVG(salary) as AverageSalary "
                 "FROM job_titles ")
        self.cur.execute(query)
        return self.cur.fetchall()

    def count_records(self):
        query = ("SELECT "
        "records_of_services.name,"
        "    COUNT(strings.id_string) as Number_of_jobs "
        "FROM"
        "    records_of_services "
        "INNER JOIN "
        "    strings ON records_of_services.id_record = strings.kod_record "
        "GROUP BY "
        "    records_of_services.name;")
        self.cur.execute(query)
        return self.cur.fetchall()

    def count_people(self):
        query = ("SELECT COUNT(DISTINCT records_of_services.name) as Number_of_Persons "
        "FROM records_of_services "
        "INNER JOIN strings ON records_of_services.id_record = strings.kod_record;")
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def get_max_number(self, record):
        query = ("SELECT MAX(number) FROM strings WHERE kod_record = ?")
        self.cur.execute(query, (record,))
        return self.cur.fetchall()
    
    def records_view(self):
        query = ("select rs.id_record, rs.name, rs.date_birth, rs.sex, e.education, rs.kod_education "
                "from records_of_services rs "
                "join educations e on rs.kod_education = e.id_education")
        self.cur.execute(query)
        return self.cur.fetchall()

    def search_records(self, value):
        query = ("select rs.id_record, rs.name, rs.date_birth, rs.sex, e.education, rs.kod_education "
                "from records_of_services rs "
                "join educations e on rs.kod_education = e.id_education "
                "where rs.name like ? or rs.id_record like ? or rs.sex like ? or rs.date_birth like ? or e.education like ?")
        self.cur.execute(query, (f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%",))
        return self.cur.fetchall()
    
    def view_records_part(self):
        query = ("SELECT id_record, name, date_birth FROM records_of_services")
        self.cur.execute(query)
        return self.cur.fetchall()

    def view_employed(self):
        query = ("SELECT s.id_string, s.kod_record, r.name, s.number, s.date_string, j.jobtitle, d.department, s.kod_jobtitle, s.kod_department "
                "FROM strings s JOIN records_of_services r ON s.kod_record = r.id_record "
                "JOIN job_titles j ON s.kod_jobtitle = j.id_jobtitle "
                "JOIN departments d ON s.kod_department = d.id_department")
        self.cur.execute(query)
        return self.cur.fetchall()   
        
    def search_employed(self, value):
        query = ("SELECT s.id_string, s.kod_record, r.name, s.number, s.date_string, j.jobtitle, d.department, s.kod_jobtitle, s.kod_department "
                "FROM strings s JOIN records_of_services r ON s.kod_record = r.id_record "
                "JOIN job_titles j ON s.kod_jobtitle = j.id_jobtitle "
                "JOIN departments d ON s.kod_department = d.id_department "
                "WHERE r.name like ? or s.number like ? or s.date_string like ? or j.jobtitle like ? or d.department like ? or s.kod_record like ?")
        self.cur.execute(query, (f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%", f"%{value}%",))
        return self.cur.fetchall()
    
    def view_person_table(self, wb_number):
        query = ("SELECT "
            "s.number, "
            "s.date_string, "
            "j.jobtitle, "
            "j.salary, "
            "d.department "
        "FROM "
        "    strings s "
        "    JOIN records_of_services ros ON s.kod_record = ros.id_record "
        "    JOIN job_titles j ON s.kod_jobtitle = j.id_jobtitle "
        "    JOIN departments d ON s.kod_department = d.id_department "
        "WHERE s.kod_record = ?")
        self.cur.execute(query, (wb_number,))
        return self.cur.fetchall()
    
    def view_person_info(self, wb_number):
        query = ("SELECT "
                 "r.name, r.date_birth, r.sex, r.kod_education, e.education "
                 "FROM records_of_services r JOIN educations e ON r.kod_education = e.id_education "
                 "WHERE r.id_record = ?")
        self.cur.execute(query, (wb_number,))
        return self.cur.fetchall()
    
    
db = DB()

print(db.avg_salary())
print(db.count_records())
print(db.count_people())