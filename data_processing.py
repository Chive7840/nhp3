import pandas as pd


class DataConstruct:
    def __init__(self):
        self.address_df = pd.read_csv('./data/address_data.csv', header=None)
        self.distance_df = pd.read_csv('./data/distance_matrix.csv', header=None)
        self.package_df = pd.read_csv('./data/package_data.csv', header=None)


# This class is used to build out each individual node which in this case means a delivery Hub
# The information provided in the documentation is used to build each Hub as separate vertex in the graph
class DeliveryHub:
    def __init__(self, hub_id, hub_name, hub_addr, hub_zip, nearest_kth):
        # In order to initialize the graph all distances need to be sert to infinite
        self.distance = float("inf")
        # Providing the ability to track efficient routing to all hubs
        # can be accomplished by tracing a path backward via it's predecessor pointer
        self.predecessor = ''
        # List of hub unique IDs integers from 0 to 26
        self.hub_id = hub_id
        # String object storing the name of the hub as correlated to the hub_id
        self.hub_name = hub_name
        # String object storing the address of the hub as correlated to the hub_id
        self.hub_addr = hub_addr
        # Integer object storing the zip code for the hub as correlated to the hub_id
        self.hub_zip = hub_zip
        # List of distances to other hubs in the network from the source hub
        self.nearest_kth = nearest_kth

    # Provides a method to fetch the nearest vertices to the specified vertex
    def fetch_neighbor(self, vertex):
        return self.nearest_kth[vertex]

    # In order to compare delivery hubs to each other and describe relationships between them
    # This class for the DeliveryHubs is used to aggregate and compare relevant information

    class DeliverHubs:
        def __init__(self):
            self.route_weights = {}
            self.adjacent_hubs = {}
            self.list_hubs = []

        # This method is used to populate the list of hubs
        def put_hub(self, hub_to_add):
            self.list_hubs.append(hub_to_add)
            self.adjacent_hubs[hub_to_add] = []

        def fetch_hub(self, hub_index):
            return self.list_hubs[hub_index]

        def fetch_id(self, address):
            for ele in range(len(self.list_hubs)):
                if self.list_hubs[ele].address == address:
                    return ele
                else:
                    return None