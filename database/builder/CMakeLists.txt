add_executable(zonedetect_builder)
target_sources(zonedetect_builder PRIVATE
    builder.cpp
)
target_link_libraries(zonedetect_builder PRIVATE
    shp
)

FetchContent_Declare(naturalearthdata
    URL https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/10m/cultural/ne_10m_admin_0_countries_lakes.zip
    URL_HASH SHA256=3f1596b05b4a19bd97f3a54731497cffbb4dbed4cda494084e73dd6dd3d37264
)
FetchContent_MakeAvailable(naturalearthdata)

FetchContent_Declare(timezonedata
    URL https://github.com/evansiroky/timezone-boundary-builder/releases/download/2021c/timezones-with-oceans.shapefile.zip
    URL_HASH SHA256=8eabf4ad0ecb4660ebcb149b3e11c621c75e9e127e2cfceb789e1cdc74ea6fa8
)
FetchContent_MakeAvailable(timezonedata)

set(DB_FILES)

foreach(P IN ITEMS 16 21)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/out/country${P}.bin
        DEPENDS zonedetect_builder
        COMMAND zonedetect_builder C ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${CMAKE_BINARY_DIR}/out/country${P}.bin ${P} "Made with Natural Earth, placed in the Public Domain." 0
    )
    list(APPEND DB_FILES ${CMAKE_BINARY_DIR}/out/country${P}.bin)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/out_v1/country${P}.bin
        DEPENDS zonedetect_builder
        COMMAND zonedetect_builder C ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${CMAKE_BINARY_DIR}/out_v1/country${P}.bin ${P} "Made with Natural Earth, placed in the Public Domain." 1
    )
    list(APPEND DB_FILES ${CMAKE_BINARY_DIR}/out_v1/country${P}.bin)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/out/timezone${P}.bin
        DEPENDS zonedetect_builder
        COMMAND zonedetect_builder T ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${timezonedata_SOURCE_DIR}/combined-shapefile-with-oceans ${CMAKE_BINARY_DIR}/out/timezone${P}.bin ${P} "Contains data from Natural Earth, placed in the Public Domain. Contains information from https://github.com/evansiroky/timezone-boundary-builder, which is made available here under the Open Database License (ODbL)." 0
    )
    list(APPEND DB_FILES ${CMAKE_BINARY_DIR}/out/timezone${P}.bin)
    add_custom_command(
        OUTPUT ${CMAKE_BINARY_DIR}/out_v1/timezone${P}.bin
        DEPENDS zonedetect_builder
        COMMAND zonedetect_builder T ${naturalearthdata_SOURCE_DIR}/ne_10m_admin_0_countries_lakes ${timezonedata_SOURCE_DIR}/combined-shapefile-with-oceans ${CMAKE_BINARY_DIR}/out_v1/timezone${P}.bin ${P} "Contains data from Natural Earth, placed in the Public Domain. Contains information from https://github.com/evansiroky/timezone-boundary-builder, which is made available here under the Open Database License (ODbL)." 1
    )
    list(APPEND DB_FILES ${CMAKE_BINARY_DIR}/out_v1/timezone${P}.bin)
endforeach()

add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/db.zip
    COMMAND ${CMAKE_COMMAND} -E tar "cf" ${CMAKE_BINARY_DIR}/db.zip --format=zip -- ${CMAKE_BINARY_DIR}/out ${CMAKE_BINARY_DIR}/out_v1
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    DEPENDS ${DB_FILES}
)

add_custom_target(zonedetect_db
    DEPENDS ${CMAKE_BINARY_DIR}/out_v1/timezone21.bin
)

add_custom_target(zonedetect_db_zip
    DEPENDS ${CMAKE_BINARY_DIR}/db.zip
)
