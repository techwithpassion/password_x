
import random , smtplib ,time
from tkinter import messagebox
import tkinter as tk
from tkinter import *

root = ''

def start():
    global root
    root = Tk()
    root.title('Password-X : Home')
    root.iconbitmap('rk.ico')
    root.geometry('700x400')

    def Password_of_my_name():
        global root
        root.destroy()
        root = Tk()
        root.title('Password-X : Name Generator')
        root.geometry('700x400')

        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`~!@#$%^&*()-_=+[{]}\|;:\'",<.>/?'
        with open('passw.txt','r') as t:
            key = t.read()

        def decode(code):
            final = ''
            key_index = 0
            alternate = 0

            for j, i in enumerate(code):

                if j != 0 and j == int(key[0]) + key_index*int(key[0]) + key_index:
                    key_index += 1
                    continue

                if i not in alpha:
                    final += i
                    continue

                if i == ' ':
                    final += ' '
                    continue

                index = alpha.index(i)

                if (index == len(alpha) - 1) and (alternate%2==1):
                    change = 'A'
                else:
                    if alternate%2==1:
                        change = alpha[index + 1]
                    else:
                        change = alpha[index - 1]
                    
                final += change

                alternate += 1

            return final

        def encode(code):
            final = ''
            key_index = 0
            alternate = 0

            for j, i in enumerate(code): # j= indexing of a  i= value of a

                if j != 0 and j%int(key[0]) == 0:
                    final += key[key_index%len(key)] # IMPORTANT ALGORITHEM...(it's like looping some range of integer.)
                    key_index += 1

                if i not in alpha:
                    final += i
                    continue

                if i == ' ':
                    final += ' '
                    continue
                
                index = alpha.index(i)

                if (index == len(alpha) - 1) and (alternate%2==0):
                    change = 'A'
                else:
                    if alternate%2==0:
                        change = alpha[index + 1]
                    else:
                        change = alpha[index - 1]
                    
                final += change

                alternate += 1

            return final

    

        def name_password():

            my_name = name.get()
            name_gen = encode(my_name)
            Label(root, text = f'Password of your name is' , font=('calibri',10,'bold'),foreground = 'yellow' , background = 'black').place(x = 100 , y = 100)
            box_area = Text(root , width = 40 , height = 1)
            box_area.place(x =250 , y = 100)
            box_area.insert(tk.END, f'{name_gen}')
            
            

            def copy():
                root.clipboard_append(name_gen)
                Label(root, text = "Successfully Copied To Clipboard!" , background = 'white', foreground = 'green'  ).place(x= 500 , y =70)
            
            root.bind('<Control-Key-c>', copy)    
            Button(root, text = 'Copy' , command = copy ).place(x = 450 , y = 70)
        def back():
            global root
            root.destroy()
            start()

        Label(root, text = 'Generate your desirable password !', font = ('calibri',10,'bold')).place(x=5,y=5)

        name = StringVar()
        Label(root, text = 'Enter your name' ).place( x = 20 , y = 50)
        box = Entry(root, textvariable = name, width =25 , font = ('calibri',15,'bold'))
        box.place(x = 20 , y = 70)
        Button(root, text = 'Generate my password', command = name_password ).place(x = 300 , y = 70)
        Button(root, text = 'Back' , command = back).place(x= 300 , y = 100)
        root.mainloop()
        
    # my_frame = Frame(root)
    # my_frame.pack(pady = 5)

    # create text box
    # my_textbox = Text(my_frame, width=100 , height = 20 , font =('helvetica',10), selectbackground ='yellow' , selectforeground = 'black' , undo =True , )
    # my_textbox.pack()

    def self_generate():
        global root
        root.destroy()
        root = Tk()
        root.title('Password-X : Self generator')
        root.geometry('400x700')

        def generate():

            check()

            alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            alpha_lower = alpha_upper.lower()

            num  = "1234567890"

            symbols = "!@#$%^&*()_"

            # abcd are the booleans 

            gen = ""

            if a.get() == 1:
                gen += alpha_upper

            if b.get()== 1:
                gen += alpha_lower

            if c.get()==1:
                gen += num

            if d.get()==1:
                gen += symbols

            yaxis = 400

            string = ''
            for x in range(int(password_amount.get())):
                password = "".join(random.sample(gen, int(password_length.get())))
                string += f'password number {x+1} is {password}'
                string += '\n\n'
                yaxis = yaxis + 30

            text_area = Text(root , yscrollcommand = True , width = 40 , height = 15)
            text_area.place(x = 20, y= 380)
            text_area.insert(tk.END , f'{string}')
def passway():
    root.tk()
    root.destroy()
    root = Tk()
    root.title('Password-X : passway gate')
    root.geometry('800x700')
    

        def check():
            if int(password_length.get()) == '':
                messagebox.showwarning('WARNING!!!','length should be greater than 0')
            elif int(password_amount.get()) == '':
                messagebox.showwarning('WARNING!!!','length should be greater than 0')
            elif int(password_length.get()) > 73:
                messagebox.showwarning('WARNING!!!','length should be lesser than 73')
            else:
                pass

        password_length = StringVar()
        Label(root, text = f'How Long do you want the characer to be! (must be less than 73) ').place(x=50 , y = 30)
        Entry(root, textvariable = password_length , validatecommand = check).place(x = 50, y= 60 )

        password_amount = StringVar()
        Label(root, text = f'how many password do you want !').place(x =50 , y = 90)
        Entry(root, textvariable = password_amount , validatecommand = check).place(x = 50 , y = 120)   

        a = IntVar()
        C1 =  Checkbutton(root , text = 'Does it Contain Uppercase! (Stage 1)' , variable = a)
        C1.place(x = 50 , y = 150)

        b = IntVar()
        Checkbutton(root , text = 'Does it Contain Lowercase! (Stage 2)' , variable = b).place(x = 50 , y = 200)

        c = IntVar()
        Checkbutton(root , text = 'Does it Contain Numeric Values! (Stage 3)' , variable = c).place(x =50 , y = 250)

        d = IntVar()
        Checkbutton(root, text = 'Does it Contain Symbols! (Stage 4)' , variable = d).place(x=50, y=300)

        Button(root, text = 'Submit',command = generate).place(x=50 , y = 350)

        root.mainloop()

    Label(root, text = 'Generate your desirable password !', font = ('calibri',10,'bold')).place(x=5,y=5)

    Button(root, text = 'Generate a password of my name!' , command = Password_of_my_name , font = ('helvatica',15,'bold')).place(x = 20 , y = 50)

    Button(root, text = 'Generate Password for required condition!' , command = self_generate, font = ('helvatica',15,'bold')).place(x = 20 , y = 120)
    
    Button(root, text = 'Auto generate passway !' , command = passway, font = ('helvatica',15,'bold')).place(x = 20 , y = 190)

    root.mainloop()

if __name__ == '__main__':
    start()
