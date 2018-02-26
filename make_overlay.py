# Radio/optical overlap of NGC5128: Generate an overlay map of Centaurus A
# Usage: >> python make_overlay.py
# V.A. Moss (vmoss.astro@gmail.com)

# Imports
import aplpy
from pylab import *
from matplotlib import rc
rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['serif'],'size':18})

# Specify position of central black hole
cal_ra = +201.365064
cal_dec = -43.019112

# Load optical image and set colourscale
f = aplpy.FITSFigure('optical.fits',figsize=(10,8))
f.show_colorscale(cmap='Greys',stretch='linear')

# Add a grid
f.add_grid()
f.grid.set_color('black')
f.grid.set_alpha(0.3)

# Show the radio contours
f.show_contour('radio.fits',colors='w',levels=[1,5,10,15,20,25,30])

# Add title, colorbar, marker
title('NGC 5128')
f.show_colorbar()
f.colorbar.set_axis_label_text('Photon counts')
f.show_markers(cal_ra,cal_dec,marker='x',facecolor='r',edgecolor='r',s=100)

# Save figure
savefig('opticalwithradiocontours.pdf',bbox_inches='tight',transparent=True)