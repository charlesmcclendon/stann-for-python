Introduction
============

The stann python module wraps the C++ Stann library which
implements a number of nearest neighbor algorithms and custom
data types.
The Stann library relies heavily upon C++ class and function
templating, a feature not found in python. We used Swig to 
generate the interface but the only way to make the templates
accessible in python was to recreate each function and class
instantiation with every combination of template parameters.
This results in a huge set of functions and classes with long
and confusing names that are kept in the stann_backend module. 
The main difficulty in creating a python wrapper for Stann
is finding a way to handle all the function and class templates
behind the scenes so that we can deliver concise and intuitive
function and class names to users.
The main idea behind our solution is to provide a function
configure which allows you to configure the global module variables:

.. py:function:: configure(dim, data_type, point_type=POINT_TYPE_DPOINT)

   DIM represents the number of dimensions of the vector space you
   are working in.
   DATA_TYPE represents the data type of the points, for example int or float.
   POINT_TYPE is the type of point you choose to use from the original
   Stann library; this value defaults to dpoint::

      DIM = dim
      DATA_TYPE = data_type
      POINT_TYPE = point_type

After configuring these values you can call stann functions like
newRandomPoint() and classes like bruteNN() without having to specify
the dimension and data type of the vector space each time.

.. ::toctree
   :maxdepth: 2


