neg_values = {100,50,30,10,50,70,50,22.34,10,100,20,20,60,14.99,20,70,3.90,30,10.02,60,1.95,30,3,20,60,1.95,6.99,40,27.60,30,30
          ,38.02,60,40,20.19,30,5.99,6.75,30,6.10,30,120,1.95,20.55,40,30,20,30,30,3.35}

pos_values = {36,212.34,200,219,170,30,40,50,50,30,120,55,50,30,30}
total_value = pos_values - neg_values

#print(sorted(negative_values))

print("negative value amount = " + str(sum(neg_values)))
print("positive value amount = " + str(sum(pos_values)))
print("total amount = ")