%include "sfcnn_knng.hpp"


%define sfcnn_knng_getitem(T, D)

%extend sfcnn_knng<reviver::dpoint<T, D>, D, T> {
    std::vector<long unsigned int>& __getitem__(unsigned long i) {
        return (*($self))[i];
    }
};

%enddef

sfcnn_knng_getitem(unsigned short, 1)
sfcnn_knng_getitem(short,          1)
sfcnn_knng_getitem(unsigned int,   1)
sfcnn_knng_getitem(int,            1)
sfcnn_knng_getitem(unsigned long,  1)
sfcnn_knng_getitem(long,           1)
sfcnn_knng_getitem(float,          1)
sfcnn_knng_getitem(double,         1)

sfcnn_knng_getitem(unsigned short, 2)
sfcnn_knng_getitem(short,          2)
sfcnn_knng_getitem(unsigned int,   2)
sfcnn_knng_getitem(int,            2)
sfcnn_knng_getitem(unsigned long,  2)
sfcnn_knng_getitem(long,           2)
sfcnn_knng_getitem(float,          2)
sfcnn_knng_getitem(double,         2)

sfcnn_knng_getitem(unsigned short, 3)
sfcnn_knng_getitem(short,          3)
sfcnn_knng_getitem(unsigned int,   3)
sfcnn_knng_getitem(int,            3)
sfcnn_knng_getitem(unsigned long,  3)
sfcnn_knng_getitem(long,           3)
sfcnn_knng_getitem(float,          3)
sfcnn_knng_getitem(double,         3)

sfcnn_knng_getitem(unsigned short, 4)
sfcnn_knng_getitem(short,          4)
sfcnn_knng_getitem(unsigned int,   4)
sfcnn_knng_getitem(int,            4)
sfcnn_knng_getitem(unsigned long,  4)
sfcnn_knng_getitem(long,           4)
sfcnn_knng_getitem(float,          4)
sfcnn_knng_getitem(double,         4)

sfcnn_knng_getitem(unsigned short, 5)
sfcnn_knng_getitem(short,          5)
sfcnn_knng_getitem(unsigned int,   5)
sfcnn_knng_getitem(int,            5)
sfcnn_knng_getitem(unsigned long,  5)
sfcnn_knng_getitem(long,           5)
sfcnn_knng_getitem(float,          5)
sfcnn_knng_getitem(double,         5)

/* sfcnn_knng */
%define sfcnn_knng__template(T, PT, D)

%template(sfcnn_knng_DPoint_ ## D ## d_ ## PT ## )  ::sfcnn_knng<reviver::dpoint<T, D>, D, T>;

%enddef

%define sfcnn_knng(D)
    sfcnn_knng__template(unsigned short, UShort, D)
    sfcnn_knng__template(short, Short, D)
    sfcnn_knng__template(unsigned int, UInt, D)
    sfcnn_knng__template(int, Int, D)
    sfcnn_knng__template(unsigned long, ULong, D)
    sfcnn_knng__template(long, Long, D)
    sfcnn_knng__template(float, Float, D)
    sfcnn_knng__template(double, Double, D)
%enddef

sfcnn_knng(1)
sfcnn_knng(2)
sfcnn_knng(3)
sfcnn_knng(4)
sfcnn_knng(5)

/*
%template(sfcnn_knng_DPoint_1d_UShort)       ::sfcnn_knng<reviver::dpoint<unsigned short, 1>, 1, unsigned short>;
%template(sfcnn_knng_DPoint_1d_Short)        ::sfcnn_knng<reviver::dpoint<short         , 1>, 1, short         >;
%template(sfcnn_knng_DPoint_1d_UInt)         ::sfcnn_knng<reviver::dpoint<unsigned int  , 1>, 1, unsigned int  >;
%template(sfcnn_knng_DPoint_1d_Int)          ::sfcnn_knng<reviver::dpoint<int           , 1>, 1, int           >;
%template(sfcnn_knng_DPoint_1d_ULong)        ::sfcnn_knng<reviver::dpoint<unsigned long , 1>, 1, unsigned long >;
%template(sfcnn_knng_DPoint_1d_Long)         ::sfcnn_knng<reviver::dpoint<long          , 1>, 1, long          >;
%template(sfcnn_knng_DPoint_1d_Float)        ::sfcnn_knng<reviver::dpoint<float         , 1>, 1, float         >;
%template(sfcnn_knng_DPoint_1d_Double)       ::sfcnn_knng<reviver::dpoint<double        , 1>, 1, double        >;

%template(sfcnn_knng_DPoint_2d_UShort)       ::sfcnn_knng<reviver::dpoint<unsigned short, 2>, 2, unsigned short>;
%template(sfcnn_knng_DPoint_2d_Short)        ::sfcnn_knng<reviver::dpoint<short         , 2>, 2, short         >;
%template(sfcnn_knng_DPoint_2d_UInt)         ::sfcnn_knng<reviver::dpoint<unsigned int  , 2>, 2, unsigned int  >;
%template(sfcnn_knng_DPoint_2d_Int)          ::sfcnn_knng<reviver::dpoint<int           , 2>, 2, int           >;
%template(sfcnn_knng_DPoint_2d_ULong)        ::sfcnn_knng<reviver::dpoint<unsigned long , 2>, 2, unsigned long >;
%template(sfcnn_knng_DPoint_2d_Long)         ::sfcnn_knng<reviver::dpoint<long          , 2>, 2, long          >;
%template(sfcnn_knng_DPoint_2d_Float)        ::sfcnn_knng<reviver::dpoint<float         , 2>, 2, float         >;
%template(sfcnn_knng_DPoint_2d_Double)       ::sfcnn_knng<reviver::dpoint<double        , 2>, 2, double        >;

%template(sfcnn_knng_DPoint_3d_UShort)       ::sfcnn_knng<reviver::dpoint<unsigned short, 3>, 3, unsigned short>;
%template(sfcnn_knng_DPoint_3d_Short)        ::sfcnn_knng<reviver::dpoint<short         , 3>, 3, short         >;
%template(sfcnn_knng_DPoint_3d_UInt)         ::sfcnn_knng<reviver::dpoint<unsigned int  , 3>, 3, unsigned int  >;
%template(sfcnn_knng_DPoint_3d_Int)          ::sfcnn_knng<reviver::dpoint<int           , 3>, 3, int           >;
%template(sfcnn_knng_DPoint_3d_ULong)        ::sfcnn_knng<reviver::dpoint<unsigned long , 3>, 3, unsigned long >;
%template(sfcnn_knng_DPoint_3d_Long)         ::sfcnn_knng<reviver::dpoint<long          , 3>, 3, long          >;
%template(sfcnn_knng_DPoint_3d_Float)        ::sfcnn_knng<reviver::dpoint<float         , 3>, 3, float         >;
%template(sfcnn_knng_DPoint_3d_Double)       ::sfcnn_knng<reviver::dpoint<double        , 3>, 3, double        >;

%template(sfcnn_knng_DPoint_4d_UShort)       ::sfcnn_knng<reviver::dpoint<unsigned short, 4>, 4, unsigned short>;
%template(sfcnn_knng_DPoint_4d_Short)        ::sfcnn_knng<reviver::dpoint<short         , 4>, 4, short         >;
%template(sfcnn_knng_DPoint_4d_UInt)         ::sfcnn_knng<reviver::dpoint<unsigned int  , 4>, 4, unsigned int  >;
%template(sfcnn_knng_DPoint_4d_Int)          ::sfcnn_knng<reviver::dpoint<int           , 4>, 4, int           >;
%template(sfcnn_knng_DPoint_4d_ULong)        ::sfcnn_knng<reviver::dpoint<unsigned long , 4>, 4, unsigned long >;
%template(sfcnn_knng_DPoint_4d_Long)         ::sfcnn_knng<reviver::dpoint<long          , 4>, 4, long          >;
%template(sfcnn_knng_DPoint_4d_Float)        ::sfcnn_knng<reviver::dpoint<float         , 4>, 4, float         >;
%template(sfcnn_knng_DPoint_4d_Double)       ::sfcnn_knng<reviver::dpoint<double        , 4>, 4, double        >;

%template(sfcnn_knng_DPoint_5d_UShort)       ::sfcnn_knng<reviver::dpoint<unsigned short, 5>, 5, unsigned short>;
%template(sfcnn_knng_DPoint_5d_Short)        ::sfcnn_knng<reviver::dpoint<short         , 5>, 5, short         >;
%template(sfcnn_knng_DPoint_5d_UInt)         ::sfcnn_knng<reviver::dpoint<unsigned int  , 5>, 5, unsigned int  >;
%template(sfcnn_knng_DPoint_5d_Int)          ::sfcnn_knng<reviver::dpoint<int           , 5>, 5, int           >;
%template(sfcnn_knng_DPoint_5d_ULong)        ::sfcnn_knng<reviver::dpoint<unsigned long , 5>, 5, unsigned long >;
%template(sfcnn_knng_DPoint_5d_Long)         ::sfcnn_knng<reviver::dpoint<long          , 5>, 5, long          >;
%template(sfcnn_knng_DPoint_5d_Float)        ::sfcnn_knng<reviver::dpoint<float         , 5>, 5, float         >;
%template(sfcnn_knng_DPoint_5d_Double)       ::sfcnn_knng<reviver::dpoint<double        , 5>, 5, double        >;
*/

