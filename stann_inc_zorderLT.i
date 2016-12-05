%include "zorder_lt.hpp"

%define zorder_lt__template(T, PT, D)
    %template(zorderLT_DPoint_ ## D ## d_ ## PT)  ::zorder_lt<reviver::dpoint<T, D>>;

    %extend zorder_lt<reviver::dpoint<T, D>> {
        bool __call__(reviver::dpoint<T, D> &p1, reviver::dpoint<T, D> &p2) {
            return (*($self))(p1, p2);
        }
    };


%enddef

zorder_lt__template(unsigned short, UShort, 1)
zorder_lt__template(short, Short,           1)
zorder_lt__template(unsigned int, UInt,     1)
zorder_lt__template(int, Int,               1)
zorder_lt__template(unsigned long, ULong,   1)
zorder_lt__template(long, Long,             1)
zorder_lt__template(float, Float,           1)
zorder_lt__template(double, Double,         1)

zorder_lt__template(unsigned short, UShort, 2)
zorder_lt__template(short, Short,           2)
zorder_lt__template(unsigned int, UInt,     2)
zorder_lt__template(int, Int,               2)
zorder_lt__template(unsigned long, ULong,   2)
zorder_lt__template(long, Long,             2)
zorder_lt__template(float, Float,           2)
zorder_lt__template(double, Double,         2)

zorder_lt__template(unsigned short, UShort, 3)
zorder_lt__template(short, Short,           3)
zorder_lt__template(unsigned int, UInt,     3)
zorder_lt__template(int, Int,               3)
zorder_lt__template(unsigned long, ULong,   3)
zorder_lt__template(long, Long,             3)
zorder_lt__template(float, Float,           3)
zorder_lt__template(double, Double,         3)

zorder_lt__template(unsigned short, UShort, 4)
zorder_lt__template(short, Short,           4)
zorder_lt__template(unsigned int, UInt,     4)
zorder_lt__template(int, Int,               4)
zorder_lt__template(unsigned long, ULong,   4)
zorder_lt__template(long, Long,             4)
zorder_lt__template(float, Float,           4)
zorder_lt__template(double, Double,         4)

zorder_lt__template(unsigned short, UShort, 5)
zorder_lt__template(short, Short,           5)
zorder_lt__template(unsigned int, UInt,     5)
zorder_lt__template(int, Int,               5)
zorder_lt__template(unsigned long, ULong,   5)
zorder_lt__template(long, Long,             5)
zorder_lt__template(float, Float,           5)
zorder_lt__template(double, Double,         5)

