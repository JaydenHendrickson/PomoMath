import sqlite3

#All
calc_1_list = [
    #Easy problems
    ("easy", "f(x) = 5x^3 Find f'(x)", "15x^2"),
    ("easy", "f(x) = x^2 + 3x + 7  Find f'(x)", "2x + 3"),
    ("easy", "f(x) = 8x^5 Find f'(x)", "40x^4"),
    ("easy", "f(x) = 4x^2 - 2x + 1 Find f'(x)", "8x - 2"),
    ("easy", "f(x) = 7x Find f'(x)", "7"),
    ("easy", "f(x) = 9 Find f'(x)", "0"),
    ("easy", "f(x) = x^4 Find f'(x)", "4x^3"),
    ("easy", "f(x) = 3x^3 + 2x^2 + x Find f'(x)", "9x^2 + 4x + 1"),
    ("easy", "f(x) = x^6 - 4x^3 Find f'(x)", "6x^5 - 12x^2"),
    ("easy", "f(x) = 2x^5 + x^4 - x^2 Find f'(x)", "10x^4 + 4x^3 - 2x"),
    
    #medium
    ("medium", "f(x) = sin(x) + x^2 Find f'(x)", "cos(x) + 2x"),
    ("medium", "f(x) = e^x + 3x^2 Find f'(x)", "e^x + 6x"),
    ("medium", "f(x) = ln(x) + 4x Find f'(x)", "1/x + 4"),
    ("medium", "f(x) = cos(x) - x^3 Find f'(x)", "-sin(x) - 3x^2"),
    ("medium", "f(x) = 5x^2 * e^x Find f'(x)", "10xe^x + 5x^2e^2"),
    ("medium", "f(x) = x^2 * ln(x) Find f'(x)", "2xln(x) + x"),
    ("medium", "f(x) = tan(x) + x^2 Find f'(x)", "sec^2(x) + 2x"),
    ("medium", "f(x) = sqrt(x) + ln(x) Find f'(x)", "1/2sqrt(x) + 1/x"),
    ("medium", "f(x) = e^x^2 Find f'(x)", "2xe^x^2"),
    ("medium", "f(x) = x * sin(x) Find f'(x)", "sin(x) + xcos(x)")
    
]

"""NOTE Since the answers are formated with spaces (Ex. 2x + 3), it might be best to do:
attempt = attempt.replace(" ", "") before testing for correctness so any answer (no matter how many spaces) 
will be correct so long as the values are correct
"""

#All the database stuff
connection = sqlite3.connect("problems.db")
cursor = connection.cursor()

#creating tables

#Dropping tables so that we can run it as we update without deleting the database each time the program runs
cursor.execute("drop table if exists problems.calc_1")

#Creating and inserting values into tables
cursor.executemany("insert into calc_1 values (?,?,?)", calc_1_list)

#print database rows so everything works!
for row in cursor.execute("select * from calc_1"):
    print(row)

connection.close()