import os
from cffi import FFI

ffibuilder = FFI()

basePath = os.path.dirname(__file__)
filePath = os.path.abspath(os.path.join(basePath, "..", "..", "build/bin/simple_bfs.cpp"))
compiledSimpleBFSFilePath = os.path.abspath(os.path.join(basePath, "simple_bfs.a"))
#bfs_include_path = os.path.abspath(join("include"))

#cpp_path = path.Path("../../build/bin").abspath()

#include_dirs = []
#include_dirs.append(cpp_path.joinpath("include"))
#include_dirs.append(cpp_build_path)


runtimePath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib"))
intrinsicsPath = os.path.abspath(os.path.join(basePath, "..", "..", "src/runtime_lib/intrinsics.h"))

print("This is compiledSimpleBFSFilePath")
print(compiledSimpleBFSFilePath)

#print("This is bfs_include_path")
#print(bfs_include_path)

with open(filePath,'rb') as f:
    #externFunction = "r'''extern \"C\" {} {} {}'''".format('{', f.read(), '}')
    #print(externFunction)

    ffibuilder.set_source("_simplebfs_cffi",
                          #r'''extern "C" {}{}{}'''.format('{', f.read(), '}'),
                          #f.read(),
                          r'''extern "C" {}''',
                          language="c++",
                          extra_objects=[compiledSimpleBFSFilePath],
                          include_dirs=[runtimePath],
                          source_extension = ".cpp",
                          libraries=["stdc++"],
                          library_dirs=['simple_bfs'],
                          extra_compile_args = ["-std=c++11"]
)

#ffibuilder.cdef(
#    """
#    struct run_bfs{};
#    """
#)

#with open(intrinsicsPath, "r") as f:
#    ffibuilder.cdef(f.read())

#ffibuilder.new("struct run_bfs *")

#ffibuilder.set_source("_simplebfs_cffi",
#                      sources=['../../build/bin/simple_bfs.cpp'])

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)