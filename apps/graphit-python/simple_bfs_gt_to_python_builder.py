import os
from cffi import FFI

ffibuilder = FFI()

basePath = os.path.dirname(__file__)
filePath = os.path.abspath(os.path.join(basePath, "..", "..", "build/bin/simple_bfs.cpp"))
compiledSimpleBFSFilePath = os.path.abspath(os.path.join(basePath, "..", "..", "build/bin/simple_bfs.cpp"))


runtimePath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib"))
intrinsicsPath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib/intrinsics.h"))

print("This is runtimepath")
print(runtimePath)

with open(filePath,'rb') as f:
    #externFunction = "r'''extern \"C\" {} {} {}'''".format('{', f.read(), '}')
    #print(externFunction)

    ffibuilder.set_source("_simplebfs_cffi",
                          #r'''extern "C" {}{}{}'''.format('{', f.read(), '}'),
                          #f.read(),
                          r'''extern "C" {}''',
                          include_dirs=[runtimePath],
                          source_extension = ".cpp",
                          libraries=['simple_bfs'],
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