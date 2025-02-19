#File: base_solution_py
#date: 13/11/2024

from vpython import *


# Definir los parametros

rM0 = 4.60    # Initial radius of Mercury orbit, in units of R0
vM0 = 5.10e-1 # Initial orbital speed of Mercury, in units of R0/T0
c_a = 9.90e-1 # Base acceleration of Mercury, in units of R0**3/T0**2
rS  = 2.95e-7 # Schwarzschild radius of Sun,in units of R0
rL2 = 8.19e-7 # Specific angular momentum, in units of R0**2

vec_rM0 = vector(0, rM0, 0) # Initial position vector of Mercury
vec_vM0 = vector(vM0, 0, 0) # Initial velocity vector of Mercury



def evolve_mercury(vec_rM_old, vec_vM_old, alpha, beta):
    """
    Advance Mercury in time by one step of length dt.
    Arguments:
         - vec_rM_old: old position vector of Mercury
         - vec_vM_old: old velocity vector of Mercury
         - alpha: strength of 1/r**3 term in force
         - beta: strength of 1/r**4 term in force
    Returns:
         - vec_rM_new: new position vector of Mercury
         - vec_vM_new: new velocity vector of Mercury
    """

    # Compute the factor coming from General Relativity
    fact = 1 + alpha * rS / vec_rM_old.mag + beta * rL2 / vec_rM_old.mag**2
    # Compute the absolute value of the acceleration
    aMS = c_a * fact / vec_rM_old.mag**2
    # Multiply by the direction to get the acceleration vector
    vec_aMS = - aMS * ( vec_rM_old / vec_rM_old.mag )
    # Update velocity vector
    vec_vM_new = vec_vM_old + vec_aMS * dt
    # Update position vector
    vec_rM_new = vec_rM_old + vec_vM_new * dt
    return vec_rM_new, vec_vM_new


dt = 2. * vM0 / c_a / 20  # Time step
alpha = 1.e6              # Strength of 1/r**3 term
beta = 0.0                # Strength of 1/r**4 term
time = 0                  # Current simulation time
max_time = 1000*dt        # Maximum simulation time


# Specify how the output should look like
scene            = canvas()             # Create a new scene: this displays the scene below this cell
scene.userzoom   = False                # No zoom allowed (for smooth scrolling in notebook)
scene.width      = 1024                 # Width of visualization in pixel
scene.height     = 1024                 # Height of visualization in pixel
scene.background = color.white          # Background color ...
scene.center     = vector(0, -2, 0)     # ... and shifted center

# Define graphical objects; M = Mercury, S = Sun ...
M = sphere(pos=vec_rM0,         radius=0.5,  color=color.red   )
S = sphere(pos=vector(0, 0, 0), radius=1.5,  color=color.yellow)
# ... and the initial velocities
M.velocity = vec_vM0
S.velocity = vector(0, 0, 0)

# Add a visible trajectory to Mercury
M.trajectory = curve(color=color.black, radius=0.005)

# Run the simulation for a given time and draw trajectory
while time < max_time:
    # Set the frame rate: shows four earth days at once
    rate(100)
    # Update the drawn trajectory with the current position
    M.trajectory.append(pos=M.pos)
    # Update the velocity and position
    M.pos, M.velocity = evolve_mercury(M.pos, M.velocity, alpha, beta)