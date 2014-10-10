import pickle

y={"a": "b", "ccc": "ddddd", "efghi": "hhhh"}

print (y)

# store dictionary in file
pickle.dump(y, open('/home/tterebus/python_sandbox/pickle/tt.txt', "wb"))


# load dictionary from the pickle file
z = pickle.load( open('/home/tterebus/python_sandbox/pickle/tt.txt', "rb") ) 

print(z)
