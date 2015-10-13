#QUIVERS AND LEGENDS
#Based on the original script by Nicolas P. Rougier
#http://www.labri.fr/perso/nrougier/teaching/matplotlib/scripts/quiver_ex.py

import numpy as np
import matplotlib.pyplot as plt

#Example 1: simple quiver
#Building the vectors
x = np.linspace(-5, 5, 10)     
y = np.linspace(-5, 5, 10)

#Building meshgrid matrices
X, Y = np.meshgrid(x, y)

#Building the matrices of the vector components 
U, V = np.cos((X - 10) / (2*np.pi)), np.sin((Y) / (2*np.pi))

#The quiver() function can take only the u, v matrices or the x, y matrices
#as the vectors positions. It was associated to an object for use in the
#quiverkey() function.
Q = plt.quiver(X, Y, U, V)

#Setting the axis limits to a good plotting area and some space for the legend
plt.axis([-6.2, 6.2, -6.2, 8])

#The quiverkey() function takes the quiver() plot object, the x position,
#y position, size of the legend arrow and the label as a string. Each different
#quiver plot must have different object associated to it, so you can define
#different styles.
plt.quiverkey(Q, 0.93, 0.93, 1, 'arrows')

#Removing the ticks to get a clean figure
plt.xticks([]), plt.yticks([])
plt.show()

#Example 2: same as above, but with 2 different plots on same graph
#The x components were splitted in two
x1 = np.linspace(-5, 0, 5)
x2 = np.linspace(1, 5, 5)

#The y component must remain the same
y = np.linspace(-5, 5, 10)

#Now, we need x and y matrices for both meshgrids  
X1, Y1 = np.meshgrid(x1, y)
X2, Y2 = np.meshgrid(x2, y)

#Same for the u, v components
U1, V1 = np.cos((X1 - 10) / (2*np.pi)), np.sin((Y1) / (2*np.pi))
U2, V2 = np.cos((X2 - 10) / (2*np.pi)), np.sin((Y2) / (2*np.pi))

#Calling and associating the plots separately. Same process as #1, but now
#using the colors argument
Q1 = plt.quiver(X1, Y1, U1, V1, color='r')
Q2 = plt.quiver(X2, Y2, U2, V2, color='b')
plt.axis([-6.2, 6.2, -6.2, 8])
plt.quiverkey(Q1, 0.78, 0.93, 1, 'reds')
plt.quiverkey(Q2, 0.93, 0.93, 1, 'blues')
plt.xticks([]), plt.yticks([])
plt.show()