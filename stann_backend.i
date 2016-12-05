%module stann_backend
%include "std_string.i"
%include "stdint.i"
%include "std_vector.i"
%include "cpointer.i"

%template(StringVector)   std::vector<std::string>;
%template(UShortVector)   std::vector<unsigned short>;
%template(ShortVector)    std::vector<short>;
%template(UIntVector)     std::vector<unsigned int>;
%template(IntVector)      std::vector<int>;
%template(ULongVector)    std::vector<unsigned long>;
%template(LongVector)     std::vector<long>;
%template(FloatVector)    std::vector<float>;
%template(DoubleVector)   std::vector<double>;

%include "carrays.i"
%array_class(char               , Int8Array);
%array_class(unsigned char      , UInt8Array);
%array_class(short              , ShortArray);
%array_class(unsigned short     , UShortArray);
%array_class(int                , IntArray);
%array_class(unsigned int       , UIntArray);
%array_class(long               , LongArray);
%array_class(unsigned long      , ULongArray);
%array_class(float              , FloatArray);
%array_class(double             , DoubleArray);
%{
    #include "test.hpp"
%}

%include "stann_inc_test_hpp.i"
%include "stann_inc_dpoint_hpp.i"
%include "stann_inc_bruteNN_hpp.i"
%include "stann_inc_sfcnn_hpp.i"
%include "stann_inc_sfcnn_hpp.i"
%include "stann_inc_sfcnn_knng_hpp.i"
%include "stann_inc_zorderLT.i"
