cmake_minimum_required(VERSION 3.22)

project(zonedetect C CXX)

set(CMAKE_CXX_STANDARD 20)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
   file(DOWNLOAD
        "https://raw.githubusercontent.com/conan-io/cmake-conan/master/conan.cmake"
        "${CMAKE_BINARY_DIR}/conan.cmake"
        TLS_VERIFY ON
        )
endif()
include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_configure(
    REQUIRES
        shapelib/1.5.0
    GENERATORS
        cmake_find_package
    OPTIONS
        *:shared=False
    )
conan_cmake_autodetect(settings)
conan_cmake_install(
    PATH_OR_REFERENCE .
    BUILD outdated
    SETTINGS ${settings}
    )

find_package(shapelib)

include(FetchContent)
set(CMAKE_TLS_VERIFY true)


add_subdirectory(library)
add_subdirectory(database)

add_executable(zonedetect_demo)
target_sources(zonedetect_demo PRIVATE
    demo.c
)
target_link_libraries(zonedetect_demo PRIVATE zonedetect)
add_dependencies(zonedetect_demo zonedetect_db)
