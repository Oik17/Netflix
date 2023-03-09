import mysql.connector as sqltor
from datetime import date
import requests

url = "https://netflix54.p.rapidapi.com/search/"
dic={}
lst=[]
dic1={}
log1=0
sign=0
amd=0

db0 = sqltor.connect(host="localhost", user='root', passwd='pass', database='netflix')
cursor = db0.cursor()

str2 = "create table if not exists admin(admin_email varchar(255), movie_name char(255), movie_description longtext,genre varchar(255), age_restriction varchar(255), duration integer, year_released integer);"
cursor.execute(str2)

str1= "create table if not exists login(email_id varchar(255) primary key, password varchar(20), phone_number bigint,age int, subscription_plan varchar(30), starting_date date);"
cursor.execute(str1)

str4= "create table if not exists admin_id(email_id varchar(255) primary key, password varchar(20));"
cursor.execute(str4)

print("Do you want to sign up or login in?")
print("Press 1 to log in, 2 to sign up.")

log=int(input("Enter your choice: "))

while log!=1 and log!=2:
    print("Please enter a valid choice.")
    log = int(input("Enter your choice: "))

def loginx():
    print("Logging In...")
    global log1
    global sign
    global amd
    global email
    email= str(input("Enter your email: "))
    password= str(input("Enter your password: "))
    login="select * from login where email_id= '{}';".format(email)
    cursor.execute((login))
    lst=cursor.fetchall()

    try:
        admin="select * from admin_id where email_id='{}';".format(email)
        cursor.execute(admin)
        lst1=cursor.fetchall()
        if email==lst1[0][0]:
            amd+=1
    except:
        pass

    #print(lst)
    if len(lst)==0:
        print("Please sign up.")
        sign+=1
    else:
        if lst[0][1]==password:
            print("Successfully logged in.")
            log1+=1

        else:
            print("Invalid Password")
            loginx()
    return 0
if log==1:
    #print("Logging In.")

    loginx()

#print(sign)

if (log==2 or sign>0):
    print("Signing Up.")
    try:
        em=str(input("Enter your email: "))
        passwrd=str(input("Enter your password: "))
        phone= int(input("Enter your phone number: "))
        age= int(input("Enter your age: "))
        print("Choose your plan: ")
        print("Mobile: ₹149")
        print("Basic: ₹199")
        print("Standard: ₹499")
        print("Premium ₹649")

        while 1>0:
            plan= (str(input("Enter your chosen plan: "))).lower()
            if plan== "mobile" or plan== "basic" or plan== "standard" or plan== "premium":
                break
            else:
                print("Invalid entry.")
                continue

        #print("hi")
        today = date.today()
    except:
        print("Please enter valid details")
    try:
        str3 = "insert into login values('{}','{}',{},{},'{}','{}');".format(em,passwrd,phone,age,plan,today)
        cursor.execute(str3)
        db0.commit()
        loginx()
    except:
        print("Userdata already exists")
        loginx()

if log1>0:

    if amd>0:
        print("You're the admin.")

        while True:
            print("Actions: ")
            print("1. Upload Data.")
            print("2. Delete Data.")
            print("3. Exit")
            choose=int(input("Enter your choice: "))
            if choose==1:
                print("Uploading data.")
                movie_name=str(input("Enter movie name: "))
                movie_desc=str(input("Enter brief description of movie: "))
                genre= str(input("Enter genre: "))
                age_res=str(input("Enter age restriction: "))
                duration= int(input("Enter duration: "))
                year=int(input("Enter year released: "))
                str5="insert into admin values('{}','{}','{}','{}','{}',{},{});".format(email,movie_name,movie_desc,genre,age_res,duration,year)
                cursor.execute(str5)
                db0.commit()
                print("Successfully Updated")

            elif choose==2:
                print("Deleting data.")
                mov=str(input("Enter the movie name that you want to delete: "))
                str6="delete from admin where movie_name='{}'".format(mov)
                cursor.execute(str6)
                db0.commit()
                print("Successfully Deleted")

            elif choose==3:
                break
            else:
                print("Please enter valid choice")
                continue


    else:
        print("You're the user")
        movies=[]
        print('\n')
        str6='select * from admin;'
        cursor.execute(str6)
        lst1=cursor.fetchall()
        #print(lst1)
        print("The movies available are: ")
        for i in lst1:
            print(i[1])
            movies.append(i[1])
        print('\n')
        moviee=str(input("What movie do you want to see: "))
        if moviee not in movies:
            print("Movie not available")
        else:
            #print("what")
            print('\n')
            for j in lst1:
                if j[1]==moviee:
                    print("Movie:",j[1])
                    print("Description:",j[2])
                    print("Genre:",j[3])
                    print("Age Restriction:",j[4])
                    print("Duration:",j[5],"minutes")
                    print("Year Released:",j[6])

            print("Do you want more information about similar movies?\nYes/No")

            while True:
                info = (str(input("Enter: "))).lower()
                if info=='no':
                    print("Okay, thank you for using Netflix.")
                    break
                elif info=='yes':
                    print("Okay, redirecting...\n")
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

                        for i in dic1.keys():
                            print(i, ":", dic1[i])

                        print('\n')
                    break

                else:
                    print("Please enter valid choice")
                    continue
