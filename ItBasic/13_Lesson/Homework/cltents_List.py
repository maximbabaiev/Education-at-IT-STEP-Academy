clients_list = ["bob", "rob", "rob", "pit", "rob"]

cont = {}

def countClients():
    for i in clients_list:
        cont[i] = cont.get(i, 0) + 1
    dub = {i: count for i, count in cont.items() if count > 1}
    print(dub)
    print("rob gets a discount")



countClients()