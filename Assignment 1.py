#creating  a list
L = [1,3,5,7,"Hello",'World',56.79,55.20]
print("Printing List\n",L)

#adding element to the list
L.append(30)
print("\nAdding an element\n",L)

#removing element from the list
L.remove('World')
print("\nRemoving an element\n",L)


#modifying an element in the list
L[-2] = 0.33
print("\nModyfing the list\n",L)

#creting a dictionary
D = {'Name':'Tifa', 'Age':20, 'Designation':'Intern'}
print("\nPrinting Dictionary\n",D)

#adding element to the dictionary
D['Salary'] = 25000
print("\nAdding Element to dictionary\n",D)

#removing element from the dictionary
del D['Designation']
print("\nRemoving an element from dictonary\n",D)

#modifying an element in the dictionary
D['ID'] = "EMP095"
print("\nModifying the dictionary\n",D)

#creting a set
S = {2,4.6,True,0,"Thirty"}
print("\nPrinting a Set\n",S)

#adding element to the set
S.add(-45)
print("\nAdding element in the set\n",S)

#removing element from the set
S.remove(4.6)
print("\nRemoving element in the set\n",S)

#modifying an element in the set
S.discard("Thirty")
S.add('Pizza')
print("\nModifying the set\n",S)


