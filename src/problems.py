import sqlite3

connection = sqlite3.connect("problems.db")
cursor = connection.cursor()

cursor.execute("create table problems (problem_type text, difficulty text, problem text, correct_answer text)")
problems_list = [
    #arithmetic problems
    ("arithmetic", "easy", "1+1", "2"),
    ("arithmetic", "easy", "3+2", "5"),
    ("arithmetic", "easy", "10-6", "4"),
    ("arithmetic", "easy", "10*5", "50"),
    ("arithmetic", "easy", "4*50", "200"),
    ("arithmetic", "easy", "7*6", "42"),
    ("arithmetic", "easy","81/9", "9"),
    ("arithmetic", "easy", "36/6", "6"),
    ("arithmetic", "easy", "28/4", "7")
]



cursor.executemany("insert into problems values (?,?,?,?)", problems_list)

#print database rows
for row in cursor.execute("select * from problems"):
    print(row)
    
connection.close()