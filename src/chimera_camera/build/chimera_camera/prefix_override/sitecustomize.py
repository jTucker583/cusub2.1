import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/williamhardee/Documents/cusub2.1/src/chimera_camera/install/chimera_camera'
