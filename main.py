import tkinter as tk
from tkinter import ttk

selection_data = {'Father': ['Noble', 'Merchant', 'Warrior', 'Hunter', 'Nomad', 'Thief'],
                  'Early life': ['Page', 'Apprentice', 'Assistant', 'Urchin', 'Steppe Child'],
                  'Adulthood': ['Squire/Lady in Waiting', 'Troubadour', 'Student', 'Peddler', 'Smith', 'Poacher'],
                  'Reason for adventuring': ['Revenge', 'Loss', 'Wanderlust', 'Forced out', 'Money']
                  }

class Character:
    def __init__(self):
        self.attributes = {'STR': 5, 'AGI': 5, 'INT': 4, 'CHA': 5}
        self.proficiencies = {'One-handed weapons': 42,
                                             'Two-handed weapons': 18,
                                             'Polearms': 20,
                                             'Archery': 15,
                                             'Crossbows': 17,
                                             'Throwing': 19}
        self.skills = {'Riding': 1, 'Leadership': 1}
        self.equipment = None




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.character = Character()

        self.title("Warband Character Planer")
        self.geometry("800x350")
        self.resizable(True, True)

        self.attribute_label = ttk.Label(self, text="", font=("Helvetica", 12))
        self.proficiencies_label = ttk.Label(self, text="", font=("Helvetica", 10))
        self.skill_label = ttk.Label(self, text="", font=("Helvetica", 10))
        self.equipment_label = ttk.Label(self, text="", font=("Helvetica", 10))


        gender_label = ttk.Label(self, text="Gender")
        father_label = ttk.Label(self, text="Who was your father")
        childhood_label = ttk.Label(self, text="Childhood")
        adulthood_label = ttk.Label(self, text="Adulthood")
        reason_label = ttk.Label(self, text="The reason you came here")
        gender_label.grid(row=0, column=0)
        father_label.grid(row=1, column=0)
        childhood_label.grid(row=2, column=0)
        adulthood_label.grid(row=3, column=0)
        reason_label.grid(row=4, column=0)


        self.gender = tk.StringVar()
        self.gender_selection = ttk.Combobox(self, textvariable=self.gender, values=['Male', 'Female'], state="readonly")
        self.gender_selection.grid(row=0, column=1)
        self.gender_selection.bind("<<ComboboxSelected>>", self.gender_selected)

        self.father = tk.StringVar()
        self.father_selection = ttk.Combobox(self, textvariable=self.father, values=selection_data['Father'], state="disabled")
        self.father_selection.grid(row=1, column=1)
        self.father_selection.bind("<<ComboboxSelected>>", self.display_data)
        self.father_dissabled_label = ttk.Label(self, text="Select gender first")
        self.father_dissabled_label.grid(row=1, column=1)

        self.childhood = tk.StringVar()
        self.childhood_selection = ttk.Combobox(self, textvariable=self.childhood, values=selection_data['Early life'], state="readonly")
        self.childhood_selection.grid(row=2, column=1)
        self.childhood_selection.bind("<<ComboboxSelected>>", self.display_data)

        self.adulthood = tk.StringVar()
        self.adulthood_selection = ttk.Combobox(self, textvariable=self.adulthood, values=selection_data['Adulthood'], state="disabled")
        self.adulthood_selection.grid(row=3, column=1)
        self.adulthood_selection.bind("<<ComboboxSelected>>", self.display_data)
        self.adulthood_dissabled_label = ttk.Label(self, text="Select gender first")
        self.adulthood_dissabled_label.grid(row=3, column=1)

        self.reason = tk.StringVar()
        self.reason_selection = ttk.Combobox(self, textvariable=self.reason, values=selection_data['Reason for adventuring'], state="readonly")
        self.reason_selection.grid(row=4, column=1)
        self.reason_selection.bind("<<ComboboxSelected>>", self.display_data)


        self.attribute_label.grid(row=5, column=0, columnspan=1)
        self.proficiencies_label.grid(row=6, column=0, columnspan=1)
        self.skill_label.grid(row=0, column=2, rowspan=7, sticky='n', padx=5, pady=5)
        self.equipment_label.grid(row=0, column=3, rowspan=7, sticky='n', padx=5, pady=5)

        self.display_data()

    def gender_selected(self, event=None):
        self.father_selection.config(state="readonly")
        self.adulthood_selection.config(state="readonly")
        self.father_dissabled_label.config(text="")
        self.adulthood_dissabled_label.config(text="")
        self.display_data()


    def display_data(self, event=None):
        def add_skills(skills, new_skills):
            for key in new_skills:
                if key in skills:
                    skills[key] += new_skills[key]
                else:
                    skills[key] = new_skills[key]
            return skills

        STR = 5
        AGI = 5
        INT = 4
        CHA = 5

        one_handed = 42
        two_handed = 18
        polearms = 20
        archery = 15
        xbow = 17
        throw = 19

        skills = {"Riding": 1, "Leadership": 1}

        gender = self.gender.get()
        father = self.father.get()
        childhood = self.childhood.get()
        adulthood = self.adulthood.get()
        reason = self.reason.get()

        if gender == 'Male':
            STR += 1
            CHA += 1
        elif gender == 'Female':
            AGI += 1
            INT += 1

        if father == 'Noble':
            if gender == 'Male':
                INT += 1
                CHA += 2
                one_handed += 2
                two_handed += 15
                polearms += 21
                skills = add_skills(skills, {"Power Strike": 1, "Weapon Master": 1, "Riding": 1, "Tactics": 1, "Leadership": 1})
            elif gender == 'Female':
                INT += 2
                CHA += 1
                one_handed += 14
                polearms += 7
                skills = add_skills(skills, {"Riding": 2, "Wound Treatment": 1, "First Aid": 1, "Leadership": 1})
        elif father == 'Merchant':
            INT += 2
            CHA += 1
            two_handed += 15
            polearms += 26
            skills = add_skills(skills, {"Riding": 1, "Inventory Management": 1, "Leadership": 1, "Trade": 2})
        elif father == 'Warrior':
            STR += 1
            AGI += 1
            CHA += 1
            one_handed += 2
            two_handed += 23
            polearms += 33
            throw += 15
            skills = add_skills(skills, {"Ironflesh": 1, "Power Strike": 1, "Weapon Master": 1, "Trainer": 1, "Leadership": 1})
        elif father == 'Hunter':
            STR += 1
            AGI += 2
            two_handed += 15
            polearms += 7
            archery += 49
            skills = add_skills(skills, {"Power Draw": 1, "Athletics": 1, "Tracking": 1, "Path-finding": 1, "Spotting": 1})
        elif father == 'Nomad':
            if gender == 'Male':
                STR += 1
                AGI += 1
                INT += 1
                one_handed += 2
                polearms += 7
                archery += 49
                throw += 15
                skills = add_skills(skills, {"Power Draw": 1, "Riding": 2, "Horse Archery": 1, "Path-finding ": 1})
            elif gender == 'Female':
                STR += 1
                AGI += 1
                INT += 1
                one_handed += 5
                polearms += 7
                archery += 32
                throw += 7
                skills = add_skills(skills, {"Riding": 2, "Path-finding": 1, "Wound Treatment": 1, "First Aid": 1})
        elif father == 'Thief':
            AGI += 3
            one_handed += 14
            polearms += 7
            throw += 31
            skills = add_skills(skills, {"Power Throw": 1, "Athletics": 2, "Looting": 1, "Inventory Management": 1})

        if childhood == 'Page':
            STR += 1
            CHA += 1
            one_handed += 8
            polearms += 3
            skills = add_skills(skills, {"Power Strike": 1, "Persuasion": 1})
        elif childhood == 'Apprentice':
            STR += 1
            INT += 1
            skills = add_skills(skills, {"Engineer": 1, "Trade": 1})
        elif childhood == 'Assistant':
            INT += 1
            CHA += 1
            skills = add_skills(skills, {"Inventory Management": 1, "Trade": 1})
        elif childhood == 'Urchin':
            AGI += 1
            INT += 1
            one_handed += 8
            throw += 7
            skills = add_skills(skills, {"Looting": 1, "Spotting": 1})
        elif childhood == 'Steppe Child':
            STR += 1
            AGI += 1
            archery += 24
            skills = add_skills(skills, {"Power Throw": 1, "Horse Archery": 1})

        if adulthood == 'Squire/Lady in Waiting':
            if gender == 'Male':
                STR += 1
                AGI += 1
                one_handed += 23
                two_handed += 38
                polearms += 22
                archery += 16
                xbow += 16
                throw += 14
                skills = add_skills(skills, {"Power Strike": 1, "Weapon Master": 1, "Riding": 1, "Leadership": 1})
            elif gender == 'Female':
                INT += 1
                CHA += 1
                one_handed += 8
                xbow += 24
                skills = add_skills(skills, {"Riding": 1, "Wound Treatment": 1, "Persuasion": 2})
        elif adulthood == 'Troubadour':
            CHA += 2
            one_handed += 19
            xbow += 16
            skills = add_skills(skills, {"Weapon Master": 1, "Path-finding": 1, "Persuasion": 1, "Leadership": 1})
        elif adulthood == 'Student':
            INT += 2
            one_handed += 15
            xbow += 32
            skills = add_skills(skills, {"Weapon Master": 1, "Wound Treatment": 1, "Surgery": 1, "Persuasion": 1})
        elif adulthood == 'Peddler':
            INT += 1
            CHA += 1
            polearms += 11
            skills = add_skills(skills, {"Riding": 1, "Path-finding": 1, "Inventory Management": 1, "Trade": 1})
        elif adulthood == 'Smith':
            STR += 1
            INT += 1
            one_handed += 11
            skills = add_skills(skills, {"Weapon Master": 1, "Tactics": 1, "Engineer": 1, "Trade": 1})
        elif adulthood == 'Poacher':
            STR += 1
            AGI += 1
            polearms += 7
            archery += 57
            skills = add_skills(skills, {"Power Draw": 1, "Athletics": 1, "Tracking": 1, "Spotting": 1})

        if reason == 'Revenge':
            STR += 2
            skills = add_skills(skills, {"Power Strike": 1})
        elif reason == 'Loss':
            CHA += 2
            skills = add_skills(skills, {"Ironflesh": 1})
        elif reason == 'Wanderlust':
            AGI += 2
            skills = add_skills(skills, {"Path-finding": 1})
        elif reason == 'Forced out':
            STR += 1
            INT += 1
            skills = add_skills(skills, {"Weapon Master": 1})
        elif reason == 'Money':
            AGI += 1
            INT += 1
            skills = add_skills(skills, {"Looting": 1})

        attributes_message = (f"Attributes:\n"
                   f"STR: {STR}\n"
                   f"AGI: {AGI}\n"
                   f"INT: {INT}\n"
                   f"CHA: {CHA}")

        proficiency_message = (f"Proficiencies:\n"
                               f"One-handed weapons: {one_handed}\n"
                               f"Two-handed weapons: {two_handed}\n"
                               f"Polearms: {polearms}\n"
                               f"Archery: {archery}\n"
                               f"Crossbows: {xbow}\n"
                               f"Throwing: {throw}")

        skill_list = []
        for key in skills:
            skill_list.append(f"{key}: {skills[key]}")
        skills_message = ("Skills:\n" + "\n".join(skill_list))

        equipment_message = ""

        self.attribute_label.config(text=attributes_message)
        self.proficiencies_label.config(text=proficiency_message)
        self.skill_label.config(text=skills_message)
        self.equipment_label.config(text=equipment_message)


if __name__ == "__main__":
    app = App()
    app.mainloop()