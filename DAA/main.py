import sys
import json
import dijkstra

#We need to mention __name__ as main as we are importing methods from other classes
if __name__ == '__main__':

    #We are giving the file name as command line argument as input to the main file
    #with open(sys.argv[1], 'r') as data_file:
    #    datastore = json.load(data_file) #Loading the file as JSON data

    datastore = json.load(open('data.json','r'))

    #Parsing the input JSON data file into 3 variables with key word in '.....'
    distances = datastore['distances']
    requests = datastore['requests']
    vehicles = datastore['vehicles']

    #Iterating over all the items in vehicles and initializing the availability for each one to TRUE
    for vehicle in vehicles:
        vehicle['available'] = True

    #Creating an object of Dijkstra's class to use the methods inside
    g = dijkstra.Graph()

    #Iterating over all the elements in distances variable and adding vertices/nodes/points it to graph
    for distance in distances:
        #We are adding the zipcode1 and zipcode2 only after checking whether they already exist in the object 'g' or not
        #If the zipcode is present, we skip it and if not, we add it to our graph as a new vertex/node/point
        if not distance['zipcode1'] in g.get_vertices():
            g.add_vertex(distance['zipcode1'])

        if not distance['zipcode2'] in g.get_vertices():
            g.add_vertex(distance['zipcode2'])

        #Calling the method defined in Dijkstra's class and passing the variables as (zc1(64110), zc2(64112), dist b/w them(4) to say)
        #We ultimately adding the edges to the graph from start
        #passing vertices as arguments, we are drawing an edge between the two nodes we passed and adding distance to it.
        g.add_edge(distance['zipcode1'], distance['zipcode2'], distance['distance'])

    """
    print('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
    """


#Here we are defining a manual defined function/method by passing vehicle type, and zipcode- REQUESTING for a vehicle by giving the zipcode
    #This method returns list of all available vehicles;
    def get_vehicle(vehicle_type, zipcode):

            #Here we are defining a new variable that stores all the available vehicles, It iterates over the variable 'VEHICLE' and
            #.. selects the vehicle only condition1: that vehicle type is present and condition2: the present vehicle is still available or not
        available_vehicles = [v for v in vehicles if v['type'] == vehicle_type and v['available']]

        #If there are available vehicles
        if len(available_vehicles) > 0:
            g.reset_vertices() #vertex's distance = infinityvi; vextex.visited = False; vertex.previous = None will be done in reset_vertices() method
            place = g.get_vertex(zipcode) #Returns vert_dict
            dijkstra.dijkstra(g, place) #passing the graph object and place into DIJKSTRA's method in Dijkstra's file

            #Calculating and  storing the list of distances for all the available vehicles done by adding vertex and getting distance
            for av in available_vehicles:
                av['distance'] = g.get_vertex(av['zipcode']).get_distance()

            #Sorting the list of all the available vehicles, based on key with inline function Lambda(sorts based on Distances)
            #The below contains list of KEY, VALUE pairs
            available_vehicles = sorted(available_vehicles, key=lambda k: k['distance'])
        
        return available_vehicles #Sorted list of available vehicles



#Iterating over all the requests in the requests variable
    for request in requests:
        #We are calling the 'get_vehicle' function for each request in all the requests in the order of FIFO
        ev = get_vehicle(request['vehicle_type'], request['zipcode']) #ev variable stores list of sorted available vehicles based on distance

        if len(ev) > 0: #If the number of available vehicles is more than 0 or (Atleast One 1)
            vehicles[vehicles.index(ev[0])]['available'] = False #As we request the nearest vehicle, we then change the availability to FALSE from TRUE
            request['vehicle_id'] = ev[0]['id'] #Storing the vehicle id in request variable as ev[0]'s ID
            request['distance'] = ev[0]['distance'] #Similarly, storing the distance of request variable from ev[0]'s distance
            #print(request) #This prints the part of JSON data in requests variable {.;.;.;.}
            [print(k,'--->',request[k]) for k in request] #Printing key value pairs in each of the requests
            print('--------------------------------------')
    with open('vehicles_updated','w') as f:
        json.dump(vehicles,f, ensure_ascii=False) #Writing into a new file the result of the JSON data
    #print(vehicles)
    #print(requests)

#print(g)
