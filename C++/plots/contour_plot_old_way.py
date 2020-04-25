import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import math

t14,dm41=np.loadtxt("CL_90.dat",dtype=float,delimiter="\t",usecols=(0,1),comments="#",unpack=True)

fig, axes = plt.subplots()


axes.plot(t14,dm41)


y_axis_NAME='$\\Delta m^2[eV]^2$'
x_axis_NAME='$\\sin^22\\theta$'

axes.set_xscale('log')
axes.set_yscale('log')
axes.set_xlim([0.01,1.0])
axes.set_ylim([0.003,20.0])
axes.set_ylabel(y_axis_NAME)
axes.set_xlabel(x_axis_NAME)

plt.title('Bugey')
#plt.text(0.3,5,'$\\chi^2_{min}=$'+str(chi2min))
plt.savefig('th14_dm41.pdf') 
plt.show()




