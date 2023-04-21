set(Python2_ROOT_DIR "/home/curl/anaconda3/envs/rgbd_tracking")
set(PYTHON_INCLUDE_DIRS "/home/curl/anaconda3/envs/rgbd_tracking/include/python2.7")
set(PYTHON_LIBRARIES "/home/curl/anaconda3/envs/rgbd_tracking/lib/libpython2.7.so")
find_package(PythonInterp REQUIRED)
find_package(PythonLibs REQUIRED)

set(BOOST_ROOT "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
set(BOOST_LIBRARYDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib")
set(BOOST_INCLUDEDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
find_package(Boost 1.50 EXACT)

include_directories(
  SYSTEM
  ${Boost_INCLUDE_DIR}
  ${EIGEN_INCLUDE_DIR}
  ${PYTHON_INCLUDE_DIRS}
  ${BULLET_INCLUDE_DIRS}
)

if (NOT APPLE)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=hidden")
endif()

add_executable(test_npeigen
  test_npeigen.cpp
  npeigen.cpp
)
set(Boost_PYTHON_LIBRARY "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib/libboost_python.so")
target_link_libraries(test_npeigen ${Boost_PYTHON_LIBRARY} ${PYTHON_LIBRARIES} ${Boost_THREAD_LIBRARY})

set(PYTHON_NUMPY_INCLUDE_DIR "/home/curl/anaconda3/envs/rgbd_tracking/lib/python2.7/site-packages/numpy/core/include")
include_directories(${PYTHON_NUMPY_INCLUDE_DIR})
message(STATUS "PYTHON_NUMPY_INCLUDE_DIR: ${PYTHON_NUMPY_INCLUDE_DIR}")
boost_python_module(ctrackingpy
  python_interface.cpp
  mass_system.cpp
  npeigen.cpp
  bullet_unity.cpp
)
message(STATUS "BOOST_LIBRARY: ${BOOST_LIBRARY}")
message(STATUS "BOOST_SYSTEM_LIBRARY: ${BOOST_SYSTEM_LIBRARY}")
target_link_libraries(ctrackingpy ${Boost_PYTHON_LIBRARY})
