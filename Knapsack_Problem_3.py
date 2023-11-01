""" this module contains one function : multiple_knapsack"""
def multiple_knapsack(capacities, objects):
    """uses the value-to-weight ratio algorithm to solve multiple knapsacks problem
        Args:
            capacities: defines the maximum knapsack capacities of the available knapsack
            objects: defines the available objects to take with their names, weights and values
        
        Description: this implementation first sorts the objects with value-to-weight ratio in descending order
                     similarly with the knapsacks, they're sorted to be filled from the largest to the tiniest
                     for each knapsack, if the object fits , it is put entirely in the knapsack, otherwise it is fractioned
                     this allows putting the most expensive object with the maximum profit(entities or fractions)
    """
    max_profit = 0
    objects_in_knapsacks = []

    sorted_objects = sorted(objects, key=lambda x: x["value"] / x["weight"], reverse=True)
    capacities.sort(reverse=True)
    for i in range(len(capacities)):
        while sorted_objects:
            if sorted_objects[0]["weight"] < capacities[i]:
                objects_in_knapsacks.append(sorted_objects[0]["name"])
                max_profit += sorted_objects[0]["value"]
                capacities[i] -= sorted_objects[0]["weight"]
                sorted_objects.pop(0)
            else:
                objects_in_knapsacks.append(sorted_objects[0]["name"])
                max_profit += sorted_objects[0]["value"] * capacities[i] / sorted_objects[0]["weight"]
                capacities[i] = 0
                sorted_objects.pop(0)
                break
                

    return f"The objects {objects_in_knapsacks} are collected with a total profit of {max_profit}"

    

  


def main():
    print(multiple_knapsack([10,15], [
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


