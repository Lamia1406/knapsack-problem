""" this module contains one function : fractional_knapsack""" 
def fractional_knapsack(capacity, objects):
    """uses the value-to-weight ratio algorithm to solve the continuous knapsack problem(fractional)
        Args:
            capacity: defines the maximum knapsack capacity
            objects: defines the available objects to take with their names, weights and values
    """
    max_profit = 0
    objects_in_backpack = []
    
    sorted_objects = sorted(objects, key=lambda x: x["value"] / x["weight"], reverse=True)
    while capacity > 0 and sorted_objects:
        objects_in_backpack.append(sorted_objects[0]["name"])
        if capacity >= sorted_objects[0]["weight"]:
            capacity -= sorted_objects[0]["weight"]
            max_profit += sorted_objects[0]["value"]
        else:
            max_profit += (sorted_objects[0]["value"] * capacity / sorted_objects[0]["weight"]) 
        sorted_objects.pop(0)
    return f"the objects {objects_in_backpack} are collected with total profit {max_profit}"


def main():
    print(fractional_knapsack(15, [
        {
            "name" : "item 1",
            "value" : 40,
            "weight" : 2
        },
        {
            "name" : "item 2",
            "value" : 30,
            "weight" : 5
        },
        {
            "name" : "item 3",
            "value" : 50,
            "weight" : 10
        },
        {
            "name" : "item 4",
            "value" : 10,
            "weight" : 5
        },
        {
            "name" : "item 5",
            "value" : 70,
            "weight" : 7
        },
        {
            "name" : "item 6",
            "value" : 15,
            "weight" : 3
        },
        {
            "name" : "item 7",
            "value" : 60,
            "weight" : 2
        },
        {
            "name" : "item 8",
            "value" : 80,
            "weight" : 4
        },
        {
            "name" : "item 9",
            "value" : 29,
            "weight" : 9
        },
        {
            "name" : "item 10",
            "value" : 50,
            "weight" : 6
        },
        

        


    ]))

main()


