from conans import ConanFile, CMake, tools
import os


class glmConan(ConanFile):
    name = "glm"
    version = "0.9.8-0"
    license = "The Happy Bunny License, or the MIT License"
    url = "https://github.com/TimSimpson/conan-glm"

    def source(self):
       self.run("git clone https://github.com/g-truc/glm.git")
       self.run("cd glm && git checkout 3b1af3fe0b6c9b071dcb5a557b493980bd23c6e4")

    def package(self):
        self.copy("*", dst="include/glm", src="glm/glm")
