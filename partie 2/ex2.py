with open("input.txt",'r') as f:
    data = f.read()
    formatted_data = str.splitlines(data)
    formatted_data = [int(x)for x in formatted_data]
    

    nb_increase = 0
    i = 0
    while i < len(formatted_data)-3:
        sum1 = formatted_data[i]+formatted_data[i+1]+formatted_data[i+2]
        sum2 = formatted_data[i+1]+formatted_data[i+2]+formatted_data[i+3]
        
        if(sum2>sum1):
            nb_increase= nb_increase+1
        i=i+1
    print(nb_increase)