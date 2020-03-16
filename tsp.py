from itertools import permutations as pm

l = [(1, 1), (2, 3), (2, 1), (3, 6), (7,5)]
assert len(l) > 0
def distance(a, b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
	
def sub_distance(l):
	if len(l) == 1:
		return 0
	elif len(l) == 2:
		return distance(l[0], l[1])
	else:
		return distance(l[0], l[1]) + sub_distance(l[1:])
		
def round_distance(l):
	return distance((0, 0), l[0]) + sub_distance(l) + distance((0,0), l[-1]), l

lists = list(pm(l))
remove_reverse = [list(v) for k, v in enumerate(lists) if v[::-1] not in lists[:k]]

results = list(map(round_distance, remove_reverse))
results = sorted(results, key=lambda pair : pair[0])
print("Given points are", l)
print('The shortest round distance of given points is {0} the route is {1}', results[0])
