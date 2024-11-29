import mysql

print("se ha corrido este hijoputa")


testDataBase = mysql.TestDataBase("mysql://test:test@test-database:3306/test")
testDataBase.init_database()


print("se ha corrido este hijoputa")
