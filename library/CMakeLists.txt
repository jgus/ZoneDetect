add_library(zonedetect STATIC)
target_include_directories(zonedetect PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_sources(zonedetect PRIVATE
    zonedetect.c
)
