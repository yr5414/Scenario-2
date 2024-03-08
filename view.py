import tkinter as tk
from tkinter import *

class ChatWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Window")

        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_area = Text(root, yscrollcommand=self.scrollbar.set)
        self.chat_area.pack()

        self.entry_msg = Entry(root, width=50)
        self.entry_msg.pack()

        self.send_button = tk.Button(root, text="Send", command=self.send_msg)
        self.send_button.pack(side="right", ipadx=20, ipady=10, padx=10, pady=10)

        self.scrollbar.config(command=self.chat_area.yview)

    def send_msg(self):
        msg = self.entry_msg.get()
        self.chat_area.insert(END, 'You: ' + msg + '\n')
        self.entry_msg.delete(0, 'end')
        
    def receive_msg(self, msg):
        self.chat_area.insert(END, 'Bot: ' + msg + '\n')

root = tk.Tk()

w = Label(root, text="Hi, this is a bot that initializes your anonymous appointment")
w.config(bg = 'lightgreen', font = ('arial', 12))
w.pack()

ChatWindow(root)

root.mainloop()