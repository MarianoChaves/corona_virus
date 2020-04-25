from scipy.integrate import odeint
from scipy.stats import chisquare

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
	d  = +mu*h 
	return[ds, di, dh, d]

def cov_model(y0, N):
	x = odeint(covid, x0, t, args=(y0,N))
	return s, i, h, d

