# Setup instructions

Currently this package depends on some pip installs according to the documentation for the wldvl-python repo. In order to set this up for use with ros, the following command must be run within the folder `cusub2.1/src/dvl_data/dvl_data/dvl-python/serial`:

```
pip install -e .
```

Building and running the packages can be run as normal after that.

Current issue: Once and a while when no data is read, casting to a string causes the node to fail.
