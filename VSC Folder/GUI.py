import tkinter as Tk
import customtkinter
import SNICKRS as SN
import datetime as dt


class Snickr_Sheet:
    def __init__(self, cow):
        try:
            result = SN.find_cow(cow)
        except Exception as e:
            print(e)

        self.selected_label = None
        self.labels_list = []

        self.root = customtkinter.CTk()
        self.root.geometry(
            f"{self.root.winfo_screenmmwidth()}x{self.root.winfo_screenmmheight()}"
        )
        self.root.after(0, lambda: self.root.state("zoomed"))
        self.root.title("SNICKRS Sheet")

        self.editframe = customtkinter.CTkFrame(
            self.root, fg_color="black", width=100, height=800
        )
        self.editframe.pack(side="left", expand=True)
        self.editframe.configure(width=self.root.winfo_screenwidth() * 0.15)
        self.editframe.configure(height=self.root.winfo_screenheight())

        self.topframe = customtkinter.CTkFrame(self.root, fg_color="white")
        self.topframe.pack(side="top", expand="True")
        self.topframe.configure(width=self.root.winfo_screenwidth() * 0.85)
        self.topframe.configure(height=self.root.winfo_screenheight() * 0.33)

        self.mainframe = customtkinter.CTkScrollableFrame(
            master=self.root,
            fg_color="white",
            width=1600,
            height=600,
            border_width=0,
            label_text="Breeding & Milk Cycles",
            label_font=("Arial", 18),
        )
        self.mainframe.pack(side="bottom")
        self.mainframe.configure(width=self.root.winfo_screenwidth() * 0.85)
        self.mainframe.configure(height=self.root.winfo_screenheight() * 0.67)

        self.root.bind("<Escape>", self.close_window)

        try:
            IDFrame(self.topframe, result, self)
            GenealogyFrame(self.topframe, result, self)
            VaccDateFrame(self.topframe, result, self)
            EditFrame(self.editframe, self)
        except Exception as e:
            print(e)
        try:
            NotesBox = customtkinter.CTkLabel(
                self.topframe,
                width=self.topframe.cget("width") * 0.25,
                height=self.topframe.cget("height"),
                fg_color="white",
                anchor="nw",
                text=result[-2],
            )
            NotesBox.pack(side="left")
            NotesBox.bind("<Button-1>", self.label_clicked)
            self.labels_list.append(NotesBox)
        except Exception as e:
            print(e)
        try:
            self.season1 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][1:11], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle1 = MilkCycleFrame(
                self.mainframe, result=result[-1][11:55], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season2 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][55:65], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle2 = MilkCycleFrame(
                self.mainframe, result=result[-1][65:109], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season3 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][109:119], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle3 = MilkCycleFrame(
                self.mainframe, result=result[-1][119:163], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season4 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][163:173], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle4 = MilkCycleFrame(
                self.mainframe, result=result[-1][173:217], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season5 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][217:227], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle5 = MilkCycleFrame(
                self.mainframe, result=result[-1][227:271], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season6 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][271:281], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle6 = MilkCycleFrame(
                self.mainframe, result=result[-1][281:325], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season7 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][325:335], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle7 = MilkCycleFrame(
                self.mainframe, result=result[-1][335:379], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season8 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][379:389], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle8 = MilkCycleFrame(
                self.mainframe, result=result[-1][389:433], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season9 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][433:443], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle9 = MilkCycleFrame(
                self.mainframe, result=result[-1][443:487], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season10 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][487:497], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle10 = MilkCycleFrame(
                self.mainframe, result=result[-1][497:541], snickrs_instance=self
            )
        except:
            pass
        try:
            self.season11 = BreedingSeasonFrame(
                self.mainframe, result=result[-1][541:551], snickrs_instance=self
            )
        except:
            pass
        try:
            self.cycle11 = MilkCycleFrame(
                self.mainframe, result=result[-1][551:595], snickrs_instance=self
            )
        except:
            pass
        self.root.mainloop()

    def get_label_index(self, target_label):
        for i, label in enumerate(self.labels_list):
            if label.cget("text") == target_label.cget("text"):
                return i
        return -1

    def close_window(self, event):
        SN.save_data(self.labels_list)
        self.root.destroy()

    def label_clicked(self, event):
        self.selected_label = event.widget

    def update_data(self):
        index = self.get_label_index(self.selected_label)
        new_data = self.edit_entry.get()
        old_data = self.selected_label.cget("text")
        if "\n" in old_data:
            old_data = old_data.split("\n")[0]
            self.selected_label.config(text=f"{old_data}\n{new_data}")
        else:
            self.selected_label.config(text=f"{new_data}")

        self.labels_list.insert(index, self.selected_label)
        self.labels_list.pop(index + 1)

        self.selected_label = None


class Main_Menu:
    def __init__(self):
        def Snickr_Sheet_init():
            if cow_num_entry.get():
                Snickr_Sheet(cow_num_entry.get())
            elif calf_entry.get():
                Snickr_Sheet(calf_entry.get())
            else:
                pass

        def add_cow():
            SN.add_cow(calf_entry.get(), mama_entry.get(), dob_entry.get())
            Snickr_Sheet_init()

        self.root = customtkinter.CTk()
        self.root.geometry("400x300")
        self.root.title("Main Menu")
        self.mainframe = customtkinter.CTkFrame(self.root, fg_color="black")
        self.mainframe.pack(fill="both", expand=True)
        self.root.bind("<Escape>", self.close_window)

        cow_num_entry = customtkinter.CTkEntry(
            self.mainframe,
            width=200,
            height=50,
        )
        cow_num_entry.place(x=0, y=100)
        cow_data_button = customtkinter.CTkButton(
            self.mainframe,
            width=200,
            height=100,
            text_color="white",
            text="View Cow Data",
            command=Snickr_Sheet_init,
        )
        cow_data_button.place(x=0, y=0)

        calf_entry = customtkinter.CTkEntry(
            self.mainframe,
            width=100,
            height=50,
            placeholder_text="Calf's Number",
        )
        mama_entry = customtkinter.CTkEntry(
            self.mainframe,
            width=100,
            height=50,
            placeholder_text="Mama's Number",
        )

        dob_entry = customtkinter.CTkEntry(
            self.mainframe,
            width=200,
            height=50,
            placeholder_text="Date of Birth",
        )

        dob_entry.insert(0, dt.datetime.now().strftime("%m/%d/%Y"))

        calf_entry.place(x=200, y=100)
        mama_entry.place(x=300, y=100)
        dob_entry.place(x=200, y=150)

        new_cow_button = customtkinter.CTkButton(
            self.mainframe,
            width=200,
            height=100,
            text_color="white",
            text="Add New Cow",
            command=add_cow,
        )
        new_cow_button.place(x=200, y=0)

        self.root.mainloop()

    def close_window(self, event):
        self.root.destroy()


class IDFrame:
    def __init__(self, parent, result, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent,
            width=parent.cget("width") * 0.3,
            height=parent.cget("height"),
            fg_color="white",
        )
        self.frame.pack(side="right")

        NumberBox = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height") * 0.33,
            text=f"Cow Number\n{result[0]}",
            font=("Arial", 18),
            fg_color="white",
        )
        NumberBox.grid(row=1, column=1)
        NumberBox.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.insert(0, NumberBox)

        tattoo_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height") * 0.34,
            fg_color="white",
            text=f"Tattoo Number\n{result[1]}",
            font=("Arial", 18),
        )
        tattoo_label.grid(row=2, column=1)
        tattoo_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(tattoo_label)

        bday_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"Birthday\n{result[2]}",
            font=("Arial", 18),
        )
        bday_label.grid(row=3, column=1)
        bday_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(bday_label)


class GenealogyFrame:
    def __init__(self, parent, result, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent,
            width=parent.cget("width") * 0.3,
            height=parent.cget("height"),
            fg_color="white",
        )
        self.frame.pack(side="right")

        breed_frame = customtkinter.CTkFrame(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height"),
            fg_color="white",
        )
        breed_frame.grid(row=1, column=1, columnspan=4)

        holstein_label = customtkinter.CTkLabel(
            breed_frame,
            width=self.frame.cget("width") * 0.33,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"Holstein %\n{result[3]}",
            font=("Arial", 18),
        )
        holstein_label.grid(row=1, column=1)
        holstein_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(holstein_label)

        montebeliarde_label = customtkinter.CTkLabel(
            breed_frame,
            width=self.frame.cget("width") * 0.34,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"Monte %\n{result[4]}",
            font=("Arial", 18),
        )
        montebeliarde_label.grid(row=1, column=2)
        montebeliarde_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(montebeliarde_label)

        swedish_label = customtkinter.CTkLabel(
            breed_frame,
            width=self.frame.cget("width") * 0.33,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"Sw. Red %\n{result[5]}",
            font=("Arial", 18),
        )
        swedish_label.grid(row=1, column=3)
        swedish_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(swedish_label)

        breed_frame.grid(row=1, column=1, columnspan=4)

        dam_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.34,
            fg_color="white",
            text=f"Dam\n{result[9]}",
            font=("Arial", 18),
        )
        dam_label.grid(row=2, column=4)
        dam_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grdam_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.34,
            fg_color="white",
            text=f"GrDam\n{result[8]}",
            font=("Arial", 18),
        )
        grdam_label.grid(row=2, column=3)
        grdam_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grgrdam_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.34,
            fg_color="white",
            text=f"GrGrDam\n{result[7]}",
            font=("Arial", 18),
        )
        grgrdam_label.grid(row=2, column=2)
        grgrdam_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grgrgrdam_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.34,
            fg_color="white",
            text=f"GrGrGrDam\n{result[6]}",
            font=("Arial", 18),
        )
        grgrgrdam_label.grid(row=2, column=1)
        grgrgrdam_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(grgrgrdam_label)
        snickrs_instance.labels_list.append(grgrdam_label)
        snickrs_instance.labels_list.append(grdam_label)
        snickrs_instance.labels_list.append(dam_label)
        sire_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"Sire\n{result[13]}",
            font=("Arial", 18),
        )
        sire_label.grid(row=3, column=4)
        sire_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grsire_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"GrSire\n{result[12]}",
            font=("Arial", 18),
        )
        grsire_label.grid(row=3, column=3)
        grsire_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grgrsire_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"GrGrSire\n{result[11]}",
            font=("Arial", 18),
        )
        grgrsire_label.grid(row=3, column=2)
        grgrsire_label.bind("<Button-1>", snickrs_instance.label_clicked)

        grgrgrsire_label = customtkinter.CTkLabel(
            self.frame,
            width=self.frame.cget("width") * 0.25,
            height=self.frame.cget("height") * 0.33,
            fg_color="white",
            text=f"GrGrGrSire\n{result[10]}",
            font=("Arial", 18),
        )
        grgrgrsire_label.grid(row=3, column=1)
        grgrgrsire_label.bind("<Button-1>", snickrs_instance.label_clicked)
        snickrs_instance.labels_list.append(grgrgrsire_label)
        snickrs_instance.labels_list.append(grgrsire_label)
        snickrs_instance.labels_list.append(grsire_label)
        snickrs_instance.labels_list.append(sire_label)


class VaccDateFrame:
    def __init__(self, parent, result, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent,
            width=parent.cget("width") * 0.15,
            height=parent.cget("height"),
            fg_color="white",
        )
        self.frame.pack(side="left")

        labels = [
            ("Vacc", "Date"),
            ("VS6+Som", result[14]),
            ("Covenix8", result[15]),
            ("VS6+VLS", result[16]),
            ("EndovacD", result[17]),
            ("Calfhood", result[18]),
        ]

        for i, (text, date) in enumerate(labels):
            label = customtkinter.CTkLabel(
                self.frame,
                width=self.frame.cget("width") * 0.3,
                height=self.frame.cget("height") / 6,
                fg_color="white",
                text=f"{text}",
                font=("Arial", 18),
            )
            label.grid(row=i + 2, column=1)
            label.bind("<Button-1>", snickrs_instance.label_clicked)

            date_label = customtkinter.CTkLabel(
                self.frame,
                width=self.frame.cget("width") * 0.70,
                height=self.frame.cget("height") / 6,
                fg_color="white",
                text=f"{date}",
                font=("Arial", 18),
            )
            date_label.grid(row=i + 2, column=2)
            date_label.bind("<Button-1>", snickrs_instance.label_clicked)
            if i > 1:
                snickrs_instance.labels_list.append(date_label)


class BreedingSeasonFrame:
    def __init__(self, parent, result, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent,
            width=parent.cget("width"),
            height=100,
            fg_color="grey",
            bg_color="grey",
        )
        self.frame.pack()

        labels = [
            ("Bred To", result[0]),
            ("Date", result[1]),
            ("Bred To", result[2]),
            ("Date", result[3]),
            ("Bred To", result[4]),
            ("Date", result[5]),
            ("Due", result[6]),
            ("Dried Date", result[7]),
            ("Calf", result[8]),
            ("Date", result[9]),
        ]

        for i, (text, data) in enumerate(labels):
            label = customtkinter.CTkLabel(
                self.frame,
                width=self.frame.cget("width") * 0.1,
                height=80,
                fg_color="grey",
                text=f"{text}\n{data}",
                font=("Arial", 18),
            )
            label.grid(row=1, column=i + 1)
            label.bind("<Button-1>", snickrs_instance.label_clicked)
            snickrs_instance.labels_list.append(label)


class MilkCycleFrame:
    def __init__(self, parent, result, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent, width=parent.cget("width"), height=100, fg_color="white"
        )
        self.frame.pack()

        for i in range(0, 44, 2):
            month_label = customtkinter.CTkLabel(
                self.frame,
                width=(self.frame.cget("width") * 0.045),
                height=70,
                fg_color="white",
                text=f"{result[i]}\n{result[i + 1]}\n",
                font=("Arial", 18),
            )
            month_label.grid(row=1, column=int((i)) + 1)
            month_label.bind("<Button-1>", snickrs_instance.label_clicked)
            snickrs_instance.labels_list.append(month_label)


class EditFrame:
    def __init__(self, parent, snickrs_instance):
        self.frame = customtkinter.CTkFrame(
            parent, width=parent.cget("width"), height=parent.cget("height")
        )
        self.frame.pack()

        self.Edit_Button = customtkinter.CTkButton(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height") * 0.15,
            command=(snickrs_instance.update_data),
        )
        self.Edit_Button.pack(side="top")

        self.Edit_Entry = customtkinter.CTkEntry(
            self.frame,
            width=self.frame.cget("width"),
            height=self.frame.cget("height") * 0.10,
            placeholder_text="Enter new info here!",
        )
        self.Edit_Entry.pack(side="top")
        snickrs_instance.edit_entry = self.Edit_Entry


if __name__ == "__main__":
    Main_Menu()
