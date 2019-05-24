import os
from cffi import FFI

ffibuilder = FFI()

basePath = os.path.dirname(__file__)
filePath = os.path.abspath(os.path.join(basePath, "..", "..", "build/bin/simple_bfs.cpp"))
compiledSimpleBFSFilePath = os.path.abspath(os.path.join(basePath, "simple_bfs.a"))

runtimePath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib"))
intrinsicsPath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib/intrinsics.h"))

with open(filePath,'rb') as f:

    ffibuilder.set_source("_simplebfs_cffi",
                          r'''extern "C" {}''',
                          language="c++",
                          extra_objects=[compiledSimpleBFSFilePath],
                          include_dirs=[runtimePath],
                          source_extension = ".cpp",
                          libraries=["stdc++"],
                          library_dirs=['simple_bfs'],
                          extra_compile_args = ["-std=c++11"]
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)