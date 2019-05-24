import os
import _simplebfs_cffi

from cffi import FFI

ffi = FFI()

class run_bfs():
    def __init__(self):
        self.bfs = _simplebfs_cffi.ffi.new("struct run_bfs*", None)

    def __call__(self):
        (self.bfs)()

print(dir(_simplebfs_cffi.ffi.new))
run_bfs()()
