# warp simulation for skewWake


### each case has the following file with * cooresponding to the rootname: 

- diagGaussian_*figure.png  :  .png figure showing the (x,y) space 
                              before (top left), after (top right), 
			      the structure and after a 0.51-m drift
			      
- diagGaussian_*_init.npz      :  structured file with initial macroparticle 
                              distribution			      

- diagGaussian_*_final.npz      : structured file with macroparticle 
                              distribution at the exit of the structure
			      
- diagGaussian_*_scrn.npz      : structured file with macroparticle 
                              distribution at the exit of the structure
			      
	     		      
### the two configurations run are

- diagGaussian_noUpperSlab: Gaussian beam above a single slab
- diagGaussian: Gaussian beam injected in the structure

For all cases the beam was located at (x,y)=(0,0) [yoffum=0] and only the tilt was varied. 

### the structure considered is:
- Ls  =  15e-2     # length of the structure
- W   =  50e-3     # along x
- a   =  0.914e-3/2.    # half vacuum gap
- b   =  a+5e-3    # half conductor gap 



_yoffum_00.0_tiltdeg_00.0_YYYYMMDD_HHMMSSfigure.png
