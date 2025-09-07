#=======================================
# WANNIER90 	
#=======================================

TOPDIR = /home/joseph/qe-7.4.1

F90=gfortran
FCOPTS=$(FFLAGS) -cpp 
LDOPTS=-g

LIBS = -L/usr/local/lib -llapack  -lblas   -lblas  
