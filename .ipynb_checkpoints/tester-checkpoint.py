def test_my_range(start, stop=None, step=None):
    if start == None:
        raise ValueError("invalid starting point")
    index = 0 
    end = start
    move = 1
    if step != None:
        move = step
    if start != None and stop != None:
        index = start
    if stop != None:
        end = stop
    while True:
        if index > end:
            break
        print(index)
        index += move