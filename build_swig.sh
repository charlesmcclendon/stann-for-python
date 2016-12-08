rm _stann_backend.so stann_backend_wrap.*

~/opt/swig3.0.10/bin/swig -I./include/ -python -py3 -c++ stann_backend.i 

g++ -c -O3 -Wall -pedantic -ansi -Wextra -fopenmp -Wconversion -fPIC $(python3.5-config --cflags) -I./include/ stann_backend_wrap.cxx

g++ -shared -fopenmp stann_backend_wrap.o $(python3.5-config --ldflags) -o _stann_backend.so

mkdir -p distrib/stann

cp stann.py stann_backend.py _stann_backend.so distrib/stann/
mv distrib/stann/stann.py distrib/stann/__init__.py
