# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Define constraints
def constraint1(x):
    return 40 - 2*x

def constraint2(x):
    return (45 - x) / 3

# Define x range
x = np.linspace(0, 20, 400)

# Constraint 1 plot
plt.plot(x, constraint1(x), label=r'$2x_1 + x_2 \leq 40$')

# Constraint 2 plot
plt.plot(x, constraint2(x), label=r'$x_1 + 3x_2 \leq 45$')

# Constraint 3 plot
plt.plot([10, 10], [0, 15], label=r'$x_1 \leq 10$')

# Constraint 4 plot (x and y axes)
plt.plot(0, 0, 'bo')  # Show origin
plt.xlim(0, 20)
plt.ylim(0, 15)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.fill_between(x, np.minimum(constraint1(x), constraint2(x)), where=(x <= 10), color='gray', alpha=0.5)

# Show feasible region
plt.fill_between(x, np.minimum(constraint1(x), constraint2(x)), where=(x <= 10), color='gray', alpha=0.5)

# Mark the optimal point
plt.plot(10, 10, 'ro')  # Optimal point (10, 10)

# Annotate the optimal point value
plt.text(10, 10, ' Optimal\n (10,10)', verticalalignment='bottom')

# Add title and constraint labels
plt.title('Linear Programming with Graphical Method')
plt.legend()
plt.grid(True)
plt.show()

##################222#######################
# Define constraints
def constraint1(x):
    return (28 - 7*x)/2

def constraint2(x):
    return (24 - 3*x)/8

# Define x range
x = np.linspace(0, 10, 400)

# Constraint 1 plot
plt.plot(x, constraint1(x), label=r'$7x_1 + 2x_2 \geq 28$')

# Constraint 2 plot
plt.plot(x, constraint2(x), label=r'$3x_1 + 8x_2 \geq 24$')

# Constraint 3 plot (x and y axes)
plt.plot(0, 0, 'bo')  # Show origin
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.fill_between(x, constraint1(x), where=(x >= 0), color='gray', alpha=0.5)
plt.fill_between(x, constraint2(x), where=(x >= 0), color='gray', alpha=0.5)

# Mark the optimal point
plt.plot(4, 0, 'ro')  # Optimal point (4, 0)

# Annotate the optimal point value
plt.text(4, 0, ' Optimal\n (4,0)', verticalalignment='bottom')

# Add title and constraint labels
plt.title('Linear Programming with Graphical Method')
plt.legend()
plt.grid(True)
plt.show()

######################333####################################33
# Define constraints
def constraint1(x):
    return (12 - x) / 2

def constraint2(x):
    return (12 - 2*x) / 3

def constraint3(x):
    return 8 - 2*x

# Define x range
x = np.linspace(0, 10, 400)

# Constraint 1 plot
plt.plot(x, constraint1(x), label=r'$x_1 + 2x_2 \leq 12$')

# Constraint 2 plot
plt.plot(x, constraint2(x), label=r'$2x_1 + 3x_2 = 12$')

# Constraint 3 plot
plt.plot(x, constraint3(x), label=r'$2x_1 + x_2 \geq 8$')

# Constraint 4 plot (x and y axes)
plt.plot(0, 0, 'bo')  # Show origin
plt.xlim(0, 8)
plt.ylim(0, 8)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.fill_between(x, np.minimum(constraint1(x), constraint2(x)), where=(x <= 4), color='gray', alpha=0.5)
plt.fill_between(x, constraint2(x), constraint3(x), where=(x >= 2), color='gray', alpha=0.5)

# Mark the optimal point
plt.plot(2, 2, 'ro')  # Optimal point (2, 2)

# Annotate the optimal point value
plt.text(2, 2, ' Optimal\n (2,2)', verticalalignment='bottom')

# Add title and constraint labels
plt.title('Linear Programming with Graphical Method')
plt.legend()
plt.grid(True)
plt.show()


###################################444#################################
# Define constraints
def constraint1(x):
    return 4 - x

def constraint2(x):
    return 5

def constraint3(x):
    return (12 - 3*x) / 2

def constraint4(x):
    return (4 + x) / 2

# Define x range
x = np.linspace(0, 10, 400)

# Constraint 1 plot
plt.plot(x, constraint1(x), label=r'$x_1 \leq 4$')

# Constraint 2 plot
plt.axhline(y=5, color='r', linestyle='-', label=r'$x_2 \leq 5$')

# Constraint 3 plot
plt.plot(x, constraint3(x), label=r'$3x_1 + 2x_2 \leq 12$')

# Constraint 4 plot
plt.plot(x, constraint4(x), label=r'$-x_1 + 2x_2 \geq 4$')

# Constraint 5 plot (x and y axes)
plt.plot(0, 0, 'bo')  # Show origin
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Show feasible region
plt.fill_between(x, np.minimum(np.minimum(constraint1(x), constraint2(x)), constraint3(x)), where=(x <= 4), color='gray', alpha=0.5)
plt.fill_between(x, constraint3(x), constraint4(x), where=(x >= 2), color='gray', alpha=0.5)

# Mark the optimal point
plt.plot(4, 0, 'ro')  # Optimal point (4, 0)

# Annotate the optimal point value
plt.text(4, 0, ' Optimal\n (4,0)', verticalalignment='bottom')

# Add title and constraint labels
plt.title('Linear Programming with Graphical Method')
plt.legend()
plt.grid(True)
plt.show()


###################555###################################
# Define constraints
def constraint1(x):
    return (15 - 3*x) / 5

def constraint2(x):
    return 2 - x

# Define x range
x = np.linspace(0, 5, 400)

# Constraint 1 plot
plt.plot(x, constraint1(x), label=r'$3x_1 + 5x_2 \geq 15$')

# Constraint 2 plot
plt.plot(x, constraint2(x), label=r'$x_1 + x_2 \leq 2$')

# Constraint 3 plot (x and y axes)
plt.plot(0, 0, 'bo')  # Show origin
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Show feasible region
plt.fill_between(x, np.maximum(constraint1(x), 0), where=(x >= 0), color='gray', alpha=0.5)
plt.fill_between(x, 0, constraint2(x), where=(x <= 2), color='gray', alpha=0.5)

# Mark the optimal point
plt.plot(1.5, 0.5, 'ro')  # Optimal point (1.5, 0.5)

# Annotate the optimal point value
plt.text(1.5, 0.5, ' Optimal\n (1.5,0.5)', verticalalignment='bottom')

# Add title and constraint labels
plt.title('Linear Programming with Graphical Method')
plt.legend()
plt.grid(True)
plt.show()

