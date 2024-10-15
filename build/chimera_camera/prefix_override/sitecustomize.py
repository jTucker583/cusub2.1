import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/williamhardee/Documents/cusub2.1/install/chimera_camera'
