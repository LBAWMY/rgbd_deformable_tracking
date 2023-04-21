import h5py
import numpy as np

f = h5py.File('/home/curl/CUHK/Projects/SoftSim/rgbd_deformable_tracking/cloth/cloth/towel/fold_diag_left_preprocessor.hdf5', 'r')
# rgbs = f['rgb']
depths = f['depth']
# T_w_k = np.array(f['T_w_k'])