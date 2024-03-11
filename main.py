from view import ChatWindow
import tkinter as tk
from model import Questions

root = tk.Tk()
app = ChatWindow(root)


def chat():
    app.output_msg(Questions.Bot["greet"])
    app.output_msg(Questions.Bot["info"])
    Questions.Patient.update({"info": app.input_msg()})
    app.output_msg(Questions.Bot["general"])
    Questions.Patient.update({"general_descrip": app.input_msg()})

    valid = False
    while not valid:
        app.output_msg(Questions.Bot["pick"])
        Questions.Patient.update({"choice": app.input_msg()})

        if "physical" in Questions.Patient["choice"]:
            app.output_msg(Questions.Bot["physical"])
            Questions.Patient.update({"physical_answ": app.input_msg()})
            valid = True
        elif "mental" in Questions.Patient["choice"]:
            app.output_msg(Questions.Bot["Mental"])
            Questions.Patient.update({"Mental_answ": app.input_msg()})
            valid = True
        else:
            app.output_msg("I can't understand your response. Please try again.")

    app.output_msg(Questions.Bot["pre_report"])
    app.output_msg(Questions.Bot["final_report"])
    app.link_to_report("Link to your report")


while True:
    chat()
    app.output_msg("")
    app.output_msg("starting a new chat...")
    app.output_msg("")

    root.update_idletasks()
    root.update()
