rm _stann.so stann_wrap.*

~/opt/swig3.0.2/bin/swig -I./include/ -python -c++ stann_backend.i 

g++ -c -O3 -Wall -pedantic -ansi -Wextra -fopenmp -Wconversion -fPIC -I/usr/include/python2.7 -I./include/ stann_backend_wrap.cxx

g++ -shared -fopenmp stann_backend_wrap.o -o _stann_backend.so
