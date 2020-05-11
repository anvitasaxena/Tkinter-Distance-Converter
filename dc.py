import tkinter as tk
from tkinter import ttk
#from windows import set_dpi_awareness

try:
    from ctypes import windll
    windll.schore.SetProcessDpiAwareness()
except:
    pass

#set_dpi_awareness()

root=tk.Tk()
root.title("Distance Converter")

metres_value=tk.StringVar()
feet_value= tk.StringVar()

def calculate_feet(*args):
    try:
        metres=float(metres_value.get())
        feet=metres*3.28084
        #print(f"{metres} metres is equal to {feet:.3f}feet")
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass
    
root.columnconfigure(0,weight=1)

main=ttk.Frame(root, padding=(30,15))
main.grid()

metres_label=ttk.Label(main, text="Meters:")
metres_input=ttk.Entry(main, width=10, textvariable=metres_value)
feet_label=ttk.Label(main, text="Feet:")
feet_display=ttk.Label(main,textvariable=  feet_value)
calc_button=ttk.Button(main,text="Calculate",command= calculate_feet)


metres_label.grid(row=0,column=0,sticky="W",padx=5,pady=5)
metres_input.grid(row=0,column=1,sticky="EW",padx=5,pady=5)

metres_input.focus()

feet_label.grid(row=1,column=0,sticky="W",padx=5,pady=5)
feet_display.grid(row=1,column=1,sticky="EW",padx=5,pady=5)


calc_button.grid(row=2,column=0,columnspan=2,sticky="EW",padx=5,pady=5)

"""for child in main.winfo_children():
    child.grid_configure(padx=15,pady=15)"""
    
root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)
root.mainloop()
