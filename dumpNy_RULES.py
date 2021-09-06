import  matplotlib.pyplot as plt 
import numpy as np
import sys 
import os
from matplotlib import gridspec
import matplotlib as mpl

from openpmd_viewer import OpenPMDTimeSeries
from openpmd_viewer.addons import LpaDiagnostics


arg = sys.argv
argnum = len(sys.argv)

filedir=arg[1]+'/hdf5/'
#fileoutput=arg[2]
fileoutput=arg[1]

Drift=0.51


ts = LpaDiagnostics(filedir)

N_iterations = len(ts.iterations)


zi, uzi = ts.get_particle( ['z','uz'],  species='beam', iteration=ts.iterations[1])
zf, uzf = ts.get_particle( ['z','uz'],  species='beam', iteration=ts.iterations[N_iterations-1])
yi, uyi = ts.get_particle( ['y','uy'],  species='beam', iteration=ts.iterations[1])
yf, uyf = ts.get_particle( ['y','uy'],  species='beam', iteration=ts.iterations[N_iterations-1])
xi, uxi = ts.get_particle( ['x','ux'],  species='beam', iteration=ts.iterations[1])
xf, uxf = ts.get_particle( ['x','ux'],  species='beam', iteration=ts.iterations[N_iterations-1])



xs=xf+uxf/uzf*Drift
ys=yf+uyf/uzf*Drift


fig=plt.figure()
ax1 = plt.subplot(221)
ax1.hexbin(xi*1e3, yi*1e3, cmap=plt.cm.plasma, gridsize=512, mincnt=1)
ax1.set_xlim([-10,10])
ax1.set_ylim([-10,10])
#ax1.set_xlabel ('x (mm)')
ax1.set_ylabel ('y (mm)')
fig.suptitle(arg[1])

ax2= plt.subplot(222)
ax2.hexbin(xf*1e3, yf*1e3, cmap=plt.cm.plasma, gridsize=512, mincnt=1)
ax2.set_xlim([-10,10])
ax2.set_ylim([-10,10])
ax2.set_xlabel ('x (mm)')
#ax2.set_ylabel ('y (mm)')


ax3= plt.subplot(223)
ax3.hexbin(xs*1e3, ys*1e3, cmap=plt.cm.plasma, gridsize=512, mincnt=1)
ax3.set_xlim([-10,10])
ax3.set_ylim([-10,10])
ax3.set_xlabel ('x (mm)')
ax3.set_ylabel ('y (mm)')


ax1.text(-5,5,'entrance',color='red',size=11)
ax2.text(-5,5,'exit',color='red',size=11)
ax3.text(-5,5,'exit+0.51-m drift',color='red',size=11)


filefig=fileoutput+'figure.png'
plt.savefig(filefig)


filei=fileoutput+'_init'
fileo=fileoutput+'_outpt'
files=fileoutput+'_scrn'

np.savez(filei, xi=xi, yi=yi, zi=zi, uxi=uxi, uyi=uyi, uzi=uzi) 
np.savez(fileo, xf=xf, yf=yf, zf=zf, uxf=uxf, uyf=uyf, uzf=uzf)
np.savez(files, xs=xs, ys=ys, zs=zf, uxs=uxf, uys=uyf, uzs=uzf)


os.system('mv '+filei+'.npz '+'skewWake_repo')
os.system('mv '+fileo+'.npz '+'skewWake_repo')
os.system('mv '+files+'.npz '+'skewWake_repo')
os.system('mv '+filefig+' skewWake_repo')
os.system('cp dumpNpy.py skewWake_repo')
os.system('cp readexple.py skewWake_repo')


