import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to_do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My T0-D0 App", layout =[[label], [input_box, add_button]])
window.read()
print("done ")
window.close()
