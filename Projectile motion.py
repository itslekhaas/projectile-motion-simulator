import matplotlib.pyplot as plt 
import math 
g = 9.8
u = 20
angle = 45
angle_rad = math.radians(angle)
x_values = []
y_values = []
for t in range(50):
    time = t/10
    x = u * math.cos(angle_rad) * time
    y = (u * math.sin(angle_rad) * time) - ( 1/2 * g * ( time ** 2 ) )
    if y >= 0:
        x_values.append(x)
        y_values.append(y)
plt.plot(x_values,y_values)
plt.xlabel("Horizontal Distance")
plt.ylabel("Vertical Distance")
plt.title("Projectile Motion")
plt.show()
