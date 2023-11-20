add_executable(zonedetect_test)
target_compile_definitions(zonedetect_test PRIVATE
    DB_PATH="${PROJECT_BINARY_DIR}/out_v1/timezone21.bin"
)
target_sources(zonedetect_test PRIVATE
    test.cpp
)
target_link_libraries(zonedetect_test PRIVATE
    GTest::gtest_main
    zonedetect
)
add_dependencies(zonedetect_test zonedetect_db)

include(GoogleTest)
gtest_discover_tests(zonedetect_test)
