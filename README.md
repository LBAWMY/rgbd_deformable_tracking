Tracking Deformable Objects with Point Clouds
========

This is an implementation of the tracking algorithm of the paper

    Tracking Deformable Objects with Point Clouds
    John D. Schulman, Alex Lee, Jonathan Ho and Pieter Abbeel
    In the proceedings of the International Conference on Robotics and Automation (ICRA), 2013.

(website: http://rll.berkeley.edu/tracking/)

This implementation tracks cloth only, using a position-based dynamics model (Mueller et al. 2007). The cloth simulation does not support self-collisions, unlike the Bullet-based simulation that was used in the original implementation used for the experiments in the paper.

Dependencies
-----
Required:

  - Python 2.7 (we create a anaconda environment for this project)
  - PyOpenGL >= 3.0.1
  - pygame >= 1.9.1
  - python-opencv
  - h5py
  - numpy
  - PCL == 1.8 (origin 1.6 is hard to compile)
  - Boost == 1.50, including Boost Python (full version compiled with Python 2.7)
  - Eigen 3 (Note: 3.0 needed, others may not work)

Optional:

  - PyCUDA >= 2012.1, for GPU support
  - rapprentice (http://rll.berkeley.edu/rapprentice) and its dependencies, for live tracking for a depth sensor on the head of a PR2

Building and running
-----
1. Download this source code, e.g. into `$SOURCE_DIR`
2. Make a build directory `$BUILD_DIR`
3. `cd $BUILD_DIR`
4. `cmake $SOURCE_DIR`
5. `make`
6. Add directories to `$PYTHONPATH`: `echo 'export PYTHONPATH=$SOURCE_DIR:$BUILD_DIR/lib:$PYTHONPATH' >> ~/.bashrc`
7. To generate the .h5 file from the raw rosbag file: 'python $SOURCE_DIR/cloth/record_rgbd_and_T.py ./cloth/towel/fold_double_preprocessor.bag --topic /preprocessor/kinect1/image /preprocessor/kinect1/depth /tf'
8. To run the tracker with example data (recorded depth camera videos): `python $SOURCE_DIR/scripts/tracker.py --input=recording.h5 [--gpu]`
