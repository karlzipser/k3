import scipy.stats as stats

CA()

D = {
	'ad':[0.74, 0.89, 0.59, 0.82, 1.07, 0.62],

	'cy':[2.0, 1.4, 1.6, 4.2, 1.1],

	'oc':[2.7, 0.8, 2.4, 0.9, 1.4],

	'cyoc':[2.0, 1.4, 1.6, 4.2, 1.1]+[2.7, 0.8, 2.4, 0.9, 1.4],

	'ocad':[2.7, 0.8, 2.4, 0.9, 1.4]+[0.74, 0.89, 0.59, 0.82, 1.07, 0.62],

}

c = len(D)
for k in D:
	x = D[k]
	y = list(0 * na(x) + c)
	plot(x,y,'.')
	c -= 1
	print(stats.ttest_ind(a=D['ad'],b=x,equal_var=False))

# https://stackoverflow.com/questions/16082171/curve-fitting-by-a-sum-of-gaussian-with-scipy