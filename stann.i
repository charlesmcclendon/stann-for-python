%module stann
%include "std_string.i"
%include "stdint.i"
%include "std_vector.i"
%include "pointer.i"    

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
%array_class(char               , StannInt8Array);
%array_class(unsigned char      , StannUInt8Array);
%array_class(short              , StannInt16Array);
%array_class(unsigned short     , StannUInt16Array);
%array_class(int                , StannInt32Array);
%array_class(unsigned int       , StannUInt32Array);
%array_class(long               , StannInt64Array);
%array_class(unsigned long      , StannUInt64Array);
%array_class(float              , StannFloatArray);
%array_class(double             , StannDoubleArray);
%{
/*
    #include "bruteNN.hpp"
	#include "dpoint.hpp"
	#include "rand.hpp"
	#include "sfcnn.hpp"
	#include "sfcnn_king.hpp"
	#include "gmst.hpp"
	#include "zorder_lt.hpp"
*/
    #include "test.hpp"
%}

/*%include "test.hpp"
%template(testZLT_IntInt) ::testZLT<unsigned int, 3>;*/

%include "stann_inc_test_hpp.i"
%include "stann_inc_dpoint_hpp.i"
%include "stann_inc_bruteNN_hpp.i"
%include "stann_inc_sfcnn_hpp.i"

/*
%include "bruteNN.hpp"
%include "dpoint.hpp"
%include "rand.hpp"
%include "sfcnn.hpp"
%include "sfcnn_king.hpp"
%include "gmst.hpp"
%include "zorder_lt.hpp"
*/

/*%include "test.hpp"*/
