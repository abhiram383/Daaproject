# Design and Analysis of Algorithms
# Final Project



## Emergency Vehicle dispatch system:


* Implemented an algorithm that processes requests one by one. For each request, the algorithm
will try to find the closest available emergency vehicle

* We adopted the Dijkstra's algorithm for finding the shortest path from the source to the destination

* Implemented the algorith using the Python 3 with two classes, as main and Dijkstras

## objective:
  The objective of the project is to finding and allocating the available emergency vehicle from the nearest zipcode checking on availability providing the Zipcode and Emergency vehicle type as input for the algorithm
  
### Types of vehicles:
  * Ambulance
  * Fire Truck
  * Police
  
### Attributes considered:
  * Zipcodes as nodes
  * Distances as the edges weight with connected vertices
  * Vehicle type: among the above three types
  
### Data set provided: (https://github.com/abhiram383/Daaproject/blob/master/DAA/data.json)
We implemented this algorithm using the JSON data as the input type data, as JSON is the easy to access and parse.  
Dataset was available in the source code as:
   * data.json
   * datademo1.json
   * datademo2.json

## Classes Implemented:
  * Dijkstras: (https://github.com/abhiram383/Daaproject/blob/master/DAA/dijkstra.py)
  * Main     : (https://github.com/abhiram383/Daaproject/blob/master/DAA/main.py)
 
## Visualization:
* Visualization of the output data was implemented using the Bootstrap with conversion of JSON data into HTML tables to access the data and the output vehicles for the better user interface

* Make up the data for the project. Generated the files at run time, having stored into a separate output file in the format of JSON

* The output of our algorithm produces the shortest path for the required vehicle's availability


## Conclusion :
Dijkstra's algorithm finds the shortest path between two nodes . Here
we found distance between the node from which the request is raised
to all other nodes . found shortest distance to all other nodes . then we
sorted the nodes in increasing order of distance and check node with
availability . the first node with the availability (requested vehicle) is
the dispatcher node.

## Time complexity :
assuming number of requests as n and time complexity of dijkstra’s
being v2 where v is number of vertices . the time complexity of our
algorithm is O(n*V2)
