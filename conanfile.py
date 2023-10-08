from conan import ConanFile
from conan.tools.cmake import CMake
from conan.tools import files
from os.path import join

class LibConan(ConanFile):
    name = "zonedetect"
    version = "1.0"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    settings = ["os", "compiler", "build_type", "arch"]
    requires = [
        "shapelib/1.5.0",
        "gtest/1.11.0",
    ]
    tool_requires = "cmake/3.27.6"
    generators = "CMakeToolchain", "CMakeDeps"
    exports_sources = "*"

    def build(self):
        # it will find the packages by using our auto-generated FindXXX.cmake files
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        files.copy(self, "*.h", join(self.source_folder, "library"), join(self.package_folder, "include"))
        files.copy(self, "*.lib", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        files.copy(self, "*.dll", self.build_folder, join(self.package_folder, "bin"), keep_path=False)
        files.copy(self, "*.dylib*", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        files.copy(self, "*.so", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        files.copy(self, "*.a", self.build_folder, join(self.package_folder, "lib"), keep_path=False)
        files.copy(self, "timezone21.bin", join(self.build_folder, "out_v1"), join(self.package_folder, "include"), keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = ["zonedetect"]
