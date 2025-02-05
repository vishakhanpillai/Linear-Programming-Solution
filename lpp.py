from pulp import *
import matplotlib.pyplot as plt
import numpy as np

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

    optimal_x1 = x1.varValue
    optimal_x2 = x2.varValue
    
    print("\nOptimal Value for the objective function is =", value(prob.objective))
else:
    print("\nNo Optimal Solution Found")
        


plt.figure(figsize=(16, 12)) 

x_vals = np.linspace(0, 100, 1000)  

for cx1, cx2, rhs, sign in constraints:
    if cx2 != 0:
        y_vals = (rhs - cx1 * x_vals) / cx2  # Solve for x2
    else:
        y_vals = np.full_like(x_vals, rhs / cx1)  # Vertical line case

    if sign == "<=":
        plt.fill_between(x_vals, y_vals, 0, where=(y_vals >= 0), alpha=0.2, color='blue')  # Feasible region
    else:
        plt.fill_between(x_vals, y_vals, 100, where=(y_vals >= 0), alpha=0.2, color='red')  # Outside region

    plt.plot(x_vals, y_vals, label=f"{cx1}x1 + {cx2}x2 {sign} {rhs}")

# Mark the optimal solution
plt.scatter(optimal_x1, optimal_x2, color='red', s=250, marker='o', label="Optimal Solution")

# Labels and formatting
plt.xlabel("x1", fontsize=14)
plt.ylabel("x2", fontsize=14)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(0, 100)  # Increased x-axis range
plt.ylim(0, 100)  # Increased y-axis range
plt.legend(fontsize=12)
plt.title("Linear Programming Feasible Region and Constraints", fontsize=16)
plt.grid(True)

# Show the plot
plt.show()