""" this module contains one function : zero_one_knapsack""" 
def zero_one_knapsack(weight, objects):
    """uses the value-to-weight ratio algorithm to solve 0/1 knapsack problem
        Args:
            capacity: defines the maximum knapsack capacity
            objects: defines the available objects to take with their names, weights and values
    """
    max_profit = 0
    objects_in_backpack = []
    
    sorted_objects = sorted(objects, key=lambda x: x["value"] / x["weight"], reverse=True)
    while weight > 0 and sorted_objects:
        objects_in_backpack.append(sorted_objects[0]["name"])
        weight -= sorted_objects[0]["weight"]
        max_profit += sorted_objects[0]["value"]
        sorted_objects.pop(0)
    return f"the objects {objects_in_backpack} are collected with total profit {max_profit}"


def main():
    print(zero_one_knapsack(10, [
        {
            "name" : "object 1",
            "value" : 4,
            "weight" : 5
        },
        {
            "name" : "object 2",
            "value" : 3,
            "weight" : 4
        },
        {
            "name" : "object 3",
            "value" : 2,
            "weight" : 3
        },
        {
            "name" : "object 4",
            "value" : 1,
            "weight" : 1
        }
    ]))

main()


