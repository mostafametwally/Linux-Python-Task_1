X="Rte_ReceiverPullCB_Rte_Rx_000000_valueSrDatumDEF_123456789ABCDEF_123456789ABCDEF_123456789ABCDEF_123456789ABCDEF_12DECD09269A623DEB46DCD9AA19059C66_0"
# print(X)
# print (type(X))
# print (len(X))
# thisdic={
#     "name": "Mostafa",
#     "Age": 25,
#     "Score": "Good"
# }
# num= input("please Enter your value: ")
# print(f"the value you entered is {num}")
# print(f"the Value You Entered: {num}")
# print(thisdic)
# print(thisdic.keys())
# print(thisdic.values())
# print(len(thisdic))
# ls=list(range(1,100))
# set_=set(ls)
# print(set_,end='\n')
# print(list(X))

x=[1,2,3,4,5,6,7,4,4,4,4,4,4,4,4,48,9,10]
count=0
for i in x:
    if i==4:
        count+=1
print(count)
vaule=['a','e','i','o','u']
total=0
for i in X.lower():
    if i in vaule:
        print(f"The letter {i} is vaule at index {X.index(i)}")
        total+=1
print(f"The total is {total}")