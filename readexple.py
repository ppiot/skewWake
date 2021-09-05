import  matplotlib.pyplot as plt 
import numpy as np
import sys
from matplotlib import gridspec
import matplotlib as mpl

arg = sys.argv
argnum = len(sys.argv)

fileoutput=arg[1]

filei=fileoutput+'_init.npz'
fileo=fileoutput+'_outpt.npz'
files=fileoutput+'_scrn.npz'

fileiN=np.load(filei)
xi=fileiN['xi']
yi=fileiN['yi']

fileoN=np.load(fileo)
xf=fileoN['xf']
yf=fileoN['yf']

fileiN=np.load(files)
xs=fileiN['xs']
ys=fileiN['ys']



plt.plot (xi, yi, '.',label='in')
plt.plot (xf, yf, '.',label='out')
plt.plot (xs, ys, '.',label='scrn')

plt.xlabel ('x (m)')
plt.ylabel ('y (m)')
plt.legend()

plt.tight_layout()
plt.show()



