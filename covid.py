# COVID-19 Simulation;

import numpy as np
from scipy.integrate import odeint
from scipy.stats import chisquare

import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates

import pandas as pd
import datetime

N=100000	#population
g  = 1/15.	#incubation time
R0_test = 4.0		#number of transmission per person
mu = 0.02	#death rate 2%
Tq = 24		#Quarantine day after the first case

start = datetime.date(2020, 4, 3)
end = datetime.date(2020, 12, 30)
days = (end - start).days
N_analysis = (datetime.date(2020, 3, 18)-datetime.date(2020, 4, 3)).days

def read():
	dat = pd.read_csv('data/COVID19_20200402.csv',delimiter=';', index_col="estado")
	dat = dat.loc[['RJ'],['data','obitosAcumulados']]
	dat = dat[dat['obitosAcumulados'] != 0]
	time_date = pd.to_datetime(dat['data'], format='%d/%m/%Y')
	number_of_deaths = dat['obitosAcumulados']

	return number_of_deaths, time_date


def covid(x,t,y,N):
	b = y[0]
	g = y[1]
	mu = y[2]	

	s = x[0]
	i = x[1]
	h = x[2]
	d = x[3]
	
	ds = -b*i*s/N
	di = +b*i*s/N-g*i
	dh = +g*i
	d  = +g*i*mu 
	return[ds, di, dh, d]


d_data, time_data = read()


time_model = []
time_deaths = []
uti = []
for i in range(0, int(days), 1):
	uti.append(40)
	time_model.append(start + datetime.timedelta(days=i))
	time_deaths.append(start + datetime.timedelta(days=i)-datetime.timedelta(days=14))

def statistical_test(f_obs):
	chimin=100000
	dmin=100000
	M=300
	bfp = 0
	CL90 = []
	x0 = [N, 10, 0, 0]
	t = np.linspace(0,int(days),int(days))
	for i in range(0,M,1):
		chi=0
		R0 = 1.0+4./M*i
		y0  = [g*R0,g,mu]
		x = odeint(covid, x0, t, args=(y0,N))
		d = x[:,3]

		chi, p = chisquare(f_obs[:], d[7:(len(f_obs)+7)], ddof=1, axis=0)

		if(chi<chimin):
			chimin=chi
			bfp = R0





	for i in range(0,M,1):
		R0 = 1.0+5./M*i
		y0  = [g*R0,g,mu]
		x = odeint(covid, x0, t, args=(y0,N))
		d = x[:,3]

		chi, p = chisquare(f_obs, d[7:(len(f_obs)+7)], ddof=1, axis=0)

		if((chi-chimin)<6.63):
			CL90.append(R0)

	return bfp, CL90

#bfp, CL90 = statistical_test(d_data)
#CLmin = min(CL90)
#CLmax = max(CL90)
#print(bfp, CLmin, CLmax)

N=100000	#population
g  = 1/7.	#incubation time
R0_test = 1.5		#number of transmission per person
mu = 0.02	#death rate 2%
Tq = 24		#Quarantine day after the first case

t = np.linspace(0,int(days),int(days))
x0 = [N, 2, 0, 0]
y0  = [g*R0_test,g,mu]

x = odeint(covid, x0, t, args=(y0,N))

s = x[:,0]
i = x[:,1]
h = x[:,2]
d = x[:,3]

plt.style.use('seaborn')
#plt.plot_date(time_data, d_data, linestyle='solid',label='Dados 4 de Abril de 2020')
plt.xlim([datetime.date(2020, 3, 18), datetime.date(2020, 12, 1)])
plt.ylim([0, 250])

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%b, %d')
plt.gca().xaxis.set_major_formatter(date_format)

#plt.plot_date(time_model,h, linestyle='solid',label='SIR Model')
plt.plot_date(time_model,i*0.004*2, linestyle='-',label='pessoas precisando de atendimento medico\nsem distanciamento social', fillstyle = 'bottom', marker = ',')
#plt.plot_date(time_deaths,d, linestyle='--',label='numero de mortos sem distanciamento social', fillstyle = 'bottom', marker = ',')

N=100000	#population
g  = 1/7.	#incubation time
R0_test = 1.9		#number of transmission per person
mu = 0.02	#death rate 2%
Tq = 24		#Quarantine day after the first case

t = np.linspace(0,int(days),int(days))
x0 = [N, 2, 0, 0]
y0  = [g*R0_test,g,mu]

x = odeint(covid, x0, t, args=(y0,N))

s = x[:,0]
i = x[:,1]
h = x[:,2]
d = x[:,3]

plt.plot_date(time_model,i*0.0037*2, linestyle='-',label='pessoas precisando de atendimento medico\ncom distanciamento social', fillstyle = 'bottom', marker = ',')
#plt.plot_date(time_deaths,d, linestyle='--',label='numero de mortos com distanciamento social', fillstyle = 'bottom', marker = ',')

plt.plot_date(time_model,uti, linestyle='-',label='numero de leitos disponiveis na cidade', fillstyle = 'bottom', marker = ',')
plt.legend(frameon = True, loc = 'upper right', ncol=1)
plt.ylabel('numero de pessoas')
plt.title('COVID-19 em Barra do Pirai')
plt.show()
