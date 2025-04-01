from vpython import *

# Create a 3D sphere
scene = canvas(title="3D Sphere", width=800, height=600)
sphere(radius=1, color=color.blue)

# Keep the script running
while True:
    rate(30)  # This ensures the program keeps running and updates smoothly
