seed=__import__('seed')  #bring me a file called seed

connection=seed.connect_db()  #try to connect with seed database
if connection:
    seed.create_database(connection) #if connection successfull ,we create a database then close
    connection.close 
    print(f"connection successful")

connection=seed.connect_to_prodev() # direct call to the prodev database

if connection:
    seed.create_table(connection)  #inside the prodev ,add tables
    seed.insert_data(connection,'user_data.csv') #insert data from csv

cursor=connection.cursor() # like  a pen for writting
##checks if database_prodev is present 
cursor.execute(f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='Alx_prodev';")
result=cursor.fetchone()
if result:
    print(f"Database Alx_prodev is present")

#selects the first five entries 
cursor.execute(f"SELECT * FROM user_data LIMIT 5;")
rows=cursor.fetchall()
print(rows)
cursor.close() #rest our case




