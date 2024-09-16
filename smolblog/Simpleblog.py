import bcrypt
from rich import print
import os
import datetime
import getpass
import csv
import art
import textwrap

h=0
user="user"
art=art.text2art("Blogbook")
print(art)

class post:
    def __init__(self,author,date,title,content):
        self.author=author
        self.date=date
        self.title=title
        self.content=content
    
    def write(self):
        print("[yellow]"+self.content+"[/yellow]")
        self.content=input()
        print("\n")
        saveposts(self)
        print("post saved..\n")

    def display(self):
        print("|---------------------------------------------------------------------------------------------|")
        print("\t[crimson]"+self.title+"[/crimson]\n|---------------------------------------------------------------------------------------------|")
        print("\n\t"+textwrap.fill(self.content,28)+"\n\n|---------------------------------------------------------------------------------------------|\n\n")
    
    def read(self):
        print("\t[crimson]"+self.title+"[/crimson]\n|-------------------------------------------------------------------------|")
        print("\n\t"+self.content+"\n\n|-------------------------------------------------------------------------|\n\n")
        ch=int(input("1.More post info\n2.Next\n3.Back  : "))
        if ch==1:
            print("author: "+self.author+"\n\n","date created: "+str(self.date))
        elif ch==3:
            return 1


def auth():
    h=0
    u=input('Username: ')
    q=getpass.getpass(prompt="Password: ",stream=None)
    p=q.encode("utf-8")
    with open("users.csv",newline='') as f:
        f.seek(0)
        reader=csv.reader(f)
        for row in reader:
            if row[0]==u:
                if bcrypt.checkpw(p,row[1].encode("utf-8")):
                    h=1
                    break
    #n, get from csv file
    if h==1:
        print("authorised as user "+u+"\n")
        os.chdir("Blog/"+u)
    else:
        print("username or password doesnt match, executing self destruct sequence")
    return h,u

def signup(s):
    u=input("Enter username: ")
    with open("users.csv","r+") as f:
        newuser=csv.writer(f)
        reader=csv.reader(f)
        found=0
        f.seek(0)
        for i in reader:
            if i[0]==u:
                found=1
                break
        if found==1:
            print("username already exists..\n\n")
        elif found==0:
            d=True
            while d:
                p=input("enter password: ")
                q=input("confirm password: ")
                if p==q:
                    r=p.encode("utf-8")
                    s=bcrypt.hashpw(r,bcrypt.gensalt())
                    t=s.decode("utf-8")
                    d=False
                    l=[u,t]
                    newuser.writerow(l)
                    
                    try:
                        os.mkdir("Blog/"+u+"/")
                        os.chdir("Blog/"+u+"/")
                    except FileExistsError:
                        os.chdir("Blog/"+u+"/")
                    s=0
                #add username and password to sql table
                else:
                    print("password not confirmed. Try again.\n\n")
                    s=1
    if s==1:
        signup(s)
    
def logout():
    h=0
    os.chdir("/Blog/")

def saveposts(blogpost):
    f=open(blogpost.title+".txt","w")
    f.write(blogpost.content)
    f.close()

posts=[]
myposts=[]
def takein():
    i=0
    for fileder in os.listdir("Blog"):
        for file in os.listdir("Blog/"+fileder):
            i=i+1
            with open("Blog/"+fileder+"/"+file,"r") as f:
                content=f.read()
                current=os.getcwd()
                author=os.path.basename(current)
                date=os.path.getctime(current)
                title=file.replace(".txt","")
                posts.append(post(author,date,title,content))
        if i==10:
            break
    return posts
    #10 post objects created


posts=takein()   
def mainmenu(h,user):
    for i in posts:
        i.display()
    if h==0:
        c=int(input("1.View posts\n2.Login\n3.Signup\n\r"))
        if c==1:
            ch=input("what post do you want to view? Enter b to browse: ")
            if ch=="b":
                for i in posts:
                    r=i.read()
                    if r==1:
                        break
            for i in posts:
                if ch==i.title:
                    print("\n")
                    r=i.read()
                    break

            for i in posts:
                r=i.read()
                if r==1:
                    break
        elif c==2:
            [h,u]=auth()
            return h,u
        elif c==3:
            try:
                signup(1)
            except KeyboardInterrupt:
                mainmenu()

        else:
            pass
    else:
        user=os.path.basename(os.getcwd())
        c=int(input("1.View posts\n2.Write post\n3.Edit post\n4.Your posts : "))
        if c==1:
            for i in posts:
                r=i.read()
                if r==1:
                    break
        elif c==2:
            title=input("What's the title? ")
            content=input("Some content please!!: ")
            newpost=post(os.getcwd(),datetime.datetime.now(),title,content)
            saveposts(newpost)
            posts.append(newpost)
        elif c==3:
            s=input("title of post to edit?")

            for i in os.listdir(os.getcwd()):
                if i==s+".txt":
                    with open(i,"r") as f:
                        content=f.read()
                        current=os.getcwd()
                        author=os.path.basename(current)
                        date=os.path.getctime(current)
                        title=i.replace(".txt","")
                        posts.append(post(author,date,title,content))
                        posts[-1].display()
                        posts[-1].write()
                    
        elif c==4:
            for i in os.listdir(os.getcwd()):
                with open(i,"r") as f:
                    content=f.read()
                    current=os.getcwd()
                    author=os.path.basename(current)
                    date=os.path.getctime(current)
                    title=i
                    posts.append(post(author,date,title,content))
            posts[-1].display()
            ch=input("1.Edit post\n2.back : ")
            if ch==1:
                posts[-1].write()
            else:
                mainmenu(h,user)


#enter ascii art stuff
while True:
    h=mainmenu(h,user)
