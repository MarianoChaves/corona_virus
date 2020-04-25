import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm
import math

t14,dm41=np.loadtxt("chisq.dat",dtype=float,delimiter="\t",usecols=(0,1),comments="#",unpack=True)

N=100




histogram2D=np.zeros((N,N))
ax=np.zeros(N)
ay=np.zeros(N)




for i in range(0,N):
	for j in range(0,N):
		histogram2D[i][j]=4000

chi2min=2e10


t14max = math.log10(0.0001)
t14min = math.log10(2.00)

dm41max = math.log10(20.0)
dm41min = math.log10(0.001)

dt14=(t14max-t14min)/N
ddm41=(dm41max-dm41min)/N

for i in range(0,N):
	ax[i]=math.pow(10,t14min+dt14*i)
	ay[i]=math.pow(10,dm41min+ddm41*i)



for i in range(0,len(chi2)-1):

	line = int((t14[i]-t14min)/dt14)
	collumm = int((dm41[i]-dm41min)/ddm41)

	if chi2[i]<histogram2D[line][collumm]:
		histogram2D[line][collumm]=chi2[i]

	if chi2[i]<chi2min:
		chi2min=chi2[i]
		bft14=pow(10,t14[i])
		bfdm41=dm41[i]



fig = plt.figure()
axes=fig.add_subplot(1,1,1, axisbg="1.0")


ax1=[]
ay1=[]
az1=[]


for i in range(0,N):
	for j in range(0,N):
		if histogram2D[i][j]<chi2min+100.0:
			ax1.append(ax[i])
			ay1.append(ay[j])
			az1.append(histogram2D[i][j]-chi2min)




#triang = tri.Triangulation(ax1, ay1)
#refiner = tri.UniformTriRefiner(triang)
#tri_refi, z_test_refi = refiner.refine_field(az1, subdiv=3)
#axes.set_aspect('equal')
#axes.tricontourf(tri_refi,z_test_refi,levels=[0.0,2.30,6.18,11.83],cmap='Reds')


axes.tricontour(ax1,ay1,az1,levels=[4.61],linestyles=['solid'])
#axes.tricontourf(ax1,ay1,az1,levels=[0.0,6.18,11.83],cmap='Reds')
#axes.tripcolor(ax1,ay1,az1)

axes.scatter(bft14, bfdm41,c='black',edgecolors='none',s=20)

#proxy = [plt.Rectangle((0,0),1,1,fc = pc.get_facecolor()[0]) 
#    for pc in axes.collections]

#plt.legend(proxy, ['2$\\sigma$','3$\\sigma$'],loc='upper right')

y_axis_NAME='$\\Delta m^2[eV]^2$'
x_axis_NAME='$\\sin^22\\theta$'

axes.set_xscale('log')
axes.set_yscale('log')
axes.set_xlim([0.01,1.0])
axes.set_ylim([0.003,20.0])
axes.set_ylabel(y_axis_NAME)
axes.set_xlabel(x_axis_NAME)

plt.title('Bugey')
plt.text(0.3,5,'$\\chi^2_{min}=$'+str(chi2min))
plt.savefig('th14_dm41.pdf') 
plt.show()




