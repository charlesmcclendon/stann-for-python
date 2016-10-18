%include "test.hpp"

/* testNN */
%template(testNN_1d_UShort)    ::testNN<unsigned short, 1>;
%template(testNN_1d_Short)     ::testNN<short         , 1>;
%template(testNN_1d_UInt)      ::testNN<unsigned int  , 1>;
%template(testNN_1d_Int)       ::testNN<int           , 1>;
%template(testNN_1d_ULong)     ::testNN<unsigned long , 1>;
%template(testNN_1d_Long)      ::testNN<long          , 1>;
%template(testNN_1d_Float)     ::testNN<float         , 1>;
%template(testNN_1d_Double)    ::testNN<double        , 1>;

%template(testNN_2d_UShort)    ::testNN<unsigned short, 2>;
%template(testNN_2d_Short)     ::testNN<short         , 2>;
%template(testNN_2d_UInt)      ::testNN<unsigned int  , 2>;
%template(testNN_2d_Int)       ::testNN<int           , 2>;
%template(testNN_2d_ULong)     ::testNN<unsigned long , 2>;
%template(testNN_2d_Long)      ::testNN<long          , 2>;
%template(testNN_2d_Float)     ::testNN<float         , 2>;
%template(testNN_2d_Double)    ::testNN<double        , 2>;

%template(testNN_3d_UShort)    ::testNN<unsigned short, 3>;
%template(testNN_3d_Short)     ::testNN<short         , 3>;
%template(testNN_3d_UInt)      ::testNN<unsigned int  , 3>;
%template(testNN_3d_Int)       ::testNN<int           , 3>;
%template(testNN_3d_ULong)     ::testNN<unsigned long , 3>;
%template(testNN_3d_Long)      ::testNN<long          , 3>;
%template(testNN_3d_Float)     ::testNN<float         , 3>;
%template(testNN_3d_Double)    ::testNN<double        , 3>;

%template(testNN_4d_UShort)    ::testNN<unsigned short, 4>;
%template(testNN_4d_Short)     ::testNN<short         , 4>;
%template(testNN_4d_UInt)      ::testNN<unsigned int  , 4>;
%template(testNN_4d_Int)       ::testNN<int           , 4>;
%template(testNN_4d_ULong)     ::testNN<unsigned long , 4>;
%template(testNN_4d_Long)      ::testNN<long          , 4>;
%template(testNN_4d_Float)     ::testNN<float         , 4>;
%template(testNN_4d_Double)    ::testNN<double        , 4>;

%template(testNN_5d_UShort)    ::testNN<unsigned short, 5>;
%template(testNN_5d_Short)     ::testNN<short         , 5>;
%template(testNN_5d_UInt)      ::testNN<unsigned int  , 5>;
%template(testNN_5d_Int)       ::testNN<int           , 5>;
%template(testNN_5d_ULong)     ::testNN<unsigned long , 5>;
%template(testNN_5d_Long)      ::testNN<long          , 5>;
%template(testNN_5d_Float)     ::testNN<float         , 5>;
%template(testNN_5d_Double)    ::testNN<double        , 5>;
