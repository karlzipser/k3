


imgs = [
	'Pictures/Yosemite photos 2019/IMG95201908319508202094895HDR.jpg',
	'Pictures/Yosemite photos 2019/IMG95201908319509380484595HDR.jpg',
	'Pictures/Yosemite photos 2019/IMG95201908319508125490795HDR.jpg',
	'Pictures/Yosemite photos 2019/IMG952019083195075136440.jpg',
	'Pictures/Yosemite photos 2019/IMG952019083195075144754.jpg',
	'Pictures/Yosemite photos 2019/IMG95201908319509375050195HDR.jpg',
	'Pictures/Yosemite photos 2019/IMG95201908319509515180795HDR.jpg',
]

def big_img(im,x,n):
	return """
  <div class="mySlides">
    <div class="numbertext">XXX / NNN</div>
    <img src="SRC" style="width:100%">
  </div>

""".replace('XXX',str(x)).replace('NNN',str(n)).replace('SRC',im)


def small_img(im,x):
	return """
    <div class="column">
      <img class="demo cursor" src="SRC" style="width:100%" onclick="currentSlide(XXX)" alt="alt text">
    </div>
""".replace('XXX',str(x)).replace('SRC',im)



b,s = '',''
for i in rlen(imgs):
	b += big_img(imgs[i],i+1,len(imgs))
	s += small_img(imgs[i],i+1)
print(b)
print(s)


