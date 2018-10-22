# CMSE201
CMSE 201 Class Stuff

#Stuff to Import
```python
import numpy as np
from scipy.integrate import odeint
%matplotlib inline
import matplotlib.pyplot as plt
from IPython.display import display, clear_output, set_matplotlib_formats
set_matplotlib_formats('pdf', 'svg')
```

#ODEINT
```python
# Put your code here

# Import commands
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from scipy.integrate import odeint # This one is new to you!

# Derivative function
def derivs(curr_vals, time):
    
    # Declare parameters
    g = 9.81 # m/s^2
    A = 0.1 # m^2
    m = 80.0 # kg
    l_unstretched = 30
    # Unpack the current values of the variables we wish to "update" from the curr_vals list
    l, v, = curr_vals
    
    # Right-hand side of odes, which are used to compute the derivative
    dldt = v
    dvdt = g + ((-0.65 * A * v * abs(v))/m) + (-1 * k * (l - l_unstretched))/m
    return dldt, dvdt

# Declare Variables for initial conditions
h0 = 200 # meters
v0 = 0 # m/s
l0 = 30 # m/s
g = -9.81 # m/s^2
tmax = 60 # seconds
dt = 0.1 # seconds
k = 6

# Define the time array
time = np.arange(0, tmax + dt, dt)

# Store the initial values in a list
init = [l0, v0]

# Solve the odes with odeint
sol = odeint(derivs, init, time)

# Plot the results using the values stored in the solution variable, "sol"

# Plot the height using the "0" element from the solution
plt.figure(1)
plt.plot(time, sol[:,0],color="green")
plt.xlabel('Time [s]')
plt.ylabel('Height [m]')
plt.grid()

# Plot the velocity using the "1" element from the solution
plt.figure(2)
plt.plot(time, sol[:,1],color="purple")
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.grid()
```
