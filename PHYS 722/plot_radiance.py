
if __name__ == "__main__":

   # import libraries
   import numpy as np
   import matplotlib.pyplot as plt
   import pyunlvrtm as pu

   # unl-vrtm output filename
   filename = 'myfirstrun.unlvrtm.nc' 

   # read Stokes
   data = pu.read_unlvrtm( filename )
 
   #-- check what variables have been read
   print( list(data.keys()) )

   #-- copy wavelength and Stokes
   wavelength = data['Lamdas']
   stokes     = data['Stokes']

   #--  check the dimensions 
   print( wavelength.shape, stokes.shape )

   # make a plot
   plt.plot(wavelength,stokes)
   plt.xlabel('Wavelength (nm)')
   plt.ylabel('Normalized Radiance')
   plt.show()
   plt.close()
