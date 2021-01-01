#!/usr/bin/env python3

from k3.utils import *




try:
	# ln -s Library/Mobile\ Documents/com\~apple\~CloudDocs/iCloud-bucket/idata bucket/idata
	#from bucket.idata.warn import rndWarning
	import bucket.idata.warn
except:
	cE("Couldn't import rndWarning, try making symbolic link.")
	assert False


cr(__file__)

A = get_Arguments({
	('min', 'repeat every --min minutes')        : 15,
	('sd', 'SD of random variation, in minutes') : 1,
	('one','only one instance can run') : True,
})

record_PID(__file__,just_one=A['one'])

def get_timer():
	r = rndn()*A['sd']
	timer = Timer(max(60*(A['min'] + r),0))
	return timer

timer = get_timer()

print_timer = Timer(60)
print_timer.trigger()


while True:
	if print_timer.check():
		print_timer.reset()
		cr(
			'Warning in',
			datetime.timedelta(seconds=int(timer.time_s - timer.time())),
		)
	if timer.check():

		timer = get_timer()

		txt,title = bucket.idata.warn.rndWarning()
		#txt,title = 'Warning','Move around'

		result = do_dialog( txt, title )

		if result == '':
			cE('button returned:CANCEL')
		else:
			cg(result)

	time.sleep(30)

#EOF
