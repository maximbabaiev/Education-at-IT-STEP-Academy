import pickle

original = {'Illinois': 'Aurora',
            'Massachusetts': 'Boston',
            'Florida': 'Orlando'}

pickled = pickle.dumps(original)

unclenched = pickle.loads(pickled)

print(original, pickled, unclenched)
