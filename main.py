__author__ = 'harsh'
import Tkinter as tk
from pprint import pprint
import json
import sched,time
import random
s=sched.scheduler(time.time,time.sleep)
data2=[]

def all_time():
    with open('data.json') as f:
        data=json.load(f)



    random_key=random.choice(data['words'].keys())
    value=data['words'][random_key].encode('ascii','replace')
    print(random_key,value)

    main=tk.Tk()
    main.call('wm','attributes','.','-topmost',True)
    main.overrideredirect(True)

    main.geometry("+350+300")
    main.configure(background="#A40000")
    close=tk.Button(main,text="Close",width="60",command=main.destroy,relief=tk.SOLID,background="#CC0000",fg="white",font=('Calibri',10,'bold'))
    close.pack(side="top")
    frame_key=tk.Frame(main,width=200,height=100,background="#E34234")
    label_key=tk.Label(frame_key,text=random_key.upper()+' :',font=('Calibri',14,'bold'),background="#A40000",fg="white")
    label_key.pack(side='top')

    frame_key.pack(side="left")

    frame_value=tk.Frame(main,width=400,height=100,highlightthickness=0,bd=2,background="#A40000")
    label_value=tk.Label(frame_value,text=value,wraplength=400,font=('Calibri',12),background="#A40000",fg="white")
    label_value.pack()
    frame_value.pack(side="left")


    main.mainloop()


while 1:

    all_time()
    time.sleep(1000)