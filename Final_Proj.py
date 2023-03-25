import mysql.connector as sqltor
from datetime import date
import requests
from tkinter import *
from tkinter import messagebox

url = "https://netflix54.p.rapidapi.com/search/"
dic={}
lst=[]
dic1={}
log1=0
sign=0
amd=0
num1=30

db0 = sqltor.connect(host="localhost", user='root', passwd='Orchid7890', database='netflix1 ')
cursor = db0.cursor()

str2 = "create table if not exists admin(admin_email varchar(255), movie_name char(255), movie_description longtext,genre varchar(255), age_restriction varchar(255), duration integer, year_released integer);"
cursor.execute(str2)

str1= "create table if not exists login(email_id varchar(255) primary key, password varchar(20), phone_number bigint,age int, subscription_plan varchar(30), starting_date date);"
cursor.execute(str1)

str4= "create table if not exists admin_id(email_id varchar(255) primary key, password varchar(20));"
cursor.execute(str4)

root = Tk()
root.configure(bg='black')
#root.resizable(height=1000, width= 500)
root.geometry('600x150')
mainpage = Label(root, text = '''Welcome to Netflix! \nDo you want to Sign Up or Log In?''', bg="black", fg="white")
mainpage.pack()

def loginx():
    top = Toplevel()
    top.configure(bg='black')
    top.geometry('600x180')
    intend = Label(top, text="Logging In", bg="black", fg="white")
    intend.pack()
    emailLabel = Label(top, text="Email: ", bg="black", fg="white")
    emailLabel.place(x=200, y=40)
    PasswordLabel = Label(top, text="Password: ", bg="black", fg="white")
    PasswordLabel.place(x=200, y=70)
    mainpage.pack()
    emailinput = Entry(top,bg="#212221", fg="#90b4fc")
    passwordinput = Entry(top,bg="#212221", fg="#90b4fc")
    emailinput.place(x=280, y=40)
    passwordinput.place(x=280, y=70)

    def log():
        log1=0
        global sign
        amd=0
        global email
        email=emailinput.get()
        password=passwordinput.get()
        login = "select * from login where email_id= '{}';".format(email)
        cursor.execute((login))
        lst = cursor.fetchall()

        if email=="" or password=="":
            messagebox.showinfo("Error","Please enter all fields.")
        elif len(lst) == 0:
            messagebox.showinfo("Error", "Please signup")
            sign()
            #sign += 1
        else:
            admin = "select * from admin_id where email_id='{}';".format(email)
            cursor.execute(admin)
            lst1 = cursor.fetchall()
            #print(lst1)
            for i in range(len(lst1)):
                if email == lst1[i][0]:
                    amd += 1
                    break
            if lst[0][1] == password:
                print("Successfully logged in.")
                top.destroy()
                log1 += 1

            else:
                top.destroy()
                messagebox.showinfo("Error", "Please enter valid password")
                loginx()
        if amd>0 and log1>0:
            #print("hello admin")
            top1 = Toplevel()
            top1.configure(bg='black')
            top1.geometry('300x170')
            intend1 = Label(top1, text="Hello Admin", bg="black", fg="white")
            intend1.pack()
            def upload():
                top2 = Toplevel()
                top2.configure(bg='black')
                top2.geometry('600x280')
                intend2 = Label(top2, text="Uploading Data", bg="black", fg="white")
                intend2.pack()
                nameLabel1 = Label(top2, text="Name of the Movie: ", bg="black", fg="white")
                nameLabel1.place(x=150, y=50)
                moviedescLabel = Label(top2, text="Brief Description: ", bg="black", fg="white")
                moviedescLabel.place(x=150, y=80)
                genreLabel = Label(top2, text="Genre: ", bg="black", fg="white")
                genreLabel.place(x=150, y=110)
                age_resLabel = Label(top2, text="Age Restriction: ", bg="black", fg="white")
                age_resLabel.place(x=150, y=140)
                durationLabel = Label(top2, text="Duration: ", bg="black", fg="white")
                durationLabel.place(x=150, y=170)
                yearLabel = Label(top2, text="Year: ", bg="black", fg="white")
                yearLabel.place(x=150, y=200)

                nameinput1 = Entry(top2,bg="#212221", fg="#90b4fc")
                moviedescinput = Entry(top2,bg="#212221", fg="#90b4fc")
                genreinput = Entry(top2,bg="#212221", fg="#90b4fc")
                ageinput = Entry(top2,bg="#212221", fg="#90b4fc")
                durationinput = Entry(top2,bg="#212221", fg="#90b4fc")
                yearinput = Entry(top2,bg="#212221", fg="#90b4fc")
                nameinput1.place(x=280, y=50)
                moviedescinput.place(x=280, y=80)
                genreinput.place(x=280, y=110)
                ageinput.place(x=280, y=140)
                durationinput.place(x=280, y=170)
                yearinput.place(x=280, y=200)
                def up():
                    movie_name=nameinput1.get()
                    movie_desc=moviedescinput.get()
                    genre=genreinput.get()
                    age_res=ageinput.get()
                    duration=durationinput.get()
                    year=yearinput.get()
                    try:
                        str5 = "insert into admin values('{}','{}','{}','{}','{}',{},{});".format(email, movie_name,movie_desc, genre, age_res, duration, year)
                        cursor.execute(str5)
                        db0.commit()
                        messagebox.showinfo("Success!","Data Succesfully Updated")
                        top2.destroy()
                    except:
                        messagebox.showinfo("Error", "Please enter valid data")


                mainbutton = Button(top2, text="Go!", command=up, bg="#90b4fc", fg="black")
                mainbutton.place(x=285, y=230)

            mainbutton = Button(top1, text="Upload Data", command=upload, bg="#90b4fc", fg="black")
            mainbutton.place(x=110, y=50)

            def delet():
                top2 = Toplevel()
                top2.configure(bg='black')
                top2.geometry('600x170')
                intend3 = Label(top2, text="Deleting Data", bg="black", fg="white")
                intend3.pack()
                nameLabel1 = Label(top2, text="Name of the Movie: ", bg="black", fg="white")
                nameLabel1.place(x=150, y=50)
                nameinput1 = Entry(top2, bg="#212221", fg="#90b4fc")
                nameinput1.place(x=280, y=50)
                def dele():
                    mov = nameinput1.get()
                    try:
                        str6 = "delete from admin where movie_name='{}'".format(mov)
                        cursor.execute(str6)
                        db0.commit()
                        top2.destroy()
                    except:
                        messagebox.showinfo("Error", "Please enter valid data")
                mainbutton = Button(top2, text="Go!", command=dele, bg="#90b4fc", fg="black")
                mainbutton.place(x=280, y=90)

            mainbutton1 = Button(top1, text="Delete Data", command=delet, bg="#90b4fc", fg="black")
            mainbutton1.place(x=112, y=80)

            def exit():
                top1.destroy()
                amd=0
                loginx()
            mainbutton2 = Button(top1, text="Exit", command=exit, bg="#90b4fc", fg="black")
            mainbutton2.place(x=127, y=110)



        elif log1>0:
            str3=""
            num=30
            #print("hello user")
            top1 = Toplevel()
            top1.configure(bg='black')
            top1.geometry('300x300')
            movies = []
            print('\n')
            str6 = 'select * from admin;'
            cursor.execute(str6)
            lst1 = cursor.fetchall()
            for i in range(0,len(lst1)):
                str3=str3+lst1[i][1]+'\n'
                movies.append(lst1[i][1])
                num+=30
            #print(str3)
            intend1 = Label(top1, text="Hello user \nAvailable Movies: \n", bg="black", fg="white")
            intend1.pack()
            intend2 = Label(top1, text=str3, bg="black", fg="white")
            intend2.pack()
            nameLabel1 = Label(top1, text="Name of Movie: ", bg="black", fg="white")
            nameLabel1.place(x=50, y=num)
            nameinput1 = Entry(top1, bg="#212221", fg="#90b4fc")
            nameinput1.place(x=155, y=num)
            Label1 = Label(top1, text="\n", bg="black", fg="white")
            Label1.pack()
            def movie():

                top2 = Toplevel()
                top2.configure(bg='black')
                top2.geometry('1000x450')
                moviee=nameinput1.get()
                if moviee not in movies:
                    messagebox.showinfo("Error","Movie not available")
                else:
                    for j in lst1:
                        if j[1] == moviee:
                            nameLabel1 = Label(top2, text="Name of Movie ", bg="black", fg="white")
                            nameLabel1.pack()
                            name1 = Label(top2, text=j[1], bg="black", fg="white")
                            name1.pack()
                            descLabel1 = Label(top2, text="\nMovie Description ", bg="black", fg="white")
                            descLabel1.pack()
                            deLabel1 = Label(top2, text=j[2], bg="black", fg="white")
                            deLabel1.pack()
                            genreLabel1 = Label(top2, text="\nGenre ", bg="black", fg="white")
                            genreLabel1.pack()
                            genLabel1 = Label(top2, text=j[3], bg="black", fg="white")
                            genLabel1.pack()
                            age_resLabel1 = Label(top2, text="\nAge Restriction ", bg="black", fg="white")
                            age_resLabel1.pack()
                            ageLabel1 = Label(top2, text=j[4], bg="black", fg="white")
                            ageLabel1.pack()
                            durationLabel1 = Label(top2, text="\nDuration ", bg="black", fg="white")
                            durationLabel1.pack()
                            durLabel1 = Label(top2, text=str(j[5])+" minutes", bg="black", fg="white")
                            durLabel1.pack()
                            yearLabel1 = Label(top2, text="\nYear ", bg="black", fg="white")
                            yearLabel1.pack()
                            yeLabel1 = Label(top2, text=j[6], bg="black", fg="white")
                            yeLabel1.pack()
                            Label1 = Label(top2, text="\n", bg="black", fg="white")
                            Label1.pack()
                def exit():
                    top2.destroy()

                def movieee():
                    top3 = Toplevel()
                    top3.configure(bg='black')
                    top3.geometry('1000x1000')
                    querystring = {"query": moviee, "limit_titles": "10"}
                    # querystring= {'name':'Cars'}
                    headers = {
                        "X-RapidAPI-Key": "695383fc8amshe2de6b6b8b42f69p12c710jsn0e38bfd74c27",
                        "X-RapidAPI-Host": "netflix54.p.rapidapi.com"
                    }

                    response = requests.get(url, headers=headers, params=querystring)
                    out = response.json()
                    # print(type(out))
                    # print(out)
                    titles = out['titles']
                    for i in titles:
                        # print(type(i))
                        # print(i)
                        # print(i.keys())
                        for j in i.keys():
                            if j == 'jawSummary':
                                #	print(i[j])
                                for k in i[j].keys():
                                    if k == 'cast' or k == 'creators' or k == 'directors' or k == 'writers' or k == 'genres' or k == 'contextualSynopsis' or k == 'maturity' or k == 'title' or k == 'releaseYear':
                                        if type(i[j][k]) != list and type(i[j][k]) != dict:
                                            dic1[k] = i[j][k]

                                        else:
                                            if type(i[j][k]) == list:
                                                for l in i[j][k]:
                                                    # print(type(l))
                                                    # print(l)
                                                    dic1[k] = i[j][k][0]['name']
                                            else:
                                                for l in i[j][k].keys():
                                                    if type(i[j][k][l]) != dict:
                                                        dic1[k] = i[j][k][l]
                                                        break
                                                    else:
                                                        for m in i[j][k][l].keys():
                                                            dic1[k] = i[j][k][l][m]
                                                            break
                        #print(dic1)
                        global num1
                        for i in dic1.keys():
                            #print(i, ":", dic1[i])
                            Label1 = Label(top3, text=i.capitalize(), bg="black", fg="white")
                            Label1.place(x=30,y=num1)
                            Label2 = Label(top3, text=": ", bg="black", fg="white")
                            Label2.place(x=140,y=num1)
                            Label3 = Label(top3, text=dic1[i], bg="black", fg="white")
                            Label3.place(x=160,y=num1)
                            num1+=30
                        num1+=10
                        #Label4 = Label(top2, text="\n\n\n", bg="black", fg="white")
                        #Label4.pack()
                mainbutton3 = Button(top2, text="Explore More Movies", command=movieee, bg="#90b4fc", fg="black")
                mainbutton3.pack()
                mainbutton2 = Button(top2, text="Exit", command=exit, bg="#90b4fc", fg="black")
                mainbutton2.pack()

            mainbutton2 = Button(top1, text="Go!", command=movie, bg="#90b4fc", fg="black")
            mainbutton2.pack()


    mybutton = Button(top, text="Log In", command=log, bg="#90b4fc", fg="black")
    mybutton.place(x=275, y=120)

def sign():
    top = Toplevel()
    top.configure(bg='black')
    top.geometry('600x330')
    intend = Label(top, text="Signing Up\n\nPlans: \n1. Mobile: ₹149\n2. Basic: ₹199\n3. Standard: ₹499\n4. Premium: ₹649", bg="black", fg="white")
    intend.pack()
    emailLabel = Label(top, text="Email: ", bg="black", fg="white")
    emailLabel.place(x=150, y=140)
    PasswordLabel = Label(top, text="Password: ", bg="black", fg="white")
    PasswordLabel.place(x=150, y=170)
    phoneLabel = Label(top, text="Phone number: ", bg="black", fg="white")
    phoneLabel.place(x=150, y=200)
    AgeLabel = Label(top, text="Age: ", bg="black", fg="white")
    AgeLabel.place(x=150, y=230)
    PlanLabel = Label(top, text="Plan: ", bg="black", fg="white")
    PlanLabel.place(x=150, y=260)
    mainpage.pack()
    emailinput = Entry(top, bg="#212221", fg="#90b4fc")
    passinput = Entry(top, bg="#212221", fg="#90b4fc")
    phoneinput = Entry(top, bg="#212221", fg="#90b4fc")
    ageinput = Entry(top, bg="#212221", fg="#90b4fc")
    planinput = Entry(top, bg="#212221", fg="#90b4fc")
    emailinput.place(x=280, y=140)
    passinput.place(x=280, y=170)
    phoneinput.place(x=280, y=200)
    ageinput.place(x=280, y=230)
    planinput.place(x=280, y=260)


    def signup():
        try:

            email = emailinput.get()
            password = passinput.get()
            phone = phoneinput.get()
            age = ageinput.get()
            plan = planinput.get()
            today = date.today()
            #print(email, password, phone, age, plan, today)


            log = "select * from login where email_id= '{}';".format(email)
            cursor.execute((log))
            lst1 = cursor.fetchall()
            #   print(lst1)
            if len(lst1)>0:
                messagebox.showinfo("Error","Username already exists")
                top.destroy()
                loginx()
            else:
                if email=="" or password== "" or phone== " " or age=="" or plan=="":
                    messagebox.showinfo("Error","Please enter all fields.")
                else:
                    str3 = "insert into login values('{}','{}',{},{},'{}','{}');".format(email, password,phone, age, plan, today)
                    cursor.execute(str3)
                    db0.commit()
                    messagebox.showinfo("Success!", "Successfully Signed Up")
                    print("Successfully signed up")
                    top.destroy()
                    loginx()
        except:
            messagebox.showinfo("Error", "Please enter valid details")

    mybutton=Button(top,text="Sign Up",command=signup,bg="#90b4fc", fg="black")
    mybutton.place(x= 250,y=290)


mainbutton = Button(root, text="Login", command=loginx, bg="#90b4fc", fg="black")
mainbutton.place(x=275, y=50)
mainbutton1 = Button(root, text="Sign Up", command=sign, bg="#90b4fc", fg="black")
mainbutton1.place(x=269, y=80)
root.mainloop()
