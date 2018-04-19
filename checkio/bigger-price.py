def bigger_price(limit, data):

    sortedlist = sorted(data, key=lambda x: list(x.values())[0], reverse=True)
    print(sortedlist)
    reslut = []
    for i in range(limit):
        reslut.append(sortedlist[i])
    return (reslut)



bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ])
print("--"*30)

bigger_price(2,[{"price":100,"name":"bread"},{"price":138,"name":"wine"},{"price":15,"name":"meat"},{"price":1,"name":"water"}])


# if __name__ == '__main__':
#     from pprint import pprint
#     print('Example:')
#     pprint(bigger_price(2, [
#         {"name": "bread", "price": 100},
#         {"name": "wine", "price": 138},
#         {"name": "meat", "price": 15},
#         {"name": "water", "price": 1}
#     ]))


    # assert bigger_price(2, [
    #     {"name": "bread", "price": 100},
    #     {"name": "wine", "price": 138},
    #     {"name": "meat", "price": 15},
    #     {"name": "water", "price": 1}
    # ]) == [
    #     {"name": "wine", "price": 138},
    #     {"name": "bread", "price": 100}
    # ], "First"
    #
    # assert bigger_price(1, [
    #     {"name": "pen", "price": 5},
    #     {"name": "whiteboard", "price": 170}
    # ]) == [{"name": "whiteboard", "price": 170}], "Second"
    #
    # print('Done! Looks like it is fine. Go and check it')
