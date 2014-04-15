def get_item():
    item = raw_input("Give me an item (q to quit): ")
    return item

def get_list():
    my_list = []
    item = "":
    while item != 'q':
        