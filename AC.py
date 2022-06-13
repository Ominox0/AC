
__version__= "1.02"

def Quit(num="None"):
    if num=="None":
        exit()
    else:
        exit(int(num))
def show(file):
    import os
    os.system(f"attrib -h {file}")
    del os
    
def hide(file):
    import os
    os.system(f"attrib +h {file}")
    del os
def loop():
    try:
        while True:pass;
    except KeyboardInterrupt:pass;
def exist(file,hiden=False):
    if hiden==True:
        show(file)
        try:
            open(file,"r")
            hide(file)
            return True
        except FileNotFoundError:return False;
    if hiden==False:
        try:
            open(file,"r")
            return True
        except FileNotFoundError:return False;
    
def help():
    print("""functions:
    -Quit(num)
        #exiting
        
    -show(filename)
        #Showing file using CMD
        
    -hide(filename)
        #Hiding file using CMD
        
    -loop()
        #looping except KeyboardInterrupt
        
    -exist(filename, is hiden)
        #cheking if file exist
        
    -help()
        #Showing all commands
        
    -user(name, password, encrypth?)
        #making new user
        
    -userC()
        #Deliting courient user
        
    -lockout (name,password,exit if fail,key encrypth key (opsinal)")
        #nided to unlock
""")
try:
    show("ADMIN.txt")
    cn=open("ADMIN.txt","r")
    con=cn.read()
    cn.close()
    hide("ADMIN.txt")
except FileNotFoundError:
    show("ADMIN.txt")
    fi=open("ADMIN.txt","w")
    fi.write("")
    hide("ADMIN.txt")

try:
    show("PASSWORD.txt")
    cn=open("PASSWORD.txt","r")
    pas=cn.read()
    cn.close()
    hide("PASSWORD.txt")
except FileNotFoundError:
    show("PASSWORD.txt")
    fi=open("PASSWORD.txt","w")
    fi.write("")
    hide("PASSWORD.txt")
def user (name,password,enc=True):
        
    show("ADMIN.txt")
    show("PASSWORD.txt")
    with open("ADMIN.txt","w") as adm:
        adm.write(name)
    with open("PASSWORD.txt","w")as pasw:
        pasw.write(password)
    
    if enc==True:
        from cryptography.fernet import Fernet
        show(".key")
        key = Fernet.generate_key()
        with open('.key', 'wb') as filekey:
           filekey.write(key)
        with open('.key', 'rb') as filekey:
            key = filekey.read()
        hide(".key")
        fernet = Fernet(key)
        with open('PASSWORD.txt', 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open('PASSWORD.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            
        with open('ADMIN.txt', 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open('ADMIN.txt', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        
    hide("ADMIN.txt")
    hide("PASSWORD.txt")
    
    if enc==True:
        return name,password,key
    else:
        return name,password



def userC():
    show("ADMIN.txt")
    show("PASSWORD.txt")
    show(".key")
    with open("ADMIN.txt","w") as adm:
        adm.write("")
    with open("PASSWORD.txt","w")as pasw:
        pasw.write("")
    with open(".key","wb")as pasw:
        pasw.write(b"")
    hide("ADMIN.txt")
    hide("PASSWORD.txt")
    hide(".key")
def lockout(ADMINNAME,password,EX=False,key=b"None"):
    if key != b"None":
        from cryptography.fernet import Fernet
        fernet = Fernet(key)
        with open('ADMIN.txt', 'rb') as enc_file:
            con = enc_file.read()
        con = fernet.decrypt(con)
        con = con.decode()
        with open('PASSWORD.txt', 'rb') as enc_file:
            pas = enc_file.read()
        pas = fernet.decrypt(pas)
        pas = pas.decode()
    elif key ==b"None":
        with open("PASSWORD.txt","r") as w:
            pas=w.read()
        with open("ADMIN.txt","r") as w:
            con=w.read()
        
    if password==pas and ADMINNAME==con:
        return 1
    elif password != pas or ADMINNAME != con:
        if EX==True:
            Quit(0)
        elif EX==False:
            return 0
