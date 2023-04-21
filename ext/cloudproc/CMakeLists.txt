find_package(PCL 1.8.1 EXACT)
add_definitions(${PCL_DEFINITIONS})

include_directories(SYSTEM ${PCL_INCLUDE_DIRS} /usr/include/openni)
link_directories(${PCL_LIBRARY_DIRS})

set(VTK_DIR "/usr/local/lib/cmake/vtk-7.1")
find_package(VTK REQUIRED)
link_directories(${VTK_LIBRARY_DIRS})

set(BOOST_ROOT "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
set(BOOST_LIBRARYDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib")
set(BOOST_INCLUDEDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
find_package(Boost 1.50 EXACT)

include_directories(
  SYSTEM
  ${VTK_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
  ${Eigen_INCLUDE_DIRS}
  ${PYTHON_INCLUDE_DIRS}
  ${HACD_INCLUDE_DIRS}
)

if (APPLE)
	include_directories("/usr/local/Cellar/vtk/5.10.0/include/vtk-5.10")
endif()

#include_directories("/usr/local/include/vtk-7.1")
#link_directories("/usr/local/lib")
link_directories(${BOOST_LIBRARYDIR})

#set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fvisibility=hidden -Wno-deprecated")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")

boost_python_module(cloudprocpy cloudprocpy.cpp
  cloudproc.cpp
  sphere_sampling.cpp
  mesh_simplification.cpp
  vtkQuadricDecimation2.cxx
  cloudgrabber.cpp)
set(Boost_THREAD_LIBRARY "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib/libboost_thread.so")
message("Boost_THREAD_LIBRARY: ${Boost_THREAD_LIBRARY}")
message("Boost_LIBRARIES: ${Boost_LIBRARIES}")
message("Boost_LIBRARIES: ${Boost_LIBRARIES}")
message("Boost_INCLUDE_DIRS: ${Boost_INCLUDE_DIRS}")
target_link_libraries(cloudprocpy ${VTK_LIBRARIES} ${Boost_PYTHON_LIBRARY} ${PYTHON_LIBRARIES} ${BOOST_LIBRARYDIR} ${PCL_LIBRARIES} ${Boost_THREAD_LIBRARY})
#add_executable(simplify_test simplify_test.cpp)
#target_link_libraries(simplify_test ${PCL_LIBRARIES} cloudproc ${PCL_LIBRARIES})