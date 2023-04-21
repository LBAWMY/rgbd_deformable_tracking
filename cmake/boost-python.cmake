function(boost_python_module NAME)
  set(BOOST_ROOT "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
  set(BOOST_LIBRARYDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib")
  set(BOOST_INCLUDEDIR "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/include")
  find_package(Boost 1.50 COMPONENTS system python thread program_options EXACT)

  set(Python2_ROOT_DIR "/home/curl/anaconda3/envs/rgbd_tracking")
  set(PYTHON_INCLUDE_DIRS "/home/curl/anaconda3/envs/rgbd_tracking/include/python2.7")
  set(PYTHON_LIBRARIES "/home/curl/anaconda3/envs/rgbd_tracking/lib/libpython2.7.so")
  find_package(Python2 REQUIRED)
  find_package(PythonLibs REQUIRED)

  #set(PYTHON_INCLUDE_DIR "/home/curl/anaconda3/envs/rgbd_tracking/include/python2.7")
  #set(PYTHON_LIBRARY "/home/curl/anaconda3/envs/rgbd_tracking/lib/libpython2.7.so")
  #find_package(PythonLibs 2 REQUIRED)
  #set(PYTHON_LIBRARIES "libboost_python-py27.so")
  #find_package(Boost COMPONENTS python REQUIRED)

  set(PYTHON_NUMPY_INCLUDE_DIR "/home/curl/anaconda3/envs/rgbd_tracking/lib/python2.7/site-packages/numpy/core/include")
  include_directories(${PYTHON_NUMPY_INCLUDE_DIR})
  find_package(Numpy)

  set(Boost_PYTHON_LIBRARY "/home/curl/CUHK/Projects/PACKAGES/boost_1_50_0/local/lib/libboost_python.so")
  set(PYTHON_INCLUDE_PATH "/home/curl/anaconda3/envs/rgbd_tracking/include/python2.7")
  message(STATUS "Boost_PYTHON_LIBRARY: ${Boost_PYTHON_LIBRARY}")
  message(STATUS "PYTHON_INCLUDE_PATH: ${PYTHON_INCLUDE_PATH}")
  message(STATUS "Boost_INCLUDE_DIR: ${Boost_INCLUDE_DIR}")
  set(DEP_LIBS
    ${Boost_PYTHON_LIBRARY}
    ${PYTHON_LIBRARIES}
    )
  #these are required includes for every ecto module
  include_directories(
    ${PYTHON_INCLUDE_PATH}
    ${Boost_INCLUDE_DIR}
    )
  add_library(${NAME} SHARED
    ${ARGN}
    )
  set_target_properties(${NAME}
    PROPERTIES
    OUTPUT_NAME ${NAME}
    COMPILE_FLAGS "${FASTIDIOUS_FLAGS}"
    LINK_FLAGS -dynamic
    PREFIX ""
  )
  if( WIN32 )
    set_target_properties(${NAME} PROPERTIES SUFFIX ".pyd")
  elseif( APPLE OR ${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    # on mac osx, python cannot import libraries with .dylib extension
    set_target_properties(${NAME} PROPERTIES SUFFIX ".so")
  endif()  
  target_link_libraries(${NAME}
    ${DEP_LIBS}
    )
endfunction()
