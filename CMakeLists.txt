cmake_minimum_required(VERSION 3.22)

project(zonedetect C CXX)
enable_testing()

if(NOT EXISTS ${CMAKE_BINARY_DIR}/conaninfo.txt)
    execute_process(
        COMMAND conan install -s build_type=${CMAKE_BUILD_TYPE} --build=outdated ${CMAKE_SOURCE_DIR}
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
    list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
endif()

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
