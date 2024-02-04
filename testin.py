view_person=tk.Button(new_window)
        view_person["bg"] = "#f0f0f0"
        ft = self.font_setting(view_person, "#000000")
        view_person["text"] = "Отделение"
        view_person.place(x=370,y=10,width=100,height=30)
        view_person["command"] = lambda: self.choose_department(department_entry, kod_department)