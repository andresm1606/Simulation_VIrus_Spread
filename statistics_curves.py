import numpy as np
import matplotlib.pyplot as plt


# Data without precautions

data = np.loadtxt('Data.txt')

plt.figure(figsize=(7,2))
plt.xlim(0,50)
plt.ylim(0,200)
plt.xlabel('Tiempo')
plt.ylabel('Número de personas')

y = data[:,0] + data[:,1] 
y1 = y + data[:,2]


plt.fill_between(data[:,3],y,data[:,1], where = y > data[:,1], color='b')

plt.fill_between(data[:,3],data[:,1], color='brown')

plt.fill_between(data[:,3], y1, y, where = y1 >= y, color='g')

plt.savefig("No_precautions.png", bbox_inches='tight')

plt.close()


# Social distancing 

data = np.loadtxt('Data2.txt')

plt.figure(figsize=(7,2))
plt.xlim(0,50)
plt.ylim(0,200)
plt.xlabel('Tiempo')
plt.ylabel('Número de personas')

y = data[:,0] + data[:,1]
y1 = y + data[:,2]

plt.fill_between(data[:,3],y,data[:,1], where = y > data[:,1], color='b')

plt.fill_between(data[:,3],data[:,1], color='brown')

plt.fill_between(data[:,3], y1, y, where = y1 >= y, color='g')

plt.savefig("Social_distancing.png", bbox_inches='tight')

plt.close()

# Quarantine

data = np.loadtxt('Data3.txt')

plt.figure(figsize=(7,2))
plt.xlim(0,50)
plt.ylim(0,200)
plt.xlabel('Tiempo')
plt.ylabel('Número de personas')

y = data[:,0] + data[:,1]
y1 = y + data[:,2]

plt.fill_between(data[:,3],y,data[:,1], where = y > data[:,1], color='b')

plt.fill_between(data[:,3],data[:,1], color='brown')

plt.fill_between(data[:,3], y1, y, where = y1 >= y, color='g')

plt.savefig("Quarantine.png", bbox_inches='tight')

plt.close()
