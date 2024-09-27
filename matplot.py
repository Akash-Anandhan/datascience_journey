import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
arr1 = [1,3,5,2,5,7,8,3,2,5]
arr2 = [0,8,6,7,4,6,4,6,7,4]
arr1.sort()
arr2.sort()

arr3 = [3,4,5,6,3,2,5,6,6,4,]
arr4 = [5,6,3,2,5,6,7,5,5,5,]
arr3.sort()
arr4.sort()
x = np.array(arr1)
y = np.array(arr2)

x1 = np.array(arr3)
y1 = np.array(arr4)

#TITLE AND AXIS LABELING
plt.title("plotting array ")
plt.xlabel("array 1 as x-axis ")
plt.ylabel("array 2 as y-axis")
plt.plot(x,y)
plt.show()

#LINEWIDTH PLOT
plt.title("LINEWIDTH PLOT ")
plt.plot(x,y , linewidth = 4 )
plt.show()

#PLOT WITH GRID PLANE
plt.title("PLOT WITH GRID PLANE")
plt.plot(x,y)
plt.grid()
plt.show()

#PLOT WITH ONLY ONE AXIS GRID
plt.title("PLOT WITH ONLY ONE AXIS GRID")
plt.plot(x,y )
plt.grid(axis='y')
plt.show()

#SUBPLOT
plt.title("SUBPLOT")
plt.subplot(1,2,1)
plt.plot(x,y)

plt.subplot(1,2,2)
plt.plot(x1,y1)

plt.show()

#SCATTER PLOT
plt.title("SCATTER PLOT ")
plt.scatter(x,y)
plt.scatter(x1,y1)
plt.show()


