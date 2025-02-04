from pulp import *

print("LPP Solver")
n = input("Please specify Maximization or Minimization (Enter max / min): ")

while True:
    if( n == "max"):
        prob = LpProblem("LPP", LpMaximize)
        break
    elif( n == "min"):
        prob = LpProblem("LPP", LpMinimize)
        break
    else:
        print("Please enter a valid option!!")
        n = input("Please specify Maximization or Minimization (Enter max / min): ")
        
x1 = LpVariable("x1", lowBound = 0)
x2 = LpVariable("x2", lowBound = 0)

print("Enter the coefficients for objective function")
obX1 = int(input("Enter the value of x1: "))
obX2 = int(input("Enter the value of x2: "))

prob += obX1 * x1 + obX2 * x2


cNo = int(input("Enter the number of constraints: "))

if cNo <= 0:
    print("Number must be postive")
    exit()

constraints = []
for i in range(0,cNo):
    print("Constraint ", i + 1)
    cx1 = int(input("Enter the value of x1: "))
    cx2 = int(input("Enter the value of x2: "))
    sign = input("<= or >= ")
    if(sign not in ("<=", ">=")):
        print("Invalid Sign!!!")
        exit()
    rhs = int(input("Enter RHS: "))
    
    if sign == "<=":
        prob += cx1 * x1 + cx2 *x2 <= rhs
        constraints.append((cx1, cx2, rhs, "<="))
    else:
        prob += cx1 * x1 + cx2 *x2 >= rhs
        constraints.append((cx1, cx2, rhs, ">="))

status = prob.solve()

print("The Objective Function Is:", prob.objective)
print("\nConstraints:")
for constraint in prob.constraints.values():
    print(constraint)

print("\nThe Solution is", LpStatus[status], "\n")

if status == 1:
    for i in prob.variables():
        print(i.name, "=", i.varValue)
    print("\nOptimal Value for the objective function is =", value(prob.objective))
else:
    print("\nNo Optimal Solution Found")
        


