import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:

	#make a random walk and plot the points
	rw = RandomWalk(10000)
	rw.fill_walk()

	# set the size of the plotting window
	plt.figure(dpi=128, figsize=(10, 6))

	""" generate a list of numbers equal to the 
	number of points in the walk"""
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=0.5, alpha=1)

	# emphasize the last and last points
	plt.scatter(0, 0, c='green', edgecolors='none', s=15)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=15)

	# remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break