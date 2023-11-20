cmake_minimum_required(VERSION 3.22)

project(zonedetect C CXX)

enable_testing()

# download CPM.cmake
file(
    DOWNLOAD
    https://github.com/cpm-cmake/CPM.cmake/releases/download/v0.38.3/CPM.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/cmake/CPM.cmake
    EXPECTED_HASH SHA256=cc155ce02e7945e7b8967ddfaff0b050e958a723ef7aad3766d368940cb15494
)
include(${CMAKE_CURRENT_BINARY_DIR}/cmake/CPM.cmake)

CPMAddPackage(
    NAME shapelib
    VERSION 1.5.0
    GITHUB_REPOSITORY "OSGeo/shapelib"
    GIT_TAG "v1.5.0"
    OPTIONS "BUILD_SHARED_LIBS OFF"
)
target_include_directories(shp INTERFACE ${shapelib_SOURCE_DIR})

CPMAddPackage("gh:google/googletest@1.14.0")

include(FetchContent)
set(CMAKE_TLS_VERIFY true)

add_subdirectory(library)
add_subdirectory(database)
# add_subdirectory(test)

add_executable(zonedetect_demo)
target_sources(zonedetect_demo PRIVATE
    demo.c
)
target_link_libraries(zonedetect_demo PRIVATE zonedetect)
add_dependencies(zonedetect_demo zonedetect_db)
