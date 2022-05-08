from conans import ConanFile, CMake, tools


class LibConan(ConanFile):
    name = "ZoneDetect"
    version = "1.0"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    settings = [ "os", "compiler", "build_type", "arch", "cppstd" ]
    requires = [
        "shapelib/1.5.0",
        "gtest/1.11.0",
    ]
    generators = "cmake_find_package"
    exports_sources = "*"

    def build(self):
        # it will find the packages by using our auto-generated FindXXX.cmake files
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="library")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("timezone21.bin", dst="include", src="out_v1", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = [ "zonedetect" ]
