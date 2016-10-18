%include "dpoint.hpp"

/* dpoint */
%template(DPoint_1d_UShort)    reviver::dpoint<unsigned short, 1>;
%template(DPoint_1d_Short)     reviver::dpoint<short         , 1>;
%template(DPoint_1d_UInt)      reviver::dpoint<unsigned int  , 1>;
%template(DPoint_1d_Int)       reviver::dpoint<int           , 1>;
%template(DPoint_1d_ULong)     reviver::dpoint<unsigned long , 1>;
%template(DPoint_1d_Long)      reviver::dpoint<long          , 1>;
%template(DPoint_1d_Float)     reviver::dpoint<float         , 1>;
%template(DPoint_1d_Double)    reviver::dpoint<double        , 1>;

%template(DPoint_2d_UShort)    reviver::dpoint<unsigned short, 2>;
%template(DPoint_2d_Short)     reviver::dpoint<short         , 2>;
%template(DPoint_2d_UInt)      reviver::dpoint<unsigned int  , 2>;
%template(DPoint_2d_Int)       reviver::dpoint<int           , 2>;
%template(DPoint_2d_ULong)     reviver::dpoint<unsigned long , 2>;
%template(DPoint_2d_Long)      reviver::dpoint<long          , 2>;
%template(DPoint_2d_Float)     reviver::dpoint<float         , 2>;
%template(DPoint_2d_Double)    reviver::dpoint<double        , 2>;

%template(DPoint_3d_UShort)    reviver::dpoint<unsigned short, 3>;
%template(DPoint_3d_Short)     reviver::dpoint<short         , 3>;
%template(DPoint_3d_UInt)      reviver::dpoint<unsigned int  , 3>;
%template(DPoint_3d_Int)       reviver::dpoint<int           , 3>;
%template(DPoint_3d_ULong)     reviver::dpoint<unsigned long , 3>;
%template(DPoint_3d_Long)      reviver::dpoint<long          , 3>;
%template(DPoint_3d_Float)     reviver::dpoint<float         , 3>;
%template(DPoint_3d_Double)    reviver::dpoint<double        , 3>;

%template(DPoint_4d_UShort)    reviver::dpoint<unsigned short, 4>;
%template(DPoint_4d_Short)     reviver::dpoint<short         , 4>;
%template(DPoint_4d_UInt)      reviver::dpoint<unsigned int  , 4>;
%template(DPoint_4d_Int)       reviver::dpoint<int           , 4>;
%template(DPoint_4d_ULong)     reviver::dpoint<unsigned long , 4>;
%template(DPoint_4d_Long)      reviver::dpoint<long          , 4>;
%template(DPoint_4d_Float)     reviver::dpoint<float         , 4>;
%template(DPoint_4d_Double)    reviver::dpoint<double        , 4>;

%template(DPoint_5d_UShort)    reviver::dpoint<unsigned short, 5>;
%template(DPoint_5d_Short)     reviver::dpoint<short         , 5>;
%template(DPoint_5d_UInt)      reviver::dpoint<unsigned int  , 5>;
%template(DPoint_5d_Int)       reviver::dpoint<int           , 5>;
%template(DPoint_5d_ULong)     reviver::dpoint<unsigned long , 5>;
%template(DPoint_5d_Long)      reviver::dpoint<long          , 5>;
%template(DPoint_5d_Float)     reviver::dpoint<float         , 5>;
%template(DPoint_5d_Double)    reviver::dpoint<double        , 5>;

%template(Vector_DPoint_1d_UShort)  std::vector<reviver::dpoint<unsigned short, 1>>;
%template(Vector_DPoint_1d_Short)   std::vector<reviver::dpoint<short         , 1>>;
%template(Vector_DPoint_1d_UInt)    std::vector<reviver::dpoint<unsigned int  , 1>>;
%template(Vector_DPoint_1d_Int)     std::vector<reviver::dpoint<int           , 1>>;
%template(Vector_DPoint_1d_ULong)   std::vector<reviver::dpoint<unsigned long , 1>>;
%template(Vector_DPoint_1d_Long)    std::vector<reviver::dpoint<long          , 1>>;
%template(Vector_DPoint_1d_Float)   std::vector<reviver::dpoint<float         , 1>>;
%template(Vector_DPoint_1d_Double)  std::vector<reviver::dpoint<double        , 1>>;

%template(Vector_DPoint_2d_UShort)  std::vector<reviver::dpoint<unsigned short, 2>>;
%template(Vector_DPoint_2d_Short)   std::vector<reviver::dpoint<short         , 2>>;
%template(Vector_DPoint_2d_UInt)    std::vector<reviver::dpoint<unsigned int  , 2>>;
%template(Vector_DPoint_2d_Int)     std::vector<reviver::dpoint<int           , 2>>;
%template(Vector_DPoint_2d_ULong)   std::vector<reviver::dpoint<unsigned long , 2>>;
%template(Vector_DPoint_2d_Long)    std::vector<reviver::dpoint<long          , 2>>;
%template(Vector_DPoint_2d_Float)   std::vector<reviver::dpoint<float         , 2>>;
%template(Vector_DPoint_2d_Double)  std::vector<reviver::dpoint<double        , 2>>;

%template(Vector_DPoint_3d_UShort)  std::vector<reviver::dpoint<unsigned short, 3>>;
%template(Vector_DPoint_3d_Short)   std::vector<reviver::dpoint<short         , 3>>;
%template(Vector_DPoint_3d_UInt)    std::vector<reviver::dpoint<unsigned int  , 3>>;
%template(Vector_DPoint_3d_Int)     std::vector<reviver::dpoint<int           , 3>>;
%template(Vector_DPoint_3d_ULong)   std::vector<reviver::dpoint<unsigned long , 3>>;
%template(Vector_DPoint_3d_Long)    std::vector<reviver::dpoint<long          , 3>>;
%template(Vector_DPoint_3d_Float)   std::vector<reviver::dpoint<float         , 3>>;
%template(Vector_DPoint_3d_Double)  std::vector<reviver::dpoint<double        , 3>>;

%template(Vector_DPoint_4d_UShort)  std::vector<reviver::dpoint<unsigned short, 4>>;
%template(Vector_DPoint_4d_Short)   std::vector<reviver::dpoint<short         , 4>>;
%template(Vector_DPoint_4d_UInt)    std::vector<reviver::dpoint<unsigned int  , 4>>;
%template(Vector_DPoint_4d_Int)     std::vector<reviver::dpoint<int           , 4>>;
%template(Vector_DPoint_4d_ULong)   std::vector<reviver::dpoint<unsigned long , 4>>;
%template(Vector_DPoint_4d_Long)    std::vector<reviver::dpoint<long          , 4>>;
%template(Vector_DPoint_4d_Float)   std::vector<reviver::dpoint<float         , 4>>;
%template(Vector_DPoint_4d_Double)  std::vector<reviver::dpoint<double        , 4>>;

%template(Vector_DPoint_5d_UShort)  std::vector<reviver::dpoint<unsigned short, 5>>;
%template(Vector_DPoint_5d_Short)   std::vector<reviver::dpoint<short         , 5>>;
%template(Vector_DPoint_5d_UInt)    std::vector<reviver::dpoint<unsigned int  , 5>>;
%template(Vector_DPoint_5d_Int)     std::vector<reviver::dpoint<int           , 5>>;
%template(Vector_DPoint_5d_ULong)   std::vector<reviver::dpoint<unsigned long , 5>>;
%template(Vector_DPoint_5d_Long)    std::vector<reviver::dpoint<long          , 5>>;
%template(Vector_DPoint_5d_Float)   std::vector<reviver::dpoint<float         , 5>>;
%template(Vector_DPoint_5d_Double)  std::vector<reviver::dpoint<double        , 5>>;

%include "stann_inc_dpoint_newRandomPoint.i"
