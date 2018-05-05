__author__ = 'harsh'
import Tkinter as tk

from pprint import pprint
import json
import sched,time
import random
s=sched.scheduler(time.time,time.sleep)
data2=[]

def words_mcq_function():
    while 1:


        with open('data.json') as f:
            data=json.load(f)



        random_key=random.choice(data['words'].keys())
        value=data['words'][random_key].encode('ascii','replace')


        #generating random word and key and 3 other options to make a mcq in a list
        mcq_options=[]
        global random_key_for_mcq,value_correct,value_random1,value_random2,value_random3
        value_correct=""
        value_random1=""
        value_random2=""
        value_random3=""



        def word_again():
            global random_key_for_mcq,value_correct
            random_key_for_mcq=random.choice(data['words'].keys())
            if(random_key_for_mcq==random_key):
                word_again()
            else:
                value_correct=data['words'][random_key_for_mcq].encode('ascii','replace')
                def again():
                        global value_random1,value_random3,value_random2
                        value_random1=data['words'][random.choice(data['words'].keys())].encode('ascii','replace')
                        value_random2=data['words'][random.choice(data['words'].keys())].encode('ascii','replace')
                        value_random3=data['words'][random.choice(data['words'].keys())].encode('ascii','replace')
                        if(value_random1==value_correct or value_random2==value_correct or value_random3==value_correct):
                            again()
                        else:
                            print('done')
                            pass

                again()
        word_again()
        mcq_options.extend([value_correct,value_random1,value_random2,value_random3])
        print("mcq options1",mcq_options)
        print(random_key,value)





        main=tk.Tk()
        main.call('wm','attributes','.','-topmost',True)
        main.overrideredirect(True)

        main.geometry("+%d+%d"%(w/2-300,h/2-150))
        main.configure(background="#A40000",highlightthickness=4,highlightcolor="#000000")
        # close=tk.Button(main,text="Close",width=100,command=main.destroy,relief=tk.RAISED,background="#a40000",fg="white",font=('Calibri',10,'bold'))
        # close.pack(side="top")


        #word with meaning part

        main_frame=tk.Frame(main,width=600,height=100,background="#A40000",highlightthickness=2)
        main_frame.pack(side='top',pady=10)
        frame_key=tk.Frame(main_frame,width=200,height=100,background="#a40000")
        label_key=tk.Label(frame_key,text=random_key.upper()+' :',font=('Calibri',14,'bold'),background="#A40000",fg="white")
        label_key.pack(side='top')

        frame_key.pack(side="left")

        frame_value=tk.Frame(main_frame,width=400,height=100,highlightthickness=0,bd=2,background="#A40000")
        label_value=tk.Label(frame_value,text=value,wraplength=400,font=('Calibri',12),background="#A40000",fg="white")
        label_value.pack()
        frame_value.pack(side="left")




        #part of mcq frame



        mcq_frame=tk.Frame(main,width=600,height=100,background="#A40000",highlightthickness=2)
        mcq_frame.pack(side='top',pady=10)

        frame_key=tk.Frame(mcq_frame,width=200,height=100,background="#a40000")
        label_key=tk.Label(frame_key,text=random_key_for_mcq.upper()+' :',font=('Calibri',14,'bold'),background="#A40000",fg="white")
        label_key.pack(side='top')
        frame_key.pack(side="left",padx=30)

        frame_value=tk.Frame(mcq_frame,width=400,height=100,highlightthickness=0,bd=2,background="#A40000")


        # print(random.sample(range(0,4),4)[0],random.sample(range(0,4),4)[1],random.sample(range(0,4),4)[2],random.sample(range(0,4),4)[3])
        # print mcq_options[random.sample(range(0,4),4)[0]]
        # print mcq_options[random.sample(range(0,4),4)[1]]
        # print mcq_options[random.sample(range(0,4),4)[2]]
        # print mcq_options[random.sample(range(0,4),4)[3]]
        random_list=random.sample(range(0,4),4)
        var=tk.IntVar()
        var.set('L')
        verify=tk.StringVar()
        var.set=''

        for i in range(0,4):
            def bind_color(event):
                widget=event.widget
                widget.config(background="#a40000",foreground="#ffffff")
            radio1=tk.Radiobutton(frame_value,indicatoron=0,text=mcq_options[random_list[i]],anchor="w",variable=var,value=i,width=50,background="#a40000",activeforeground="black",activebackground="#a40000",fg="black",font=('Calibri',12),wraplength=400)
            radio1.pack()
            radio1.bind('<B1-Motion>',bind_color)

        def choose(event):
            global count
            widget=event.widget
            widget.config(relief=tk.SUNKEN)
            if(mcq_options[random_list[var.get()]]==value_correct):
                verify.set('Correct')

                main.destroy()

            else:
                verify.set("Incorrect")

        select_button=tk.Button(frame_key,text="Select",width=20,relief=tk.RAISED,background="#a40000",fg="white")
        select_button.pack(side='bottom')
        select_button.bind('<Button-1>',choose)
        label=tk.Label(frame_key,textvariable=verify,background="#a40000",fg="white")
        label.pack(side='bottom')
        # radio1=tk.Radiobutton(frame_value,text=value_random2,width=50,background="#A40000",fg="white",font=('Calibri',12),wraplength=400)
        # radio1.pack()
        # radio1=tk.Radiobutton(frame_value,text=value_random3,width=50,background="#A40000",fg="white",font=('Calibri',12),wraplength=400)
        # radio1.pack()
        # radio1=tk.Radiobutton(frame_value,text=value_correct,width=50,background="#A40000",fg="white",font=('Calibri',12),wraplength=400)
        # radio1.pack()

        frame_value.pack(side="left")



        main.mainloop()

        time.sleep(2)

def only_words_function():
    while 1:
        with open('data.json') as f:
            data=json.load(f)



        random_key=random.choice(data['words'].keys())
        value=data['words'][random_key].encode('ascii','replace')
        print(random_key,value)

        main=tk.Tk()
        main.call('wm','attributes','.','-topmost',True)
        main.overrideredirect(True)

        main.geometry("+%d+%d"%(w/2-200,h/2-100))
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

        time.sleep(2)


main2=tk.Tk()
global h,w
h=main2.winfo_screenheight()
w=main2.winfo_screenwidth()
main2.geometry("+%d+%d"%(w/2-200,h/2-100))
main2.overrideredirect(True)
close=tk.Button(main2,text="Close",width=50,command=main2.destroy,relief=tk.RAISED,fg="black",font=('Calibri',10,'bold'))
close.pack(side="top")

def onlywords():
    main2.destroy()
    only_words_function()

def words_mcq():
    main2.destroy()
    words_mcq_function()

button1=tk.Button(main2,text="Only Words and Meaning",command=onlywords,width=50,background="#a40000",fg="white",font=('Calibri',12,'bold'))
button1.pack()
button2=tk.Button(main2,text="Words with MCQ",command=words_mcq,width=50,background="#a40000",fg="white",font=('Calibri',12,'bold'))
button2.pack()

main2.mainloop()
# while 1:
#
#     all_time()
#     time.sleep(300)
