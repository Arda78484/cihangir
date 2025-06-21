from tkinter import *
import mission1
import mission2
from mathexclusive import * 

def startmission1():
    lat1 = float(e1.get('1.0', 'end-1c'))
    lon1 = float(e3.get('1.0', 'end-1c'))
    lat2 = float(e2.get('1.0', 'end-1c'))
    lon2 = float(e4.get('1.0', 'end-1c'))
    det = int(er.get('1.0', 'end-1c'))
    rad = float(ed.get('1.0', 'end-1c'))

    mission1.startmission((lat1,lon1), (lat2,lon2), rad, det)
    
def startmission2():
    lat1 = float(e5.get('1.0', 'end-1c'))
    lon1 = float(e7.get('1.0', 'end-1c'))
    lat2 = float(e6.get('1.0', 'end-1c'))
    lon2 = float(e8.get('1.0', 'end-1c'))
    lat3 = float(e9.get('1.0', 'end-1c'))
    lon3 = float(e11.get('1.0', 'end-1c'))
    lat4 = float(e10.get('1.0', 'end-1c'))
    lon4 = float(e12.get('1.0', 'end-1c'))
    tur = float(er2.get('1.0', 'end-1c'))
    rad = float(ed2.get('1.0', 'end-1c'))
    dis = float(em2.get('1.0', 'end-1c'))

    mission2.startmission((lat1, lon1,), (lat2, lon2), (lat3, lon3), (lat4, lon4), tur, rad, dis)

root = Tk()
root.title("UAV Mission Starter")

Label(root, text="First Pylon Latitude").grid(row=0, column=0)
Label(root, text="First Pylon Longitude").grid(row=0, column=3)
Label(root, text="Second Pylon Latitude").grid(row=1, column=0)
Label(root, text="Second Pylon Longitude").grid(row=1, column=3)
Label(root, text="Detail Level").grid(row=2, column=0)
Label(root, text="Turning Radius").grid(row=2, column=3)
# e1 = Entry(root)
# e2 = Entry(root)
e1 = Text(root,height=1, width=15)
e2 = Text(root,height=1, width=15)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
# e3 = Entry(root)
# e4 = Entry(root)
e3 = Text(root,height=1, width=15)
e4 = Text(root,height=1, width=15)
e3.grid(row=0, column=4)
e4.grid(row=1, column=4)
er = Text(root, height=1, width=15)
ed = Text(root, height=1, width=15)
er.grid(row=2, column=1)
ed.grid(row=2, column=4)

button1 = Button(root, 
                   text="Start Mission 1", 
                   command=startmission1,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=20,
                   wraplength=200)

button1.grid(row=3, column=2)

Label(root, text="First Pylon Latitude").grid(row=4, column=0)
Label(root, text="First Pylon Longitude").grid(row=4, column=3)
Label(root, text="Second Pylon Latitude").grid(row=5, column=0)
Label(root, text="Second Pylon Longitude").grid(row=5, column=3)
Label(root, text="First Area Latitude").grid(row=6, column=0)
Label(root, text="First Area Longitude").grid(row=6, column=3)
Label(root, text="Second Area Latitude").grid(row=7, column=0)
Label(root, text="Second Area Longitude").grid(row=7, column=3)
Label(root, text="Angle Between").grid(row=8, column=0)
Label(root, text="Turning Radius").grid(row=8, column=3)
Label(root, text="Distance Between").grid(row=9, column=0)
e5 = Text(root,height=1, width=15)
e6 = Text(root,height=1, width=15)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7 = Text(root,height=1, width=15)
e8 = Text(root,height=1, width=15)
e7.grid(row=4, column=4)
e8.grid(row=5, column=4)
e9 = Text(root,height=1, width=15)
e10 = Text(root,height=1, width=15)
e9.grid(row=6, column=1)
e10.grid(row=7, column=1)
e11 = Text(root,height=1, width=15)
e12 = Text(root,height=1, width=15)
e11.grid(row=6, column=4)
e12.grid(row=7, column=4)
ed2 = Text(root, height=1, width=15)
ed2.grid(row=8, column=1)
er2 = Text(root, height=1, width=15)
er2.grid(row=8, column=4)
em2 = Text(root, height=1, width=15)
em2.grid(row=9, column=1)

button1 = Button(root, 
                   text="Start Mission 2", 
                   command=startmission2,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   width=20,
                   wraplength=200)

button1.grid(row=10, column=2)

root.mainloop()