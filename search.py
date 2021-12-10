import mysql.connector
# profile_id = input("Enter profile_id")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="leakeddata"
)
# print(mydb)
mycursor = mydb.cursor()

sql = "INSERT INTO SearchData (Data) VALUES (%s)"

f=open("India 2.txt",mode='r+',encoding='utf8')
l=f.readlines()
for i in range(1301,1350):
    mycursor.execute("INSERT INTO SearchData (Data) VALUES ('"+l[i]+"')")
mydb.commit()


# f1=open("India 2.txt", mode="r+", encoding="utf8")
# l1=f1.readlines()
# for j in l1:
#     if profile_id in j:
#         print(j)
