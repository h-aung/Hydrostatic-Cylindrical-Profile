#!/usr/bin/env python

import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import quad

#differential equation, ostriker 1964, eq: 10
def func(y,t,n):
    #if t!=0, 
    if t!=0:
        return [y[1],-(y[0]**n)-y[1]/t]
    else:
        return [y[1],-(y[0]**n)]

#for a given gamma, it generates normalized mass per unit length and density as a function of position. 
def gen_interpolate(gamma):
    n=1./(gamma-1)
    y0= [1,0] #[y(0), y'(0)], r=0 values
    t = np.arange(0,9,0.0001)

    y = odeint(func,y0,t,args=(1/(gamma-1),),mxstep=5000000)

    t=t[~np.isnan(y[:,0])]
    dat=y[:,0][~np.isnan(y[:,0])]
    
    massfunc = lambda x: x*np.interp(x,t,dat**(1/(gamma-1)))
    #maximum mpl for hydrostatic
    lambdacrit = quad(massfunc,0,np.amax(t))[0] 
    
    x=np.linspace(0.1,2.5,num=1000)
    dens = np.interp(x,t,dat**(1/(gamma-1)))
    mu = np.zeros(len(x))
    for i in range(len(x)):
        mu[i] = quad(massfunc,0,x[i])[0]/lambdacrit
    
    np.save('mpl_interpolate_%.2f.npy'%(gamma),[mu,dens,x])
    return

#reload mpl values calculated, and find where stream should end
#mu defined in Aung+ 19
def profile(gamma,mu,delta):
    [mpl,dens,x] = np.load('mpl_interpolate_%.2f.npy'%(gamma))
    densfunc = interp1d(mpl, dens)
    xcutfunc = interp1d(mpl, x)
    
    #find density at edge of stream for mu=mu, see md file for associated equation
    yRin = densfunc(mu) 
    yRout = 1./delta 
    alpha = yRin/yRout
    
    #differential equation
    y0= [1,0] #[y0, y'0]
    t = np.arange(0,9,0.0001)
    
    n=1./(gamma-1)
    y = odeint(func,y0,t,args=(n,),mxstep=5000000)
    t=t[~np.isnan(y[:,0])]
    dat=y[:,0][~np.isnan(y[:,0])]
    dat = dat**(1/(gamma-1)) #this is density
    
    mask = dat>yRin
    ##dens and r inside the stream
    densin = dat[mask]
    rin = t[mask]
    rstream = rin[-1]
    print "rratio, rstream/rc is %.4f"%rstream
    ##starting point (bc) for outside the stream
    tstart = t[len(rin)-1]*alpha**(-gamma/2)
    y0 = [y[len(rin)-1,0]/alpha**(gamma-1),y[len(rin)-1,1]*alpha**(-(gamma/2))]
    t = np.arange(tstart,10,0.001*alpha**(-gamma/2))
    y = odeint(func,y0,t,args=(1/(gamma-1),),mxstep=5000000)
    t=t[~np.isnan(y[:,0])]
    dat=y[:,0][~np.isnan(y[:,0])]
    dat = dat**(1/(gamma-1)) 
    densout = dat
    rout = t*alpha**(gamma/2)
    dens = np.concatenate((densin,densout[1:]))
    r = np.concatenate((rin,rout[1:]))/rstream
    print "density at and inside Rs: %.5f"%(densin[-1])
    
    P = np.concatenate((densin**gamma,(alpha*densout[1:])**gamma))
    ind=r==1.0
    pedge = P[ind][0]
    print "pressure at Rs: %.5f"%(P[ind])
    
    mask = r<30
    f=open('test.txt','w')
    #f.write("#r/R_s dens/dens(0) pres/pres(0)\n")
    for i in range(len(r)):
        f.write("%.5e %.5e %.5e\n"%(r[i],dens[i],P[i]))
    f.close()
    return
    
def main():
    gamma = 5./3
    mu = 0.1
    delta = 100.
    #only need to run this once for every gamma
    gen_interpolate(gamma)
    profile(gamma,mu,delta)
    return 
    
if __name__=="__main__":
    main()