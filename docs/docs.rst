
Documentation
=============

.. ::toctree
   :maxdepth: 2
   :numbered:


.. module:: stann
   :synopsis: stann wrapper class


Algorithm Classes
-----------------


.. py:class:: bruteNN(pointVector, n)

   Object for performing nearest neighbor calculations by
   brute force. The dimension and data type are
   determined by the dimension and data type of pointVector.
   Parameter n represents the number of points in pointVector.


   .. data:: DIM

      Dimension of the vector space.


   .. data:: DATA_TYPE

      Data type of the points.


   .. method:: ksearch(point, k, ans_vector)

      Perform a nearest neighbor search on parameter point. Find
      the k nearest neighbors and store them inside ans_vector.


.. py:class:: sfcnn(pointVector, n)

   Similar to bruteNN but the nearest neighbor calculations
   are optimized using a space filling curve algorithm.


   .. data:: DIM

      Dimension of the vector space.


   .. data:: DATA_TYPE

      Data type of the points.


   .. method:: ksearch(point, k, ans_vector)

      Perform a nearest neighbor search on parameter point. Find
      the k nearest neighbors and store them inside ans_vector.


.. py:class:: sfcnn_knng(pointVector, n)

   Similar to sfcnn but the nearest neighbor calculations
   are optimized using multi-threading. 


   .. data:: DIM

      Dimension of the vector space.


   .. data:: DATA_TYPE

      Data type of the points.


   .. method:: ksearch(point, k, ans_vector)

      Perform a nearest neighbor search on parameter point. Find
      the k nearest neighbors and store them inside ans_vector.


.. py:class:: zorderLT()

   Object used to impose a total order on an n-dimensional
   point cloud. Only for use on point clouds with integral
   coordinates. Example usage::

      import stann

      stann.configure(3, stann.DATA_TYPE_INT)
      p1 = newRandomPoint(0, 100)
      p2 = newRandomPoint(0, 100)

      lt = stann.zorderLT()

      if(lt(p1, p2))
          print('p1 < p2')




Utility Functions
-----------------



.. py:function:: newRandomPoint(min_val, max_val)

   Generates a random point with component values between
   min_val and max_val.


.. py:function:: createPointVector()

   Generates an empty vector of points with dimension and data type
   matching the module configuration.


.. py:function:: createAnswerVector()

   Generates an empty vector of long integers. Used for storing
   results of :func:`ksearch`.


Point Class
-----------


Once you have created points with utility functions like
:func:`newRandomPoint` and :func:`createPointVector` there are a
number of helper methods you can use to access and manipulate
their data.


.. py:class:: Point


   .. data:: coords

      Mutable list that represents the coordinates of the point.


   .. data:: coords_tuple

      Immutable python tuple that represents the coordinates of the point.
      Usage::

         import stann

         stann.configure(3, stann.DATA_TYPE_INT)
         p = stann.newRandomPoint(0, 5)
         print(p.coords)            # [2, 4, 5]
         p.coords[2] = 3
         print(p.coords_tuple)      # (2, 4, 3)


