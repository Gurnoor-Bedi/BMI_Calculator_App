from tkinter import *
window=Tk()
window.title("BMI Calculator.")
window.geometry("500x500")
window.configure(bg="lightcyan")
def bmical(w,h):
    w=int(weight_entry.get())
    h=int(height_entry.get())
    bmi=w/(h/100)**2
    bmi=round(bmi,1)
    name=user_name.get()
    result_label.destroy()
    message=""
    if bmi<=18.5:
        message="You are underweight."
    elif bmi>18.5 and bmi<=24.9:
        message= "You are healthy."
    elif bmi>24.9 and bmi<=29.9:
        message= "You are overweight."
    elif bmi>29.9:
        message= "You are obese."
    else:
        message="Something went wrong"
    output_message=Label(result_frame, text=f"{name} : Your BMI is : {bmi}\n {message}", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
    output_message.place(x=20,y=100)
    output_message.pack()

app=Label(window, text="BMI Calculator", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
app.place(x=850,y=20)
name_label=Label(window, text="Your name: ", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
name_label.place(x=20,y=90)
user_name=Entry(window, textvariable="", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
user_name.place(x=200,y=90)
weight_entry=Label(window, text="Your weight: ", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
weight_entry.place(x=20,y=160)
weight_entry=Entry(window, textvariable="", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
weight_entry.place(x=200,y=160)
height_entry=Label(window, text="Your height: ", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
height_entry.place(x=20,y=230)
height_entry=Entry(window, textvariable="", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
height_entry.place(x=200,y=230)
calculate_button=Button(window, text="Calculate BMI", bg="lightcyan", fg="black", font=("Arial",20,"bold"),command=lambda: bmical(weight_entry.get(),height_entry.get()))
calculate_button.place(x=220,y=330)
result_frame=LabelFrame(window, text="", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=30,y=500)

result_label=Label(result_frame, text="", bg="lightcyan", fg="black", font=("Arial",20,"bold"))
result_label.pack()
result_label.place(x=20,y=20)

window.mainloop()
