cmake_minimum_required(VERSION 3.22)

project(zonedetect C CXX)
enable_testing()

find_package(GTest)
find_package(shapelib)

include(FetchContent)
set(CMAKE_TLS_VERIFY true)


add_subdirectory(library)
add_subdirectory(database)
add_subdirectory(test)

add_executable(zonedetect_demo)
target_sources(zonedetect_demo PRIVATE
    demo.c
)
target_link_libraries(zonedetect_demo PRIVATE zonedetect)
add_dependencies(zonedetect_demo zonedetect_db)
