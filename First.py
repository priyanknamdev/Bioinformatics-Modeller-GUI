import tkinter as tk
#import subprocess


def write_slogan():
	print("Dreams are not which you see while in your sleep, Dreams are those which not let you Sleep! ")

root = tk.Tk()
root.title("Bioinformatics")


#logo = tk.PhotoImage(file="icon1.png")
#text1 = tk.Label(root,  image=logo).pack(side="top")

#text2 = tk.Label(root,compound=tk.RIGHT,text="Hi! Welcome to Bioinformatics.",padx=200, pady=20, fg="#FF8A80", bg="#46799B",  font="Helvetica 18 bold ", image=logo ).pack(side="top")

#def buttonFunction():
	#subprocess.Popen(['C:/Program Files (x86)/Internet Explorer/iexplore.exe'])

#button = tk.button(root, text="Click This", fg="black", bg="lightgrey", padx=10 , pady=10 , font="Helvetica 16 bold", command=buttonFunction())
#button.pack()

title = "Hi! Welcome to Bioinformatics."
msgBox = tk.Message(root, text=title)	
msgBox.pack(side="top")
msgBox.configure(aspect=2000, bg="#424242", fg="#FF8A80", font="Helvetica 18 bold ")

w = tk.Canvas(root, width=2000, height=1)
w.pack()
w.create_line(2000, 2000, 20000, 20000, fill="black")


footerMessage = "Developed solely by Neha, Shivam, Priyank. Under the guidance of Mr. Rakesh Joshi."
footerMsgBox = tk.Message(root, text= footerMessage)
footerMsgBox.pack(side="bottom")
footerMsgBox.configure(font="times 10 italic", aspect = 2000)

# frame = tk.Frame(root)
# frame.configure(bg="#424242")
# frame.pack()

label = tk.Label(root, text= "Click to Open a PDB file : ", bg="#424242", fg="#E0E0E0", font="Times 14 italic bold", relief="flat", width=25).pack()

button2 = tk.Button(root, text="Open", font="Times 14 italic", bg="#757575", command=write_slogan, width=25)
button2.pack()

root.configure(bg="#424242")
root.geometry("950x600")
#root.resizable(0,0)






root.mainloop()


