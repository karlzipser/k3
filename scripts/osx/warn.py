#!/usr/bin/env python3

from k3.utils import *

record_PID(__file__,just_one=True)


try:
	# ln -s Library/Mobile\ Documents/com\~apple\~CloudDocs/iCloud-bucket/idata bucket/idata
	from bucket.idata.warn import rndWarning
except:
	cE("Couldn't import rndWarning, try making symbolic link.")
	assert False


cr(__file__)

A = get_Arguments({
	('min', 'repeat every --min minutes')        : 15,
})

timer = Timer(A['min']*60)
print_timer = Timer(60)
print_timer.trigger()


while True:
	if print_timer.check():
		print_timer.reset()
		cr(
			'Warning in',
			datetime.timedelta(seconds=int(A['min']*60 - timer.time())),
		)
	if timer.check():
		timer.reset()

		txt,title = rndWarning()
		#txt,title = 'Warning','Move around'

		result = do_dialog( txt, title )

		if result == '':
			cE('button returned:CANCEL')
		else:
			cg(result)

	time.sleep(30)

#EOF
