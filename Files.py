employee_file = open("employees.txt", "r")
print(employee_file.readable())
print(employee_file.readline())
# Jim utantol folytatja az olvasast
# print(employee_file.read())  # Az egesz fajlt beolvassa
#print(employee_file.readlines())  # ['Dwight- Salesman\n', 'Pam - Receptionist\n', 'Michael - Manager\n', 'Oscar - Accountant']
print(employee_file.readlines()[1])
employee_file.close()

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

########################## Write File #############################

employee_file = open("employees.txt", "a")  # append
print(employee_file.writable())
employee_file.write("\nToby - Human Resources")
employee_file.close()

employee_file = open("employees.txt", "w")  # overwrite
employee_file.write("\nKaren - Human Resources")
employee_file.close()

employee_file = open("index.html", "w")  # writes a new file
employee_file.write("<p>This is HTML </p>")
employee_file.close()