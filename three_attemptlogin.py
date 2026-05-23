username=input("enter you username")
password=int(input("enter you password"))

data={
    "Pushkar":1234,
    "rahul":5678

}

if username in data:
    if password==data[username]:
        print("Welcome Back")
        print("you are logged in")

    if password!=data[username]:
        for i in range(1,3):
            password=int(input("enter you password again"))

            if password == data[username]:
                print("Welcome Back!")
                print("you are logged in")
                break

        else :
         print("wrong password")
         print("try again after sometime.....")

else:
    print("username not found")
    print("try again after sometime........")