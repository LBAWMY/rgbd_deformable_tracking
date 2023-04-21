cmake_minimum_required(VERSION 2.8)
project(tracking)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/modules")

option(DEVEL_MODE "build with compiler more errors" OFF)
if (DEVEL_MODE) 
  set(CMAKE_CXX_FLAGS "-Werror -Wall -Wno-sign-compare")
endif(DEVEL_MODE)

set(CMAKE_INCLUDE_SYSTEM_FLAG_CXX "-isystem ")        

# http://cmake.3232098.n2.nabble.com/Default-value-for-CMAKE-BUILD-TYPE-td7550756.html
if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
  message(STATUS "Setting build type to 'Release' as none was specified.")
  set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose the type of build." FORCE)
  # Set the possible values of build type for cmake-gui
  set_property(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release"
    "MinSizeRel" "RelWithDebInfo")
endif()

set(EIGEN_INCLUDE_DIR "/home/curl/CUHK/Projects/PACKAGES/eigen-3.0.5/eigen/local/include/eigen3")
find_package(Eigen REQUIRED)
set(BOOST_ROOT "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
set(BOOST_LIBRARYDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib")
set(BOOST_INCLUDEDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
find_package(Boost 1.50 COMPONENTS system python thread program_options EXACT)

set(Python2_ROOT_DIR "/home/curl/anaconda3/envs/rgbd_tracking")
set(PYTHON_INCLUDE_DIRS "/home/curl/anaconda3/envs/rgbd_tracking/include/python2.7")
set(PYTHON_LIBRARIES "/home/curl/anaconda3/envs/rgbd_tracking/lib/libpython2.7.so")
find_package(PythonInterp REQUIRED)
#find_package(Python2 REQUIRED)
find_package(PythonLibs REQUIRED)

set(VTK_DIR "/usr/local/lib/cmake/vtk-7.1")
find_package(VTK REQUIRED)
include_directories(${VTK_INCLUDE_DIRS})
link_directories(${VTK_LIBRARY_DIRS})
message(STATUS "VTK_VERSION: ${VTK_VERSION}")
message(STATUS "VTK_LIBRARIES: ${VTK_LIBRARIES}")
message(STATUS "VTK_INCLUDE_DIRS: ${VTK_INCLUDE_DIRS}")

set(PCL_DIR "/usr/local/pcl181/local/share/pcl-1.8")
find_package(PCL 1.8.1 EXACT)

include_directories("/opt/ros/melodic/include")
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  geometry_msgs
  tf
)

set(BULLET_INCLUDE_DIRS ${CMAKE_SOURCE_DIR}/ext/bullet/src)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

include("${CMAKE_SOURCE_DIR}/cmake/boost-python.cmake")

add_subdirectory(src)
add_subdirectory(ext/cloudproc)
