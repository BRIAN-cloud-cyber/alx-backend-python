## seed=__import__('seed') imports seed library inorder to use its tools
creation 0f database ## connection=seed.create_database(connection)
connection=seed.connect_to_prodev()# direct call
after creation ,inside the database,we add tables and insert data from a csv file
## if connection:
## seed.create_table(connection)
## seed.insert_data(connection,'user_data_csv')


cursor=connection.cursor() # writer to the tables
cursor.execute(f".....") # checks if the database exists"
cursor.fetchone() takes the first row
cursor.fetchall()takes all the rows
cursor.execute(f"SELECT * FROM USERS_DATA LIMIT 5) 
