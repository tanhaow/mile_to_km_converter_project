from tkinter import *

def miles_to_km():
    try:
        miles = float(miles_input.get())
    except ValueError:
        km_result_label.config(text="Invalid input")
        return
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles To Kilometer Converter")
window.config(padx=50, pady=20)

# pop the window at the center of the screen
x = (window.winfo_screenwidth() - window.winfo_width()) // 2
y = (window.winfo_screenheight() - window.winfo_height()) // 2
window.geometry(f"+{x}+{y}")


# widgets

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)





window.mainloop()
