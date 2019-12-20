# Program : Tax Calculation based on Name , Salary, Gender and age

# Input

name = input("Enter the name of a person for income tax calculation. : ")
print ("\n.........Hi", name, "........\n")
gender = input("Please enter your gender in m or f : ")
age = int(input("Please enter your age in years : "))
salary = float(input("Enter anuual income in rupees : "))

# Process

if salary>0 and salary<=250000 and age>17 and age<=60 and (gender=='m' or gender=='f'):
    print ("Income tax to be paid is 0")
elif salary>250000 and salary<=500000 and age>17 and age<=60 and (gender=='m' or gender=='f'):
    tt1=salary -250000
    tax1= (tt1*5)/100
    ftax1= (tax1*4)/100
    final1=tax1+ftax1
    print ("Income tax to be paid is ", final1)
elif salary>500000 and salary<=1000000 and age>17 and age<=60 and (gender=='m' or gender=='f'):
    tt2=salary-500000
    tax2= 12500 + ((tt2*20)/100)
    ftax2 = (tax2*4)/100
    final2=tax2+ftax2
    print ("Income tax to be paid is ", final2)
elif salary>1000000 and age>17 and age<=60 and (gender=='m' or gender=='f'):
    tt3=salary-1000000
    tax3=112500 + ((tt3*30)/100)
    ftax3 = (tax3*4)/100
    final3=tax3+ftax3
    print ("Income tax to be paid is ", final3)
elif salary>0 and salary<=300000 and age>60 and age<=80 and (gender=='m' or gender=='f'):
    print ("Income tax to be paid is 0")
elif salary>300000 and salary<=500000 and age>60 and age<=80 and (gender=='m' or gender=='f'):
    tt4=salary -300000
    tax4= (tt4*5)/100
    ftax4= (tax4*4)/100
    final4=tax4+ftax4
    print ("Income tax to be paid is ", final4)
elif salary>500000 and salary<=1000000 and age>60 and age<=80 and (gender=='m' or gender=='f'):
    tt5=salary-500000
    tax5= 10000 + ((tt5*20)/100)
    ftax5 = (tax5*4)/100
    final5=tax5+ftax5
    print ("Income tax to be paid is ", final5)
elif salary>1000000 and age>60 and age<=80 and (gender=='m' or gender=='f'):
    tt6=salary-1000000
    tax6=110000 + ((tt6*30)/100)
    ftax6= (tax6*4)/100
    final6=tax6+ftax6
    print ("Income tax to be paid is ", final6)
elif salary>0 and salary<=500000 and age>80 and (gender=='m' or gender=='f'):
    print ("Income tax to be paid is 0")
elif salary>500000 and salary<=1000000 and age>80 and (gender=='m' or gender=='f'):
    tt7=salary-500000
    tax7= ((tt7*20)/100)
    ftax7 = (tax7*4)/100
    final7=tax7+ftax7
    print ("Income tax to be paid is ", final7)
elif salary>1000000 and age>80 and (gender=='m' or gender=='f'):
    tt8=salary-1000000
    tax8=100000 + ((tt8*30)/100)
    ftax8= (tax8*4)/100
    final8=tax8+ftax8
    print ("Income tax to be paid is ", final8)
elif salary<=0:
    print ("salary should be more than 0, please re enter your annual salary amount ")
elif age<18:
    print ("Earning age should start from 18, please re nter your age ")
else:
    print ("Enter the details once again")

    
