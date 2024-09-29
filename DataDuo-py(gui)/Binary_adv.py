from tkinter import *
from tkinter import filedialog
import customtkinter
from PIL import Image ,ImageTk
import time
from ctypes import windll
from BlurWindow.blurWindow import blur
import str_binary


root = customtkinter.CTk()

#Screen Geomentry
w = root.winfo_screenwidth()
h = root.winfo_screenheight()


root.geometry("%dx%d+%d+%d" % (w/4 , h , w, 0))

#Screen Background
root.config(bg='cyan')
root.overrideredirect(True)
root.wm_attributes('-transparent' , 'cyan')

#main frame
frame = customtkinter.CTkFrame(root,bg_color='cyan')
frame.place(relheight = 1 ,relwidth =1 ,x = 0 ,y = 0)

back_ground = windll.user32.GetForegroundWindow()
blur(back_ground)

canvas = customtkinter.CTkCanvas(root,bg='cyan')
canvas.place(relheight=1,relwidth=1,x = 0, y= 0)

#Images for buttons(for both frames)
trashi = PhotoImage('Trash.png')
trashi = customtkinter.CTkImage(light_image=Image.open("Trash.png"),size=(20,20))

copyi = PhotoImage('Copy.png')
copyi = customtkinter.CTkImage(light_image=Image.open("Copy.png"),size=(15,15))

folderi = PhotoImage('Folder.png')
folderi = customtkinter.CTkImage(light_image=Image.open("Folder.png"))

down = PhotoImage('down.png')
down = customtkinter.CTkImage(light_image=Image.open("down.png"),size=(15,15))

#Functions for both frames

def close():
    root.destroy()


def delete(place_del_y):
    if place_del_y == delete_text_button.place_info()['y']:
        entry_text.delete(0.0 , 'end')
        text_character.configure(text = f"No.of Character:   ")
        
        
    else:
        entry_binary.delete(0.0 , 'end')
        binary_character.configure(text = f"No.of Character:   ")
    
    


    if len(entry_text.get(0.0,'end')) == 1:
        upload.configure(fg_color='#000000',hover_color = '#808080')
        con.place_forget()

def delete2(place_del_y2):
    if place_del_y2 == delete_text_button2.place_info()['y']:
        entry_text2.delete(0.0 , 'end')
        text_character2.configure(text = f"No.of Character:   ")
        
        
    else:
        entry_binary2.delete(0.0 , 'end')
        binary_character2.configure(text = f"No.of Character:   ")
        
    if len(entry_binary2.get(0.0,'end')) == 1:
        upload2.configure(fg_color='#000000',hover_color = '#808080')
        con2.place_forget()

def copy(place_y):
    if place_y == copy_text_button.place_info()['y']:
        root.clipboard_clear()
        root.clipboard_append(entry_text.get(0.0 , 'end'))
        copy_t = customtkinter.CTkLabel(frame_text_to_binary,text='Copied to clipboard',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        copy_t.place(x = (5*w/32) -63 ,y=305 )
        copy_t.after(3000,copy_t.destroy)

    else :
        root.clipboard_clear()
        root.clipboard_append(entry_binary.get(0.0 , 'end'))
        copy_b = customtkinter.CTkLabel(frame_text_to_binary,text='Copied to clipboard',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        copy_b.place(x = (5*w/32) -100 ,y=605 )
        copy_b.after(3000,copy_b.destroy)

def copy2(place_y):
    if place_y == copy_text_button2.place_info()['y']:
        root.clipboard_clear()
        root.clipboard_append(entry_text2.get(0.0 , 'end'))
        copy_b2 = customtkinter.CTkLabel(frame_binary_to_text,text='Copied to clipboard',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        copy_b2.place(x = (5*w/32) -100 ,y=605 )
        copy_b2.after(3000,copy_b2.destroy)

    else :
        root.clipboard_clear()
        root.clipboard_append(entry_binary2.get(0.0 , 'end'))
        copy_t2 = customtkinter.CTkLabel(frame_binary_to_text,text='Copied to clipboard',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        copy_t2.place(x = (5*w/32) -63 ,y=305 )
        copy_t2.after(3000,copy_t2.destroy)
        

t=0
def save(frame00):
    global t
    t+=1
    if frame00 == str(save_binary_button.master):
        binary_file = open(f'Binary({t}).txt','w')
        binary_file.write(entry_binary.get(0.0,'end'))
        global sav_bin
        sav_bin = customtkinter.CTkLabel(frame_text_to_binary,text=f"Saved as Binary({t})",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        sav_bin.place(x = (5*w/32) -100 ,y=605)
        sav_bin.after(3000,sav_bin.destroy)
    else:
        text_file = open(f'Text({t}).txt','w')
        text_file.write(entry_text2.get(0.0,'end'))
        global sav_txt
        sav_txt = customtkinter.CTkLabel(frame_binary_to_text,text=f"Saved as Text({t})",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
        sav_txt.place(x = (5*w/32) -100 ,y=605)
        sav_txt.after(3000,sav_txt.destroy)

    


def convert_text():
    textb = str(entry_text.get(0.0,'end'))
    binary = str_binary.str_to_binary(textb)
    entry_binary.insert(0.0,binary)
    text_character.configure(text = f"No.of Charecter: {len(entry_text.get(0.0,'end')) - 1}")
    binary_character.configure(text = f"No.of Charecter: {len(entry_binary.get(0.0,'end')) - 1}")

def convert_binary():
    binaryb = str(entry_binary2.get(0.0,'end'))
    text = str_binary.binary_to_str(binaryb)
    entry_text2.insert(0.0,text)
    text_character2.configure(text = f"No.of Charecter: {len(entry_text2.get(0.0,'end')) - 1}")
    binary_character2.configure(text = f"No.of Charecter: {len(entry_binary2.get(0.0,'end')) - 1}")



frame_text_to_binary_x = w/4
frame_text_to_binary_x_after = 0
frame_binary_to_text_x = w/4
frame_binary_to_text_x_after = 0

def bring_frame_binary_to_text():
    global frame_binary_to_text_x
    frame_binary_to_text_x-=5
    if frame_binary_to_text_x > 0 :
        frame_binary_to_text.place_configure(x= frame_binary_to_text_x)

    if frame_binary_to_text_x>0:
        frame_binary_to_text.after(7,bring_frame_binary_to_text)
    else:
        frame_binary_to_text.after_cancel(root)
        frame_binary_to_text_x = w/4

def bring_frame_text_to_binary():
    global frame_text_to_binary_x
    frame_text_to_binary_x-=5
    if frame_text_to_binary_x > 0 :
        frame_text_to_binary.place_configure(x= frame_text_to_binary_x)

    if frame_text_to_binary_x>0:
        frame_text_to_binary.after(7,bring_frame_text_to_binary)
    else:
        frame_text_to_binary.after_cancel(root)
        frame_text_to_binary_x = w/4
    


    

def back_text():
    global frame_text_to_binary_x_after
    frame_text_to_binary_x_after+=5
    if frame_text_to_binary_x_after <500 :
        frame_text_to_binary.place_configure(x= frame_text_to_binary_x_after)

    if frame_text_to_binary_x_after<500 :
        frame_text_to_binary.after(1,back_text)
    else:
        frame_text_to_binary.after_cancel(root)
        frame_text_to_binary_x_after = 0

    if len(entry_text.get(0.0,'end')) > 1:
        entry_text.delete(0.0,'end')
        entry_binary.delete(0.0,'end')
        upload.configure(fg_color='#000000',hover_color = '#808080')
        con.place_forget()
        text_character.configure(text =f"No.of Character:   ")
        binary_character.configure(text =f"No.of Character:   ")

def back_binary():
    global frame_binary_to_text_x_after
    frame_binary_to_text_x_after+=5
    if frame_binary_to_text_x_after <500 :
        frame_binary_to_text.place_configure(x= frame_binary_to_text_x_after)

    if frame_binary_to_text_x_after<500 :
        frame_binary_to_text.after(1,back_binary)
    else:
        frame_binary_to_text.after_cancel(root)
        frame_binary_to_text_x_after = 0

    if len(entry_binary2.get(0.0,'end')) > 1:
        entry_text2.delete(0.0,'end')
        entry_binary2.delete(0.0,'end')
        upload2.configure(fg_color='#000000',hover_color = '#808080')
        con2.destroy()
        text_character2.configure(text =f"No.of Character:   ")
        binary_character2.configure(text =f"No.of Character:   ")
    
        

def uploadf(frame_val):
    if frame_val == upload.master:
        if upload.cget('fg_color') == '#000000':
            directory = filedialog.askopenfilename(title='Select a file',filetypes=(('txt','*.txt'),('All files','*.*')))
            dire = directory.split('/')[-1]
            if len(directory) != 0:
                import codecs
                with codecs.open(str(directory),'r',encoding='utf8') as text_file:
                    text_input = text_file.read()
                entry_text.insert('end' , text_input)
                upload.configure(fg_color='red',hover_color = 'red')
                con.configure(text = f'{dire}')
                con.update()
                con.place_configure(x = (5*w/32) +120 ,y=128)

            else:
                return
        
        else:
            tem = customtkinter.CTkLabel(frame_text_to_binary,text='A file is already uploaded!',width=130,font=('Helvatica',10),text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
            tem.place(x = (5*w/32) -130 ,y=50 )
            tem.after(3000,tem.destroy)

    if frame_val == upload2.master:
        if upload2.cget('fg_color') == '#000000':
            directory2 = filedialog.askopenfilename(title='Select a file',filetypes=(('txt','*.txt'),('All files','*.*')))
            dire2 = directory2.split('/')[-1]
            if len(directory2) != 0:
                import codecs
                with codecs.open(str(directory2),'r',encoding='utf8') as binary_file:
                    binary_input = binary_file.read()
                entry_binary2.insert('end' , binary_input)
                upload2.configure(fg_color='red',hover_color = 'red')
                con2.configure(text = f'{dire2}')
                con2.update()
                con2.place_configure(x = (5*w/32) +120 ,y=128)

            else:
                return
        
        else:
            tem2 = customtkinter.CTkLabel(frame_binary_to_text,text='A file is already uploaded!',width=130,font=('Helvatica',10),text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
            tem2.place(x = (5*w/32) -130 ,y=50 )
            tem2.after(3000,tem2.destroy)
        
    


    

#frame_text_to_binary

frame_text_to_binary = customtkinter.CTkFrame(root,width=(w/4) - 7,bg_color='cyan',fg_color='cyan',height=h)
frame_text_to_binary.place(x = (w/4) , y = 1)

#frame_binary_to_text

frame_binary_to_text = customtkinter.CTkFrame(root,width=(w/4) - 7,bg_color='cyan',fg_color='cyan',height=h)
frame_binary_to_text.place(x = (w/4) , y = 1)


#frame_text_to_binary Buttons
entry_text = customtkinter.CTkTextbox(frame_text_to_binary,width=7*w/32,bg_color='#000000')
entry_text.place(x=w/64 ,y=100)

text_character = customtkinter.CTkLabel(frame_text_to_binary,text=f"No.of Character:   ",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
text_character.place(x=w/64 , y=300)
    
entry_binary = customtkinter.CTkTextbox(frame_text_to_binary,width=7*w/32,bg_color='#000000')
entry_binary.place(x=w/64 ,y=400)

binary_character = customtkinter.CTkLabel(frame_text_to_binary,text=f"No.of Character:   ",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
binary_character.place(x=w/64 , y=600)

convert = customtkinter.CTkButton(frame_text_to_binary,text='↻ Convert',command=convert_text,hover_color='#808080',fg_color='#000000',bg_color='#000000',border_width=2).place(x =9*w/128,y=340)

delete_text_button = customtkinter.CTkButton(frame_text_to_binary,text='',image=trashi,command=lambda: delete(delete_text_button.place_info()['y']),bg_color='#1d1e1e',fg_color='#1d1e1e',hover_color='#808080',width=25)
delete_text_button.place(x = 13*w/64 -3 ,y = 300)

delete_binary_button = customtkinter.CTkButton(frame_text_to_binary,text='',image=trashi,command=lambda: delete(delete_binary_button.place_info()['y']),bg_color='#1d1e1e',fg_color='#1d1e1e',hover_color='#808080',width=25)
delete_binary_button.place(x = 13*w/64 -3 ,y = 600)

copy_text_button = customtkinter.CTkButton(frame_text_to_binary,text='',image=copyi,bg_color='#1d1e1e',command=lambda: copy(copy_text_button.place_info()['y']),fg_color='#1d1e1e',hover_color='#808080',width=35)
copy_text_button.place(x = 13*w/64 - 37,y = 300)

copy_binary_button = customtkinter.CTkButton(frame_text_to_binary,text='',image=copyi,bg_color='#1d1e1e',command=lambda: copy(copy_binary_button.place_info()['y']),fg_color='#1d1e1e',hover_color='#808080',width=35)
copy_binary_button.place(x = 13*w/64 - 37,y = 600)

save_binary_button = customtkinter.CTkButton(frame_text_to_binary,text='',image=down,bg_color='#1d1e1e',command=lambda: save(str(save_binary_button.master)),fg_color='#1d1e1e',hover_color='#808080',width=35)
save_binary_button.place(x = 13*w/64 - 71,y = 600)

back_frame01 = customtkinter.CTkButton(frame_text_to_binary,text="◄",width=45,command=back_text,fg_color='#000000',bg_color='#000000',hover_color='#808080')
back_frame01.place(x = 20,y = 10)

text_label = customtkinter.CTkLabel(frame_text_to_binary,text="Text input",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e').place(x=w/64 , y=85)

closeb = customtkinter.CTkButton(frame_text_to_binary,text="x",command=close,width=45,fg_color='#000000',bg_color='#000000',hover_color='red').place(x = 3*w/16,y = 10)

upload = customtkinter.CTkButton(frame_text_to_binary,text='Upload',text_color="#FFFFFF",command=lambda: uploadf(upload.master),image=folderi,width=30,fg_color='#000000',bg_color='#000000',hover_color='#808080')
upload.place(x = 5*w/32 ,y=50)

con = customtkinter.CTkLabel(frame_text_to_binary,text=f'Unknown',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
con.place(x = w/4 ,y=85)

#frame_binary_to_text Button
entry_binary2 = customtkinter.CTkTextbox(frame_binary_to_text,width=7*w/32,bg_color='#000000')
entry_binary2.place(x=w/64 ,y=100)

binary_character2 = customtkinter.CTkLabel(frame_binary_to_text,text=f"No.of Character:   ",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
binary_character2.place(x=w/64 , y=300)
    
entry_text2 = customtkinter.CTkTextbox(frame_binary_to_text,width=7*w/32,bg_color='#000000')
entry_text2.place(x=w/64 ,y=400)

text_character2 = customtkinter.CTkLabel(frame_binary_to_text,text=f"No.of Character:   ",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
text_character2.place(x=w/64 , y=600)

convert2 = customtkinter.CTkButton(frame_binary_to_text,text='↻ Convert',command=convert_binary,hover_color='#808080',fg_color='#000000',bg_color='#000000',border_width=2).place(x =9*w/128,y=340)

delete_binary_button2 = customtkinter.CTkButton(frame_binary_to_text,text='',image=trashi,command=lambda: delete2(delete_binary_button2.place_info()['y']),bg_color='#1d1e1e',fg_color='#1d1e1e',hover_color='#808080',width=25)
delete_binary_button2.place(x = 13*w/64 -3 ,y = 300)

delete_text_button2 = customtkinter.CTkButton(frame_binary_to_text,text='',image=trashi,command=lambda: delete2(delete_text_button2.place_info()['y']),bg_color='#1d1e1e',fg_color='#1d1e1e',hover_color='#808080',width=25)
delete_text_button2.place(x = 13*w/64 -3 ,y = 600)

copy_binary_button2 = customtkinter.CTkButton(frame_binary_to_text,text='',image=copyi,bg_color='#1d1e1e',command=lambda: copy2(copy_binary_button2.place_info()['y']),fg_color='#1d1e1e',hover_color='#808080',width=35)
copy_binary_button2.place(x = 13*w/64 - 37,y = 300)

copy_text_button2 = customtkinter.CTkButton(frame_binary_to_text,text='',image=copyi,bg_color='#1d1e1e',command=lambda: copy2(copy_text_button2.place_info()['y']),fg_color='#1d1e1e',hover_color='#808080',width=35)
copy_text_button2.place(x = 13*w/64 - 37,y = 600)

save_text_button2 = customtkinter.CTkButton(frame_binary_to_text,text='',image=down,bg_color='#1d1e1e',command=lambda: save(str(save_text_button2.master)),fg_color='#1d1e1e',hover_color='#808080',width=35)
save_text_button2.place(x = 13*w/64 - 71,y = 600)

back_frame02 = customtkinter.CTkButton(frame_binary_to_text,text="◄",width=45,command=back_binary,fg_color='#000000',bg_color='#000000',hover_color='#808080')
back_frame02.place(x = 20,y = 10)

binary_label = customtkinter.CTkLabel(frame_binary_to_text,text="Binary input",font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e').place(x=w/64 , y=85)

closeb = customtkinter.CTkButton(frame_binary_to_text,text="x",command=close,width=45,fg_color='#000000',bg_color='#000000',hover_color='red').place(x = 3*w/16,y = 10)

upload2 = customtkinter.CTkButton(frame_binary_to_text,text='Upload',text_color="#FFFFFF",command=lambda: uploadf(upload2.master),image=folderi,width=30,fg_color='#000000',bg_color='#000000',hover_color='#808080')
upload2.place(x = 5*w/32 ,y=50)

con2 = customtkinter.CTkLabel(frame_binary_to_text,text=f'Unknown',font=('Helvatica',10),height=15,width=70,text_color='#FFFFFF',bg_color='#1d1e1e',fg_color='#1d1e1e')
con2.place(x = w/4 ,y=85)


#Buttons in root

button01 = customtkinter.CTkButton(canvas,text="Text to Binary",command=bring_frame_text_to_binary,fg_color='#000000',bg_color='#000000',border_width=1,text_color='#FFFFFF',height=40,hover_color="#808080")
button01.place(x = 9*w/128,y= 120)
button02 = customtkinter.CTkButton(canvas,text="Binary to Text",command=bring_frame_binary_to_text,fg_color='#000000',bg_color='#000000',border_width=1,text_color='#FFFFFF',height=40,hover_color="#808080")
button02.place(x= 9*w/128 ,y= 240)
button03 = customtkinter.CTkButton(canvas,text="Image to Binary",fg_color='#000000',bg_color='#000000',border_width=1,text_color='#FFFFFF',height=40,hover_color="#808080")
button03.place(x = 9*w/128,y= 360)
button04 = customtkinter.CTkButton(canvas,text="Binary to Image",fg_color='#000000',bg_color='#000000',border_width=1,text_color='#FFFFFF',height=40,hover_color="#808080")
button04.place(x= 9*w/128 ,y= 480)
closeb = customtkinter.CTkButton(canvas,text="x",command=close,width=45,fg_color='#000000',bg_color='#000000',hover_color='red',border_width=2).place(x = 3*w/16,y = 10)


root.mainloop()

