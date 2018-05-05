__author__ = 'harsh'
import random
import Tkinter as tk
list=[1,2,3,4,5]

print(random.choice(list))



root = tk.Tk()

v = tk.IntVar()

tk.Label(root, text="""Choose a programming language:""",justify = tk.LEFT,padx = 20).pack()
radio1=tk.Radiobutton(root, text="Python",padx = 20, variable=v, value=1).pack(anchor=tk.W)
radio2=tk.Radiobutton(root, text="Perl",padx = 20, variable=v, value=2).pack(anchor=tk.W)

if(radio1==1)
root.mainloop()