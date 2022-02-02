with open("input.txt",'r') as f:
    data = f.read()
    formatted_data = str.splitlines(data)
    nb_increase = 0
    for depth in range(-1,len(formatted_data)):
        if (formatted_data[depth]>=formatted_data[depth-1]):
            nb_increase = nb_increase+1
            
    print(nb_increase)
