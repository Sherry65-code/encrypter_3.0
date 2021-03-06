from tkinter import END, Tk, Entry, Text, Button

def encrypt():
    txt = in_w.get()
    txt = txt.lower()
    ans = txt.replace('a','~@@@~').replace('b', '~@@@@@@~').replace('c','~@@@@@@@@@~').replace('d', '~@@@@@@@@@@@@~').replace('e','~@@@@@@@@@@@@@@@~').replace('f','~@@@@@@@@@@@@@@@@@@~').replace('g','~@@@@@@@@@@@@@@@@@@@@~').replace('h','~@@@@@@@@@@@@@@@@@@@@@@@@@~').replace('i','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~').replace('j','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<>@~').replace('k','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[]@@@@~').replace('l','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||@@@@@@@@@@@@@@@~').replace('m', '~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#@@@@@@@~').replace('n','~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^@~').replace('o','~#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######~').replace('p','~$$$$$$$$$$$$$$$$$$$$$$$~').replace('q','~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~').replace('r','~<><><><><><><><>><<>><>><>><<<><><>>>><>~').replace('s','~@@@@@@@@@@@#$$$$$$$$$$$$$@!@@~').replace('t','~@@@@@@@@@@@@@@@@########$$$$$$$$$$$^^^^^^^^^~').replace('u','~``````````````````````````````````````````~').replace('v','~@$#@$#$@#$@#$@#$@#$@#$@#@$@$#@$@#$@#@$@$#@#@$~').replace('w','~@@@@@@@@#$@!#$@#@$@$#@$@$@#@^**&^~').replace('x','~@@@@@@#@@@@@@@@@#@@@@@@#@@@@@@~').replace('y','~@&^&^&^&^&@&^&&@&@^@^&@^&@^&@^&^@~').replace('z','~&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&~').replace(' ','~<<>##$>>>~').replace(',','~^&^&^&^&&^&^^&*<><><<~').replace('.','~<<<<<<<<<<<>>>>>~').replace('?','~$$$$$$$$$$$$$$$$$$$$$$$############~')
    out_w.delete('1.0',END)
    out_w.insert(END, ans)
def decrypt():
    txt = in_w.get()
    # txt = txt.lower()
    ans = txt.replace('~@@@~','a').replace('~@@@@@@~','b').replace('~@@@@@@@@@~','c').replace( '~@@@@@@@@@@@@~','d').replace('~@@@@@@@@@@@@@@@~','e').replace('~@@@@@@@@@@@@@@@@@@~','f').replace('~@@@@@@@@@@@@@@@@@@@@~','g').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@~','h').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~','i').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@<>@~','j').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@[]@@@@~','k').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||@@@@@@@@@@@@@@@~','l').replace( '~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@@#@@@@@@@~','m').replace('~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@^@~','n').replace('~#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######~','o').replace('~$$$$$$$$$$$$$$$$$$$$$$$~','p').replace('~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~','q').replace('~<><><><><><><><>><<>><>><>><<<><><>>>><>~','r').replace('~@@@@@@@@@@@#$$$$$$$$$$$$$@!@@~','s').replace('~@@@@@@@@@@@@@@@@########$$$$$$$$$$$^^^^^^^^^~','t').replace('~``````````````````````````````````````````~','u').replace('~@$#@$#$@#$@#$@#$@#$@#$@#@$@$#@$@#$@#@$@$#@#@$~','v').replace('~@@@@@@@@#$@!#$@#@$@$#@$@$@#@^**&^~','w').replace('~@@@@@@#@@@@@@@@@#@@@@@@#@@@@@@~','x').replace('~@&^&^&^&^&@&^&&@&@^@^&@^&@^&@^&^@~','y').replace('~&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&~','z').replace('~<<>##$>>>~',' ').replace('~^&^&^&^&&^&^^&*<><><<~',',').replace('~<<<<<<<<<<<>>>>>~','.').replace('~$$$$$$$$$$$$$$$$$$$$$$$############~','?')
    out_w.delete('1.0',END)
    out_w.insert(END, ans)

root = Tk()
root.title("Invento Encryptor 3.0")
root.geometry("500x300")
root.resizable(0,0)
root.config(bg='#1b1b1c')
in_w = Entry(root, bg='#51526e',fg='#ffffff', borderwidth=0, highlightthickness=0, relief='flat', width=57)
in_w.place(x=20, y=20)
out_w = Text(root,  borderwidth=0, highlightthickness=0, relief='flat', width=57, height=10, bg='#51526e', fg='#ffffff')
out_w.place(x=20, y=50)
Button(text="Encrypt", fg='#ffffff', bg='#51526e',  borderwidth=0, highlightthickness=0, relief='flat', width=25, height=1, command=encrypt).place(x=20, y=252)
Button(text="Decrypt", fg='#ffffff', bg='#51526e',  borderwidth=0, highlightthickness=0, relief='flat', width=25, height=1, command=decrypt).place(x=255, y=252)
root.mainloop()