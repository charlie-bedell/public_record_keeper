import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 1.10
suefile = open('suefile.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()
