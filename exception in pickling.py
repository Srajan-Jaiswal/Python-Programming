import pickle
while True:
    try:
        GetList = input("Enter the List: ")
        with open(GetList, 'rb') as f:
            mylist = pickle.load(f)
    except (IOError, OSError, pickle.PickleError, pickle.UnpicklingError):
        print("Invalid File")
    else:
        break
