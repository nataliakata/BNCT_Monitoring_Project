## FILES

## voxelised_jaszczak&detector

    - lattice_gen.py - writes the lattice_3d.txt that describes the layout of the voxels inside the phantom, made by AI;
    - lattice_3d.txt - contains the array that is used by the .inp file (by the infl function); 
    - voxel_jaszczak.inp - contains the voxelised Si plate as well as Jaszczak's phantom, as well as a T-Cross tally defining the light entering the Si plate from the LaBr region

## jaszczak_NAAL (lab set-up developed by dr. Michal Silarski -- michal.silarski@uj.edu.pl) and a Jaszczak's phantom (OLD VERSION)

    - collimated.inp - NAAL with a Jaszczak's phantom placed beneath the neutron source, where the detector consists of the LaBr3 region and layers of Al and Pb;
    - standard.inp - NAAL with a Jaszczak's phantom model and a detector represeted by the LaBr3 region wrapped in Al;
