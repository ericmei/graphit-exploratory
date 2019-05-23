import os
from cffi import FFI

ffibuilder = FFI()

basePath = os.path.dirname(__file__)
filePath = os.path.abspath(os.path.join(basePath, "..", "..", "build/bin/simple_bfs.cpp"))
#print(filePath)

runtimePath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib"))
intrinsicsPath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib/intrinsics.h"))

print("This is runtimepath")
print(runtimePath)

with open(filePath,'r') as f:
    ffibuilder.set_source("_simplebfs_cffi",
                          f.read(),
                          include_dirs=[runtimePath],
                          source_extension = ".cpp",
                          extra_compile_args = ["-std=c++11"]
)

ffibuilder.cdef(
    """
    struct run_bfs{};
    """
)

#with open(intrinsicsPath, "r") as f:
#    ffibuilder.cdef(f.read())

#ffibuilder.new("struct run_bfs *")

#ffibuilder.set_source("_simplebfs_cffi",
#                      sources=['../../build/bin/simple_bfs.cpp'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)