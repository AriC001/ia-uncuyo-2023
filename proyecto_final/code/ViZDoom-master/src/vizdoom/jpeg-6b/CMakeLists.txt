cmake_minimum_required(VERSION 3.5)

make_release_only()

if( ZD_CMAKE_COMPILER_IS_GNUC_COMPATIBLE )
	set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wno-unused-parameter -fomit-frame-pointer" )
endif( ZD_CMAKE_COMPILER_IS_GNUC_COMPATIBLE )

add_library( jpeg
    jcomapi.c
    jdapimin.c
    jdapistd.c
    jdatasrc.c
    jdcoefct.c
    jdcolor.c
    jddctmgr.c
    jdhuff.c
    jdinput.c
    jdmainct.c
    jdmarker.c
    jdmaster.c
    jdmerge.c
    jdphuff.c
    jdpostct.c
    jdsample.c
    jerror.c
    jidctint.c
    jmemmgr.c
    jutils.c )
target_link_libraries( jpeg )
