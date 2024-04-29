user = "Rinn"
pwd = "1122"

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == user and password == pwd:
    print("hello" , username) 
elif username == user and password != pwd:
    print("wrong password")
elif username != user and password != pwd:
    print("username or password wrong")
else:
    print("something went weong")