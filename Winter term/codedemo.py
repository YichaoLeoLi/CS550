import scipy.integrate as integrate
import numpy as np


#Integration
result = integrate.quad(lambda x:x**2,0,1)#definite integral
print(result)

#If the function that's to be integrated takes additional parameters, the args argument can help quad identify the parameters in the function
from scipy.integrate import quad
def integrand(x, a, b):
	return a*x**2 + b

a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)


#integrating to infinite:

i = integrate.quad(lambda x:np.exp(x), np.NINF, 0)#This command integrates the function e^x from negative infinity to 0
print(i)


#multiple integration
area = integrate.dblquad(lambda x, y: x*y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)
print(area)


#inverse matrix
from scipy import linalg
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
linalg.inv(A)
print(A)



#solving linear system

A = np.array([[1,3,5],[2,5,1],[2,3,8]])
b = np.array([[10],[8],[3]])
x = np.linalg.solve(A, b)
print(x)


#Finding determinant

A = np.array([[1,3,5],[2,5,1],[2,3,8]])
print(linalg.det(A))


#Finding norms of a matrix

A=np.array([[1,2],[3,4]])

print(linalg.norm(A))

print(linalg.norm(A,'fro')) # frobenius norm is the default

print(linalg.norm(A,1)) # L1 norm (max column sum)

print(linalg.norm(A,-1))

print(linalg.norm(A,np.inf)) # L inf norm (max row sum)


#Finding eigenvalues and eigenvectors

A = np.array([[1, 2], [3, 4]])
la, v = linalg.eig(A)
l1, l2 = la
print(l1, l2)   # eigenvalues

print(v[:, 0])   # first eigenvector

print(v[:, 1])   # second eigenvector

#1-d interpolation

from scipy.interpolate import interp1d
x = np.linspace(0, 10, num=11, endpoint=True)
y = np.cos(-x**2/9.0)
print(x)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
xnew = np.linspace(0, 10, num=41, endpoint=True)
import matplotlib.pyplot as plt
plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()

#spline interpolation
x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
y = np.sin(x)
tck = interpolate.splrep(x, y, s=0)
xnew = np.arange(0, 2*np.pi, np.pi/50)
ynew = interpolate.splev(xnew, tck, der=0)
plt.figure()
plt.plot(x, y, 'x', xnew, ynew, xnew, np.sin(xnew), x, y, 'b')
plt.legend(['Linear', 'Cubic Spline', 'True'])
plt.axis([-0.05, 6.33, -1.05, 1.05])
plt.title('Cubic-spline interpolation')
plt.show()




