import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import webbrowser


class ChatWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Window")

        w = Label(root, text="Anonymous Health Query App")
        w.config(bg="lightgreen", font=("arial", 12))
        w.pack()

        self.tab_control = ttk.Notebook(root)
        self.appointment = ttk.Frame(self.tab_control)
        self.chat = ttk.Frame(self.tab_control)
        self.map = ttk.Frame(self.tab_control)
        self.tab_control.add(self.appointment, text="Appointment")
        self.tab_control.add(self.chat, text="Chat")
        self.tab_control.add(self.map, text="Map")
        self.tab_control.pack(expand=1, fill=BOTH)

        # appointment window
        self.cal = Calendar(
            self.appointment, selectmode="day", year=2024, month=3, day=11
        )
        self.cal.pack(fill=BOTH, expand=True, pady=50, padx=50)

        self.date_button = tk.Button(
            self.appointment, text="Confirm Date", command=self.select_date
        )
        self.date_button.pack(after=self.cal, pady=10)

        self.date = Label(self.appointment, text="")
        self.date.pack(after=self.cal, pady=10)

        # Chat window
        self.scrollbar = Scrollbar(self.chat)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_area = Text(self.chat, yscrollcommand=self.scrollbar.set)
        self.chat_area.pack(
            expand=True, fill=BOTH, padx=50, pady=20, ipadx=100, ipady=100
        )

        self.entry_msg = Entry(self.chat, width=50)
        self.entry_msg.pack()

        self.var = tk.IntVar()
        self.send_button = tk.Button(
            self.chat, text="Send", command=lambda: self.var.set(1)
        )
        self.send_button.pack(
            side="right", ipadx=20, ipady=10, padx=10, pady=10, after=self.entry_msg
        )
        self.root.bind("<Return>", lambda event: self.var.set(1))

        self.scrollbar.config(command=self.chat_area.yview)

        self.chat_area.tag_config("user", background="lightgreen", foreground="black")

        self.map_button = tk.Button(self.map, text="Open Map", command=self.open_map)
        self.map_button.pack()

    def open_map(self):
        map_url = "https://www.google.com/maps"
        webbrowser.open(map_url)

    def select_date(self):
        self.date_selected = self.cal.get_date()
        self.date.config(text="Date selected: " + self.date_selected)

    def input_msg(self):
        self.send_button.wait_variable(self.var)
        msg = self.entry_msg.get()
        self.chat_area.insert(END, "You: " + msg + "\n", "user")
        self.entry_msg.delete(0, "end")
        return msg
    
    def on_link_click(self, event):
        webbrowser.open_new('https://www.google.com/search?q=report&oq=report&gs_lcrp=EgZjaHJvbWUyDAgAEEUYORixAxiABDIKCAEQABixAxiABDIMCAIQABhDGIAEGIoFMgcIAxAAGIAEMhAIBBAAGIMBGLEDGIAEGIoFMgcIBRAAGIAEMgYIBhBFGDwyBggHEEUYPTIGCAgQRRg90gEHNzYyajBqMagCALACAA&sourceid=chrome&ie=UTF-8')

    def link_to_report(self, msg):
        self.chat_area.insert(END, msg, "link")
        self.chat_area.insert(END, "\n")
        self.chat_area.tag_config("link", foreground="blue", underline=True)
        self.chat_area.tag_bind("link", "<Button-1>", self.on_link_click)

    def output_msg(self, msg):
        self.chat_area.insert(END, "Bot: " + msg + "\n")