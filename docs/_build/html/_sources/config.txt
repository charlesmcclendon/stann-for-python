
Configuration
=============

.. toctree::
   :maxdepth: 2


+----------+-------------------------------------------+
|variable  | Meaning                                   |
+==========+===========================================+
|DIM       | Number of dimensions in the vector space. |
+----------+-------------------------------------------+
|DATA_TYPE | Represents the data type of the point.    |
|          | Assumes values like int or float.         |
+----------+-------------------------------------------+
|POINT_TYPE| Represents the type of point you wish to  |
|          | use from the original Stann library       |
+----------+-------------------------------------------+


.. function:: configure(dim, data_type, point_type=POINT_TYPE_DPOINT)

   DIM represents the number of dimensions of the vector space you
   are working in.
   DATA_TYPE represents the data type of the points, for example int or float.
   POINT_TYPE is the type of point you choose to use from the original
   Stann library; this value defaults to dpoint::

      DIM = dim
      DATA_TYPE = data_type
      POINT_TYPE = point_type
