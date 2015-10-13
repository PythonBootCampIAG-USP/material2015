#CONTOUR PLOTS
#Based on the original script by Nicolas P. Rougier
#http://www.labri.fr/perso/nrougier/teaching/matplotlib/scripts/contour_ex.py

import numpy as np
import matplotlib.pyplot as plt

#Defining the grid size and the meshgrid matrices
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

#The function that takes the x, y values and returns z values
def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

#Tightening the layout a little bit
plt.axes([0.025,0.025,0.95,0.95])

#The contourf() function fills the space with solid colors and can take
#additional arguments such as transparency and a colormap
plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap=plt.cm.hot)

#The line contour plot is assigned to an object to label the contours...
C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidth=.5)

#... using this function that takes the object and automatically draws
#their values. It also has some options to put the text above, below or
#inside the contour lines.
plt.clabel(C, inline=1, fontsize=10)

#removing the ticks to clean the figure
plt.xticks([]), plt.yticks([])

plt.show()