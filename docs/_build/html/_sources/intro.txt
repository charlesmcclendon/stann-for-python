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
function and class names to users. The main idea behind our
solution is to provide a function :func:`configure` which allows
you to configure the global module variables.
After configuring these values you can use stann functions and
classes without having to specify the dimension and data type
of the vector space each time.

.. ::toctree
   :maxdepth: 2


