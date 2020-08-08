from k3.vis3 import *
#,a

"""
ffmpeg -i temp.mp4 -vf fps=1/8 temp/%d.png

ffmpeg -i Desktop/temp/temp.flv -vf "select='between(t,30,30.5)+between(t,45,45.5)+between(t,73,73.5)" -vsync 0 Desktop/temp/temp/%d.png
ffmpeg -i Desktop/temp/1/temp.mp4 -vf "select='between(t,90,95)" -vsync 0 Desktop/temp/1/temp/%d.png

https://stackoverflow.com/questions/21420296/how-to-extract-time-accurate-video-segments-with-ffmpeg
ffmpeg -i Desktop/temp/1/temp.mp4 -force_key_frames 90,100,120,130 Desktop/temp/1/temp_key.mp4
ffmpeg -ss 90 -i Desktop/temp/1/temp_key.mp4 -t 10 -vcodec copy -acodec copy -y Desktop/temp/1/temp_final.mp4
ffmpeg -ss 120 -i Desktop/temp/1/temp_key.mp4 -t 10 -vcodec copy -acodec copy -y Desktop/temp/1/temp_final2.mp4

"""

CA()

l = []
s3s = []
duration = unix('ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 Desktop/temp/1/temp.mp4')
duration = int(float(duration[0]))
for i in range(0,duration-2,10):
	l.append(str(i))
	l.append(str(i+2))
	s3s.append(d2s('ffmpeg -ss',i,'-i Desktop/temp/1/temp_key.mp4 -t',2,'-vcodec copy -acodec copy -y Desktop/temp/1/samples/'+str(i)+'.mp4'))
s0 = 'rm Desktop/temp/1/temp_key.mp4'
s1 = d2s('ffmpeg -i Desktop/temp/1/temp.mp4 -force_key_frames',','.join(l),'Desktop/temp/1/temp_key.mp4')
s2 = 'rm -r Desktop/temp/1/samples; mkdir -p Desktop/temp/1/samples'
cmds = [s2,s0,s1] + s3s + [s0]
for c in cmds:
	os.system(c)

def corner_spot():
	#cv2.circle(D['images'],(shape(D['images'])[1] - 25,shape(D['images'])[0] - 25),2,(0,255,0),2)
	cv2.line(
		D['images'],
		(shape(D['images'])[1] - 25,(shape(D['images'])[0] - 25)),
		(shape(D['images'])[1] - 25,(shape(D['images'])[0] - 0)),
		(0,200,0),
		1
	)
	cv2.line(
		D['images'],
		(shape(D['images'])[1] - 25,(shape(D['images'])[0] - 25)),
		(shape(D['images'])[1] - 0,(shape(D['images'])[0] - 25)),
		(0,200,0),
		1
	)

def set_x_y(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDOWN:
		T_PREV = D['T']
		D['T'] = time.time()
		
		if x > shape(D['images'])[1] - 25 and y > shape(D['images'])[0] - 25:#D['T'] - T_PREV < 0.5:# or D['f'] == -64:# and D['f'] < D['MX']:
			D['f'] += 64
			D['images'] = get_images(D['files'],D['f'])
			corner_spot()
			mci(D['images'],title='images')
			"""
			if len(D['LST']) > 0:
				print('double click, ignore',D['LST'][-1])
				D['LST'].pop()
				print(D['LST'])
			"""
		else:
			n = int(x/D['SHAPE'][1])+8*int(y/D['SHAPE'][0])+D['f']
			if n < D['MX']:
				was_in = False
				if n in D['LST']:
					was_in = True
				while n in D['LST']:
					D['LST'].remove(n)
				if not was_in:
					D['LST'].append(n)
				assert(len(D['LST'])==len(set(D['LST'])))
				print(D['LST'])
				x = 3*D['D'] + D['SHAPE'][1]*int(x/(D['SHAPE'][1]*1.0))
				y = 3*D['D'] + D['SHAPE'][0]*int(y/(D['SHAPE'][0]*1.0))

				if was_in:
					c = (0,0,255)
				else:
					c = (255,0,0)
				corner_spot()
				cv2.circle(D['images'],(x,y),4,c,5)
				mci(D['images'],title='images')

cv2.namedWindow("images")

cv2.setMouseCallback("images",set_x_y)

path = opjD('temp','temp')



D = {
	'LST':[],
	'T':time.time(),
	'files':sggo(path,'*.png'),
	'S':200,
	'D':4,
	'images':None,
	'SHAPE':None,
	'f':-64,
}
D['MX'] = len(D['files'])

def get_images(files,f):
	ys = []
	for y in range(8):
		xs = []
		for x in range(8):
			i = f + x + 8*y
			try:
				a,__ = load_image_with_orientation(files[i])
				b = get_resized_img(a,D['S'],D['S'],0,0)
				c = zeros((shape(b)[0]+D['D'],shape(b)[1]+D['D'],3),np.uint8)
				#print(shape(c))
			except:
				c = zeros(D['SHAPE'],np.uint8)
				b = get_resized_img(c,D['S'],D['S'],0,0)
				#print(shape(c))
			
			d = place_img_f_in_img_g(0,0,b,c,f_center=True,center_in_g=True)
			D['SHAPE'] = shape(d)
			xs.append(d)
		ys.append(np.concatenate(xs,axis=1))
		images = np.concatenate(ys,axis=0)
	return images


D['f'] = 0
D['images'] = get_images(D['files'],D['f'])
corner_spot()
mci(D['images'],title='images')
raw_enter()


#D['LST'] = list(set(D['LST']))

