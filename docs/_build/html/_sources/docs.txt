
Documentation
=============

.. ::toctree
   :maxdepth: 2
   :numbered:


.. module:: stann
   :synopsis: stann wrapper class


.. py:function:: newRandomPoint(min_val, max_val)

   Generates a random point with component values between
   min_val and max_val.


.. py:function:: createPointVector()

   Generates an empty vector with dimension and data type
   matching the module configuration.


Algorithm Classes
-----------------


.. py:class:: bruteNN(pointVector, n)

   Object for performing nearest neighbor calculations by
   brute force. The dimension and data type are
   determined by the dimension and data type of pointVector.
   Parameter n represents the number of points in pointVector.


   .. method:: ksearch(point, k, ans_vector)

      Perform a nearest neighbor search on parameter point. Find
      the k nearest neighbors and store them inside ans_vector.



.. py:class:: sfcnn(pointVector, n)

   Similar to bruteNN but the nearest neighbor calculations
   are optimized.


   .. method:: ksearch(point, k, ans_vector)



.. py:class:: sfcnn_knng(pointVector, n)

   Similar to bruteNN but the nearest neighbor calculations
   are optimized and  multi-threading is used.
