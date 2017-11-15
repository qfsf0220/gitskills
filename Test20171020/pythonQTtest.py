import  Tkinter as tk

class App(object):
    def __init__(self,master):
        self.com    = tk.Button(master,text="hello",command=self.say_hello)
        self.com.pack(side=tk.BOTTOM)
    def say_hello(self):
        print("helooo..boss")

root =tk.Tk()
root.title('this is window')
root.geometry('300x200')

app=App(root)
root.mainloop()