from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
root=Tk()
root.title('photo resizer')
root.geometry('1000x600')
root.resizable(False,False)
file_name=""
width=0
height=0
height_data=0
width_data=0
save_file_info=""
image_file2=""
bottom_label=""
def show_image_func():
    global bottom_label
    window=Toplevel(root)
    window.title("actual image")
    img=ImageTk.PhotoImage(Image.open(file_name))
    l=Label(window,image=img)
    l.pack()
    window.mainloop()
def save_picture_func():
    global save_file_info
    global image_file2
    save_file_info=filedialog.asksaveasfilename(title="save your file",filetypes=(("jpeg file","*.jpg"),("png files","*.png")))
    image_file2.save(save_file_info)
    bottom_label['text']="Image saved in location of "+save_file_info+"---in dimensions "+str(width)+"x"+str(height)
def save_file():
    global save_file_info
    save_picture=Button(middile_frame,text="save your resized image",font=("arial",20,"bold"),fg="white",bg="#f702b6",width=40,command=save_picture_func)
    save_picture.grid(row=3,column=0)
def convert_image():
    global file_name
    global height
    global width
    global bottom_label
    global image_file2
    height=int(height_data.get())
    width=int(width_data.get())
    image_file=Image.open(file_name)
    image_file2=image_file.resize((width,height),Image.NEAREST)
    bottom_label["text"]="image has been converted to "+str(width)+"x"+str(height)
    save_file()
def show_height_width():
    global height_data
    global width_data
    height_label=Label(middile_frame,text="Height:",font=('arial',20,'bold'))
    height_label.grid(row=0,column=0)
    height_data=Entry(middile_frame,font=('arial',20,'bold'))
    height_data.grid(row=0,column=1,padx=20)
    width_label=Label(middile_frame,text="Width:",font=('arial',20,'bold'))
    width_label.grid(row=1,column=0,pady=20)
    width_data=Entry(middile_frame,font=('arial',20,'bold'))
    width_data.grid(row=1,column=1,padx=20)
    convert_btn=Button(middile_frame,text="covert that image",font=('arial',20,'bold'),fg="red",bg="yellow",command=convert_image)
    convert_btn.grid(row=2,column=0,pady=30)
    image_show_button=Button(middile_frame,text="show actual image",font=('arial',20,'bold'),fg="red",bg="yellow",command=show_image_func)
    image_show_button.grid(row=2,column=1,pady=30)
def ask_for_file():
    global file_name
    global bottom_label
    file_name=filedialog.askopenfilename(title="select file",filetypes=(("jpeg file","*.jpg"),("png files","*.png")))
    image_height_width=Image.open(file_name)
    height_width_of_image="width:"+str(image_height_width.size[0])+"    height:"+str(image_height_width.size[1])
    bottom_label=Label(bottom_frame,text=height_width_of_image,font=('arial',20,'bold'))
    bottom_label.grid(row=0,column=0)
    show_height_width()
top_frame=Frame(root)
top_frame.pack(side=TOP)
ask_button=Button(top_frame,text="open file",fg="white",bg="black",height=1,width=30,font=('arial',20,'bold'),relief=RAISED,command=ask_for_file)
ask_button.grid(row=0,column=0,pady=30)
middile_frame=Frame(root)
middile_frame.pack(side=TOP)
bottom_frame=Frame(root)
bottom_frame.pack(side=BOTTOM)

root.mainloop()