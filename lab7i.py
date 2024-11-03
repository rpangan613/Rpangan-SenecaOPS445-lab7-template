#!/usr/bin/env python3
# Student ID: Roniel G. Pangan - 113061220

def function1():
    global schoolName  # Declare that we are using the global variable
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # This will modify the global variable
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)  # This will now print 'SICT'
function2()
print('print() in main on schoolName:', schoolName)  # This will now print 'SSDO'
