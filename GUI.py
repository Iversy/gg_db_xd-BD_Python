from headers import *


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Empoyee DB")
        width=500
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        Beducations=tk.Button(self.root)
        Beducations["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Beducations["font"] = ft
        Beducations["fg"] = "#000000"
        Beducations["justify"] = "center"
        Beducations["text"] = "Образование"
        Beducations.place(x=40,y=230,width=155,height=30)
        Beducations["command"] = self.educations_window

        Bpersons=tk.Button(self.root)
        Bpersons["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bpersons["font"] = ft
        Bpersons["fg"] = "#000000"
        Bpersons["justify"] = "center"
        Bpersons["text"] = "Сотрудники"
        Bpersons.place(x=40,y=190,width=155,height=30)
        Bpersons["command"] = self.persons_window

        Bjob=tk.Button(self.root)
        Bjob["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bjob["font"] = ft
        Bjob["fg"] = "#000000"
        Bjob["justify"] = "center"
        Bjob["text"] = "Должности"
        Bjob.place(x=40,y=150,width=155,height=30)
        Bjob["command"] = self.job_window

        Bdepartment=tk.Button(self.root)
        Bdepartment["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bdepartment["font"] = ft
        Bdepartment["fg"] = "#000000"
        Bdepartment["justify"] = "center"
        Bdepartment["text"] = "Отделения"
        Bdepartment.place(x=40,y=110,width=155,height=30)
        Bdepartment["command"] = self.department_window

        Bemployed=tk.Button(self.root)
        Bemployed["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bemployed["font"] = ft
        Bemployed["fg"] = "#000000"
        Bemployed["justify"] = "center"
        Bemployed["text"] = "Записи о трудоустройстве"
        Bemployed.place(x=40,y=70,width=155,height=30)
        Bemployed["command"] = self.employed_window
        
        Bresults=tk.Button(self.root)
        Bresults["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bresults["font"] = ft
        Bresults["fg"] = "#000000"
        Bresults["justify"] = "center"
        Bresults["text"] = "Полная таблица"
        Bresults.place(x=215,y=70,width=155,height=30)
        Bresults["command"] = self.results_window
        
        Bstatistics=tk.Button(self.root)
        Bstatistics["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Bstatistics["font"] = ft
        Bstatistics["fg"] = "#000000"
        Bstatistics["justify"] = "center"
        Bstatistics["text"] = "Статистика"
        Bstatistics.place(x=215,y=110,width=155,height=30)
        Bstatistics["command"] = self.statistics_window
        
        
    def choose_education(self, education, education_id):
        
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Выбор образования")
        width=500
        height=300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.resizable(width=False, height=False)
        
        fake_education = tk.Entry(new_window)
        fake_education.place(x=10,y=10,width=0,height=0)
        
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Образование")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=230)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=10)
        
        update_lists("educations", table)
        
        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, education_id, fake_education))
        
        ok_button=tk.Button(new_window)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=10,y=250,width=100,height=30)
        def destroy():
            education['state'] = 'normal'
            education.delete(0, tk.END)
            education.insert(0, fake_education.get())
            education['state'] = 'readonly'
        ok_button["command"] = lambda: (destroy(), new_window.destroy())
    
    def choose_department(self, department, department_id):
        
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Выбор Отделения")
        width=500
        height=300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.resizable(width=False, height=False)
        
        fake_department = tk.Entry(new_window)
        fake_department.place(x=10,y=10,width=0,height=0)
        
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Отделение",)
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=230)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=10)
        
        update_lists("departments", table)
        
        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, department_id, fake_department))
        
        ok_button=tk.Button(new_window)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=10,y=250,width=100,height=30)
        def destroy():
            department['state'] = 'normal'
            department.delete(0, tk.END)
            department.insert(0, fake_department.get())
            department['state'] = 'readonly'
        ok_button["command"] = lambda: (destroy(), new_window.destroy())
    
    def choose_job(self, job, job_id):
        
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Выбор образования")
        width=500
        height=300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.resizable(width=False, height=False)
        
        fake_job = tk.Entry(new_window)
        fake_job.place(x=10,y=10,width=0,height=0)
        
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Должность", "Зарплата")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=160)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=10)
        
        update_lists("job_titles", table)
        
        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, job_id, fake_job))
        
        ok_button=tk.Button(new_window)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=10,y=250,width=100,height=30)
        def destroy():
            job['state'] = 'normal'
            job.delete(0, tk.END)
            job.insert(0, fake_job.get())
            job['state'] = 'readonly'
        ok_button["command"] = lambda: (destroy(), new_window.destroy())
    
    def choose_wbnumber(self, wb_number):
        
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Выбор Трудовой книжки")
        width=500
        height=300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.resizable(width=False, height=False)
        
        fake_wb = tk.Entry(new_window)
        fake_wb.place(x=10,y=10,width=0,height=0)
        __1 = tk.Entry(new_window)
        __1.place(x=10,y=10,width=0,height=0)
        __2 = tk.Entry(new_window)
        __2.place(x=10,y=10,width=0,height=0)
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("Номер ТК", "Ф.И.О.", "Дата рождения")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=160)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=10)
        
        update_records_choose(table)
        
        
        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, fake_wb, __1, __2))
        
        ok_button=tk.Button(new_window)
        ok_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        ok_button["font"] = ft
        ok_button["fg"] = "#000000"
        ok_button["justify"] = "center"
        ok_button["text"] = "OK"
        ok_button.place(x=10,y=250,width=100,height=30)
        def destroy():
            wb_number['state'] = 'normal'
            wb_number.delete(0, tk.END)
            wb_number.insert(0, fake_wb.get())
            wb_number['state'] = 'readonly'
        ok_button["command"] = lambda: (destroy(), new_window.destroy())
    
    
     
    def popup(self, event, tree):
        if iid := tree.identify_row(event.y):
            tree.selection_set(iid)
            return iid
        return None
    
    def statistics_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Статистика")
        width=600
        height=300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        new_window.resizable(width=False, height=False)
        
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("Ф.И.О.", "Количество записей")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=280)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=50)
        
        avg_salary_message=tk.Message(new_window)
        ft = self.font_setting(avg_salary_message, "#333333")
        avg_salary_message["text"] = "Средняя зарплата = "
        avg_salary_message["width"] = 280
        avg_salary_message.place(x=10,y=10,width=280,height=30)
        
        number_people_message=tk.Message(new_window)
        ft = self.font_setting(number_people_message, "#333333")
        number_people_message["text"] = "Количество трудоустроенных = "
        number_people_message["width"] = 280
        number_people_message.place(x=290,y=10,width=280,height=30)
        
        get_avg_salary(avg_salary_message)
        get_number_of_people(number_people_message)
        update_people(table)
        
    
    def results_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Results")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        
        #print(db.view_all())
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("Номер ТК", "Ф.И.О.", "Дата Рождения", "Пол", "Образовние", "Номер записи", "Дата трудоустройства", "Должность", "Зарплата", "Отделение")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=78)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=10)
            
        update_results(table)

        text_search, Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_results(text_search, table)

        
        
    def font_setting(self, object, hex):
        font = tkFont.Font(family='Times',size=10)
        object["font"] = font
        object["fg"] = hex
        object["justify"] = "center"
        return font
    
    def calendar(self, date):
        def set_date():
            date['state'] = 'normal'
            date.delete(0,tk.END)
            date.insert(0,cal.selection_get())
            date['state'] = 'readonly'
            top.destroy()
        
        top = tk.Toplevel(self.root)

        cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2023, month=2, day=5)
        cal.pack(fill="both", expand=True)
        Button(top, text="ok", command=set_date).pack()
        
    def search(self, new_window):
        text_search = tk.Entry(new_window)
        text_search["borderwidth"] = "1px"
        ft = self.font_setting(text_search, "#333333")
        text_search["text"] = "search"
        text_search.place(x=10,y=440,width=200,height=30)
        
        
        Bsearch=tk.Button(new_window)
        Bsearch["bg"] = "#f0f0f0"
        ft = self.font_setting(Bsearch, "#000000")
        Bsearch["text"] = "Поиск"
        Bsearch.place(x=230,y=440,width=200,height=30)
        return  text_search, Bsearch

    def educations_window(self):

        new_window = tk.Toplevel(self.root)
        new_window.title("Образование")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        
        text_message=tk.Message(new_window)
        ft = self.font_setting(text_message, "#333333")
        text_message["text"] = "Образование"
        text_message["width"] = 200
        text_message.place(x=120,y=10,width=200,height=30)
        
        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=600,y=10,width=200,height=200)


        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Образование")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=300)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=120)
        
        
        update_lists("educations", table)
        
        
        id_column=tk.Entry(new_window)
        id_column["borderwidth"] = "1px"
        ft = self.font_setting(id_column, "#333333")
        id_column["text"] = "id_educations"
        id_column.place(x=10,y=30,width=0,height=0)


        value_column=tk.Entry(new_window)
        value_column["borderwidth"] = "1px"
        ft = self.font_setting(value_column, "#333333")
        value_column["text"] = "value_educations"
        value_column.place(x=10,y=30,width=400,height=30)

        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, id_column, value_column))


        new_entry=tk.Button(new_window)
        new_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(new_entry, "#000000")
        new_entry["text"] = "Добавить"
        new_entry.place(x=450,y=30,width=120,height=70)
        new_entry["command"] = lambda: (educations_send_request(value_column, error_message), update_lists("educations",table))


        change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=70,width=200,height=30)
        change_entry["command"] = lambda: (educations_change_request(id_column,value_column, error_message), update_lists("educations", table))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=230,y=70,width=200,height=30)
        remove_entry["command"] = lambda: (educations_delete_request(value_column, error_message), update_lists("educations", table))


        text_search, Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_button("educations", "id_education", text_search, table)
        
        
        

    def persons_window(self):
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Сотрудники")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        
        
        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=10,y=300,width=200,height=200)
        
        text_message=tk.Message(new_window)
        ft = self.font_setting(text_message, "#333333")
        text_message["text"] = "Ф.И.О."
        text_message["width"] = 200
        text_message.place(x=10,y=10,width=100,height=30)

        sex_message=tk.Message(new_window)
        ft = self.font_setting(sex_message, "#333333")
        sex_message["text"] = "Пол"
        sex_message["width"] = 200
        sex_message.place(x=130,y=10,width=100,height=30)
        
        education_message=tk.Message(new_window)
        ft = self.font_setting(education_message, "#333333")
        education_message["text"] = "Образование"
        education_message["width"] = 150
        education_message.place(x=370,y=10,width=150,height=30)
        
        date_message=tk.Message(new_window)
        ft = self.font_setting(date_message, "#333333")
        date_message["text"] = "Дата Рождения"
        date_message["width"] = 200
        date_message.place(x=250,y=10,width=100,height=30)

        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ["Номер ТК", "Ф.И.О.", "Дата рождения", "Пол", "Образование","Education ID"]
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=150)
            table.heading(column,text=column,anchor=tk.CENTER)
        table['displaycolumns'] = table["columns"][:-1]
        table.place(x=10,y=120)
        

        update_persons(table)

        id_column=tk.Entry(new_window)
        id_column["borderwidth"] = "1px"
        ft = self.font_setting(id_column, "#333333")
        id_column["text"] = "id_record"
        id_column.place(x=10,y=30,width=0,height=0)
        
        value_column=tk.Entry(new_window)
        value_column["borderwidth"] = "1px"
        ft = self.font_setting(value_column, "#333333")
        value_column["text"] = "name"
        value_column.place(x=10,y=30,width=100,height=30)

        date_column=tk.Entry(new_window)
        date_column["borderwidth"] = "1px"
        ft = self.font_setting(date_column, "#333333")
        date_column["text"] = "date"
        date_column.place(x=250,y=30,width=100,height=30)
        
        sex_entry = tk.StringVar()
        sex=Combobox(new_window)
        sex['values'] = ["мужской", "женский"]
        sex['textvariable'] = sex_entry
        sex['state'] = 'readonly'
        sex.place(x=130,y=30,width=100,height=30)

        education_id=tk.Entry(new_window)
        education_id["borderwidth"] = "1px"
        ft = self.font_setting(education_id, "#333333")
        education_id["text"] = "kod_eductation"
        education_id.place(x=370,y=30,width=0,height=0)
        
        education=tk.Entry(new_window)
        education["borderwidth"] = "1px"
        ft = self.font_setting(education, "#333333")
        education["text"] = "education"
        education['state'] = 'readonly'
        education.place(x=370,y=30,width=150,height=30)
        
        
        education_choose=tk.Button(new_window)
        education_choose["bg"] = "#f0f0f0"
        ft = self.font_setting(education_choose, "#000000")
        education_choose["text"] = "Выбрать Образование"
        education_choose.place(x=540,y=30,width=150,height=30)
        education_choose["command"] = lambda: self.choose_education(education,education_id)
        
        table.bind('<<TreeviewSelect>>', lambda event: persons_select(table, sex, id_column, value_column, date_column, education, education_id))
        
        
        new_entry=tk.Button(new_window)
        new_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(new_entry, "#000000")
        new_entry["text"] = "Добавить"
        new_entry.place(x=450,y=70,width=200,height=30)
        new_entry["command"] = lambda: (persons_send_request(value_column, date_column, sex_entry, education_id, error_message),
                                        update_persons(table))


        change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=70,width=200,height=30)
        change_entry["command"] = lambda: (persons_change_request(id_column, value_column, date_column, sex_entry, education_id, error_message),
                                           update_persons(table))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=230,y=70,width=200,height=30)
        remove_entry["command"] = lambda: (persons_delete_request(id_column=id_column, error=error_message),
                                           update_persons(table))
        
        view_person=tk.Button(new_window)
        view_person["bg"] = "#f0f0f0"
        ft = self.font_setting(view_person, "#000000")
        view_person["text"] = "Посмотреть"
        view_person.place(x=500,y=350,width=200,height=30)
        view_person["command"] = lambda: self.record_window(wb_number=id_column)
        
        text_search,Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_records(text_search, table)


    def job_window(self):
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Должности")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)

        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=600,y=10,width=200,height=200)

        text_message=tk.Message(new_window)
        ft = self.font_setting(text_message, "#333333")
        text_message["text"] = "Должность"
        text_message["width"] = 200
        text_message.place(x=10,y=10,width=200,height=30)
        
        salary_message=tk.Message(new_window)
        ft = self.font_setting(salary_message, "#333333")
        salary_message["text"] = "Зарплата"
        salary_message["width"] = 100
        salary_message.place(x=230,y=10,width=200,height=30)


        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Должность", "Зарплата")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=200)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=120)
        
        update_lists("job_titles", table)
        
        id_column=tk.Entry(new_window)
        id_column["borderwidth"] = "1px"
        ft = self.font_setting(id_column, "#333333")
        id_column["text"] = "id"
        id_column.place(x=10,y=30,width=0,height=0)


        job_title_column=tk.Entry(new_window)
        job_title_column["borderwidth"] = "1px"
        ft = self.font_setting(job_title_column, "#333333")
        job_title_column["text"] = "job_title_column"
        job_title_column.place(x=10,y=30,width=200,height=30)

        salary_column=tk.Entry(new_window)
        salary_column["borderwidth"] = "1px"
        ft = self.font_setting(salary_column, "#333333")
        salary_column["text"] = "salary_column"
        salary_column.place(x=230,y=30,width=200,height=30)


        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, id_column, job_title_column, salary_column))

        new_entry=tk.Button(new_window)
        new_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(new_entry, "#000000")
        new_entry["text"] = "Добавить"
        new_entry.place(x=450,y=30,width=120,height=70)
        new_entry["command"] = lambda: (jobs_send_request(job_title_column, salary_column, error_message),
                                        update_lists("job_titles", table))


        change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=70,width=200,height=30)
        change_entry["command"] = lambda: (jobs_change_request(id_column,job_title_column, salary_column, error_message),
                                           update_lists("job_titles", table))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=230,y=70,width=200,height=30)
        remove_entry["command"] = lambda: (jobs_delete_request(job_title_column, error_message),
                                           update_lists("job_titles", table))
        
        text_search, Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_button("job_titles", text_search, table)


    def department_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Отделения")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)
        
        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=600,y=10,width=200,height=200)

        text_message=tk.Message(new_window)
        ft = self.font_setting(text_message, "#333333")
        text_message["text"] = "Отделение"
        text_message["width"] = 200
        text_message.place(x=120,y=10,width=200,height=30)


        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Отделение")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=300)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=120)
        
        update_lists("departments", table)


        id_column=tk.Entry(new_window)
        id_column["borderwidth"] = "1px"
        ft = self.font_setting(id_column, "#333333")
        id_column["text"] = "id_departments"
        id_column.place(x=10,y=30,width=0,height=0)


        value_column=tk.Entry(new_window)
        value_column["borderwidth"] = "1px"
        ft = self.font_setting(value_column, "#333333")
        value_column["text"] = "value_departments"
        value_column.place(x=10,y=30,width=400,height=30)

        table.bind('<<TreeviewSelect>>', lambda event: any_select(table, id_column, value_column))


        new_entry=tk.Button(new_window)
        new_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(new_entry, "#000000")
        new_entry["text"] = "Добавить"
        new_entry.place(x=450,y=30,width=120,height=70)
        new_entry["command"] = lambda: (departments_send_request(value_column, error_message),update_lists("departments", table))


        change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=70,width=200,height=30)
        change_entry["command"] = lambda: (departments_change_request(id_column,value_column, error_message),update_lists("departments", table))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=230,y=70,width=200,height=30)
        remove_entry["command"] = lambda: (departments_delete_request(value_column, error_message), update_lists("departments", table))

        text_search, Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_button("departments", text_search, table)
    


    def employed_window(self):
        
        new_window = tk.Toplevel(self.root)
        new_window.title("Записи о трудоустройстве")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)        
        
        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=600,y=10,width=200,height=200)
        

        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("ID", "Номер ТК", "Ф.И.О.", "Номер записи", "Дата трудоустройства",  "Должность",  "Отделение", "ID Должности", "ID Отделения")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=100)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=120)
        table['displaycolumns'] = table["columns"][:-2]

        update_strings(table)

        id_column=tk.Entry(new_window)
        id_column["borderwidth"] = "1px"
        ft = self.font_setting(id_column, "#333333")
        id_column["text"] = "id_string"
        id_column.place(x=10,y=50,width=0,height=0)
        
        record_column=tk.Entry(new_window)
        record_column["borderwidth"] = "1px"
        ft = self.font_setting(record_column, "#333333")
        record_column["text"] = "record"
        record_column.place(x=10,y=50,width=100,height=30)
        record_column["state"] = "readonly"
        
        record_choose=tk.Button(new_window)
        record_choose["bg"] = "#f0f0f0"
        ft = self.font_setting(record_choose, "#000000")
        record_choose["text"] = "Номер ТК"
        record_choose.place(x=10,y=10,width=100,height=30)
        record_choose["command"] = lambda: self.choose_wbnumber(record_column)
        
                
        number_column=tk.Entry(new_window)
        number_column["borderwidth"] = "1px"
        ft = self.font_setting(number_column, "#333333")
        number_column["text"] = "number"
        number_column.place(x=200,y=30,width=0,height=0)

        date_column=tk.Entry(new_window)
        date_column["borderwidth"] = "1px"
        ft = self.font_setting(date_column, "#333333")
        date_column["text"] = "date"
        date_column.place(x=130,y=50,width=100,height=30)
        date_column["state"] = "readonly"
        
        date_button=tk.Button(new_window)
        date_button["bg"] = "#f0f0f0"
        ft = self.font_setting(date_button, "#000000")
        date_button["text"] = "Date Employed"
        date_button.place(x=130,y=10,width=100,height=30)
        date_button["command"] = lambda: self.calendar(date_column)
        
        job=tk.Entry(new_window)
        job["borderwidth"] = "1px"
        ft = self.font_setting(job, "#333333")
        job["text"] = "job"
        job.place(x=250,y=50,width=100,height=30)
        job["state"] = "readonly"
        
        job_entry=tk.Entry(new_window)
        job_entry["borderwidth"] = "1px"
        ft = self.font_setting(job_entry, "#333333")
        job_entry["text"] = "job_entry"
        job_entry.place(x=250,y=50,width=0,height=0)
        
        job_choose=tk.Button(new_window)
        job_choose["bg"] = "#f0f0f0"
        ft = self.font_setting(job_choose, "#000000")
        job_choose["text"] = "Должность"
        job_choose.place(x=250,y=10,width=100,height=30)
        job_choose["command"] = lambda: self.choose_job(job, job_entry)
        
        department_entry=tk.Entry(new_window)
        department_entry["borderwidth"] = "1px"
        ft = self.font_setting(department_entry, "#333333")
        department_entry["text"] = "department"
        department_entry.place(x=370,y=50,width=100,height=30)
        department_entry["state"] = "readonly"
        
        kod_department=tk.Entry(new_window)
        kod_department["borderwidth"] = "1px"
        ft = self.font_setting(kod_department, "#333333")
        kod_department["text"] = "kod_department"
        kod_department.place(x=510,y=30,width=0,height=0)
        
        department_choose=tk.Button(new_window)
        department_choose["bg"] = "#f0f0f0"
        ft = self.font_setting(department_choose, "#000000")
        department_choose["text"] = "Отделение"
        department_choose.place(x=370,y=10,width=100,height=30)
        department_choose["command"] = lambda: self.choose_department(department_entry, kod_department)
        
        view_person=tk.Button(new_window)
        view_person["bg"] = "#f0f0f0"
        ft = self.font_setting(view_person, "#000000")
        view_person["text"] = "Посмотреть"
        view_person.place(x=610,y=10,width=100,height=70)
        view_person["command"] = lambda: self.record_window(wb_number=record_column)
        
        table.bind('<<TreeviewSelect>>', lambda event: strings_select(table, id_column, record_column, number_column, date_column, job, job_entry, department_entry, kod_department))
        
        
        new_entry=tk.Button(new_window)
        new_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(new_entry, "#000000")
        new_entry["text"] = "Добавить"
        new_entry.place(x=490,y=10,width=120,height=70)
        new_entry["command"] = lambda: (strings_send_request(record_column, date_column, job_entry, kod_department, error_message),
                                        update_strings(table))


        """change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=70,width=200,height=30)
        change_entry["command"] = lambda: (strings_change_request(id_column, record_column, number_column, date_column, job_entry, kod_department),
                                           update_lists("strings", table))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=230,y=70,width=200,height=30)
        remove_entry["command"] = lambda: (strings_delete_request(id_column, record_column, number_column, date_column, job_entry, kod_department),
                                           update_lists("strings", table))"""
        
        text_search, Bsearch = self.search(new_window)
        Bsearch["command"] = lambda: search_strings(text_search, table)
        
    def record_window(self, wb_number):
        new_window = tk.Toplevel(self.root)
        new_window.title("Запись")
        width=800
        height=500
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        new_window.geometry(alignstr)        
        
        error_message=tk.Message(new_window)
        ft = self.font_setting(error_message, "#333333")
        error_message["text"] = ""
        error_message["width"] = 200
        error_message.place(x=10,y=300,width=200,height=200)
        
        table = Treeview(new_window)
        table.pack()
        
        table['columns']= ("Номер", "Дата трудоустройства", "Должность", "Зарплата", "Отделение")
        table.column("#0", width=0,  stretch=tk.NO)
        for column in table['columns']:
            table.column(column,anchor=tk.CENTER, width=120)
            table.heading(column,text=column,anchor=tk.CENTER)
        table.place(x=10,y=120)
        
        
        name_column=tk.Entry(new_window)
        name_column["borderwidth"] = "1px"
        ft = self.font_setting(name_column, "#333333")
        name_column["text"] = "name_person"
        name_column.place(x=130,y=10,width=100,height=30)
        
        record_column=tk.Entry(new_window)
        record_column["borderwidth"] = "1px"
        ft = self.font_setting(record_column, "#333333")
        record_column["text"] = "record_p"
        record_column.place(x=10,y=10,width=100,height=30)
        record_column.delete(0, tk.END)
        record_column.insert(0,wb_number.get())
        record_column["state"] = "readonly"

        date_column=tk.Entry(new_window)
        date_column["borderwidth"] = "1px"
        ft = self.font_setting(date_column, "#333333")
        date_column["text"] = "date_p"
        date_column.place(x=250,y=10,width=100,height=70)
        
        sex_message=tk.Message(new_window)
        ft = self.font_setting(sex_message, "#333333")
        sex_message["text"] = ""
        sex_message["width"] = 100
        sex_message.place(x=370,y=10,width=100,height=30)
        
        sex_entry = tk.StringVar()
        sex=Combobox(new_window)
        sex['values'] = ["мужской", "женский"]
        sex['textvariable'] = sex_entry
        sex['state'] = 'readonly'
        sex.place(x=370,y=50,width=100,height=30)

        education_id=tk.Entry(new_window)
        education_id["borderwidth"] = "1px"
        ft = self.font_setting(education_id, "#333333")
        education_id["text"] = "kod_eductation_p"
        education_id.place(x=490,y=30,width=0,height=0)
        
        education=tk.Entry(new_window)
        education["borderwidth"] = "1px"
        ft = self.font_setting(education, "#333333")
        education["text"] = "education_p"
        education['state'] = 'readonly'
        education.place(x=490,y=50,width=150,height=30)
        
        education_choose=tk.Button(new_window)
        education_choose["bg"] = "#f0f0f0"
        ft = self.font_setting(education_choose, "#000000")
        education_choose["text"] = "Выбрать Образование"
        education_choose.place(x=490,y=10,width=150,height=30)
        education_choose["command"] = lambda: self.choose_education(education,education_id)
        
        
        change_entry=tk.Button(new_window)
        change_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(change_entry, "#000000")
        change_entry["text"] = "Изменить"
        change_entry.place(x=10,y=50,width=100,height=30)
        change_entry["command"] = lambda: (change_person(wb_number, name_column, education_id, sex_entry, date_column, error_message, sex_message), 
                                           update_person(table, wb_number, name_column, sex_message, date_column, education, education_id))


        remove_entry=tk.Button(new_window)
        remove_entry["bg"] = "#f0f0f0"
        ft = self.font_setting(remove_entry, "#000000")
        remove_entry["text"] = "Удалить"
        remove_entry.place(x=130,y=50,width=100,height=30)
        remove_entry["command"] = lambda: (persons_delete_request(id_column=wb_number), new_window.destroy())
        
        
        update_person(table, wb_number, name_column, sex_message, date_column, education, education_id)
        
        
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
