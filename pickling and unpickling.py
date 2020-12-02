// Pickling

import pickle
def pickle_data():
    data = {
                'name': 'SrajanJaiswal',
                'profession': 'Student,
                'Roll number': '170'
        }
    filename = 'PersonalInfo'
    outfile = open(filename, 'wb')
    pickle.dump(data,outfile)
    outfile.close()
    
pickle_data()

// Unpickling

import pickle
def unpickling_data():
    file = open(PersonalInfo,'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data
print(unpickling_data())
