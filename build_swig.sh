rm _stann.so stann_wrap.*

~/opt/swig3.0.2/bin/swig -I./include/ -python -c++ stann.i 

g++ -c -O3 -Wall -pedantic -ansi -Wextra -fopenmp -Wconversion -fPIC -I/usr/include/python2.7 -I./include/ stann_wrap.cxx

g++ -shared -fopenmp stann_wrap.o -o _stann.so
