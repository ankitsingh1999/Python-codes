data ="xbox 360! 200$ ! brand new"
n_data = data[data.index('x'):data.find('!')]
print(n_data)
new_data =data[16:]
print(new_data)


#use of find
secnew_data = data[data.find('!')+7:data.find('!',10)]
print(secnew_data)     
