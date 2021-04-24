


employee_code = int(input("provide employee number : "))
employee_name = input("provide employee name : ")
employee_salary= float(input(" please provide employee salary : "))

def HRA(employee_salary):
    return 0.4 * employee_salary

def DA(employee_salary):
    return 0.1 * employee_salary

def CCA(employee_salary):
    return 0.05 * employee_salary

def GS(employee_salary,hra,da,cca):
    return employee_salary + hra+ da+ cca

def IT(gs):
    return 0.1 * gs

def PF(gs):
    return 0.1 * gs

def NS(gs,pf,it):
    return gs - (pf+ it)

hra = int(HRA(employee_salary))
da = DA(employee_salary)
cca = CCA(employee_salary)
gs = GS(employee_salary,hra,da,cca)
it = IT(gs)
pf = PF(gs)
ns =NS(gs,pf,it)

print ("HRA component of salary is",hra)
print ("DA component of salary is",da)
print ("CCA component of salary is",cca)
print ("GS component of salary is",gs)
print ("IT component of salary is",it)
print ("PF component of salary is",pf)
print ("NS component of salary is",ns)
