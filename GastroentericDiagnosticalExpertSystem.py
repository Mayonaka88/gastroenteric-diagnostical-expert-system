#Importing the tkinter package that is being used to create the GUI
from tkinter import *
from tkinter.font import BOLD

#Here is were the tkinter canvas is created
root = Tk()
root.title("Gastroenteric Diagnostical Expert System")
root.geometry("850x400")
root.resizable(width=FALSE,height=FALSE)
root["bg"]="#202020"


label1 = Label(root, text=" Gastroenteric Diagnostical Expert System",  width="12", height=5,bd=0, background="#202020",foreground='white',font=("Catamaran", 24))
label1.place(x=100,y=5, height=100, width=650)

label2 = Label(root, text="Answer the questionnaire below to get the diagnosis",  width="12", height=5,bd=0, background="#202020",foreground='white',font=("Catamaran", 16))
label2.place(x=125,y=90, height=50, width=600)

label8 = Label(root, text="What part of the region does the pain come from?", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
label8.place(x=125,y=180, height=40, width=600)

score = 0

def printQuestion(choice, button2, button3):
    global score
    if(choice == "yes"):
        score = score + 1
    else:
        score = score + 2
        
        
    match score:
        case 3:
            label8.config(text = "Do you experience any headaches and/or pain in the back and lower sides?")
        case 4:
            label8.config(text = "Kidney Cysts")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 5:
            label8.config(text = "Do you have a lump in your abdomen?")
        case 7:
            label8.config(text = "Do you experience unexplained weight loss and/or loss of appetite?")
        case 8:
            label8.config(text = "Kidney Cancer")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 9:
            label8.config(text = "Have you not experienced any of the following? Extreme pain in your back or side that is not going away or fever and chills")
        case 11:
            label8.config(text = "Urine that smells bad or looks cloudy and/or burning feeling when you urinate?")
        case 12:
            label8.config(text = "Kidney Stones")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 15:
            label8.config(text = "Appendicitis")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 16:
            label8.config(text = "Have you not experienced any of the following? Swelling of one or more lymph glands and/or abnormal sweating and bleeding")
        case 17:
            label8.config(text = "Lymphoma")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 20:
            label8.config(text = "Acute Liver Failure")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 21:
            label8.config(text = "Have you experienced any of the following? Abdominal swelling, yellow discoloration of the skin and eyes")
        case 22:
            label8.config(text = "Liver Cancer")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 26:
            label8.config(text = "Have you experienced large amounts or bloody or dark contents?")
        case 27:
            label8.config(text = "GERD (Gastroesophageal Reflux Disease)")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 28:
            label8.config(text = "Have you experienced any of the following? Bloating or upper abdominal pain or burning or achiness")
        case 29:
            label8.config(text = "Gastritis")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case 30:
            label8.config(text = "Have you experienced any of the following? Excess hunger and thirst, fatigue, frequent urination")
        case 31:
            label8.config(text = "Diabetes")
            button2.destroy()
            button3.destroy()
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)
        case default:
            button2.destroy()
            button3.destroy()
            label8.config(text = "Uncommon Diagnosis")
            label9 = Label(root, text="Refer to a doctor immediately", background="#202020", width="12", height=5,bd=0,foreground='white',font=("Catamaran", 10), wraplength=500, justify="center")
            label9.place(x=125,y=225, height=40, width=600)



def deleteButton(button1, button2, button3, button4, choice):
    global score
    if(choice == "Kidney"):
        score = score + 1
    elif(choice == "Appendix"):
        score = score + 14
    elif(choice == "Liver"):
        score = score + 19
    elif(choice == "Stomach"):
        score = score + 24
        
        
    match score:
        case 1:
            label8.config(text = "Have you not experienced blood in your urine?")
        case 14:
            label8.config(text = "Have you had one or more of stated symptoms? Pain that worsens if you cough, walk, abdominal bloating, and/or flatulence")
        case 19:
            label8.config(text = "Have you had one or more of stated symptoms? Discomfort on your right side and/or vomiting blood")
        case 24:
            label8.config(text = "Have you had one or more of stated symptoms? Difficulty breathing after vomiting and/or pain when eating or swallowing")
        case default:
            label8.config(text = score)
    
    
    
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button2 = Button(root, text="Yes",  width="12", height=5,bd=0, bg="#75C868", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: printQuestion("yes", button2, button3))
    button2.place(x=250,y=300, height=75, width=150)
    button3 = Button(root, text="No",  width="12", height=5,bd=0, bg="#C34848", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: printQuestion("no", button2, button3))
    button3.place(x=450,y=300, height=75, width=150)
    
    


button1 = Button(root, text="Kidney",  width="12", height=5,bd=0, bg="#2d2d2d", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: deleteButton(button1, button2, button3, button4,"Kidney"))
button1.place(x=50,y=300, height=75, width=150)
button2 = Button(root, text="Appendix",  width="12", height=5,bd=0, bg="#2d2d2d", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: deleteButton(button1, button2, button3, button4, "Appendix"))
button2.place(x=250,y=300, height=75, width=150)
button3 = Button(root, text="Liver",  width="12", height=5,bd=0, bg="#2d2d2d", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: deleteButton(button1, button2, button3, button4, "Liver"))
button3.place(x=450,y=300, height=75, width=150)
button4 = Button(root, text="Stomach",  width="12", height=5,bd=0, bg="#2d2d2d", activebackground="white",foreground='#ffffff',font=("Catamaran", 16), command=lambda: deleteButton(button1, button2, button3, button4, "Stomach"))
button4.place(x=650,y=300, height=75, width=150)
root.mainloop()