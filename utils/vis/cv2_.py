
from k3.utils.misc import *
import cv2
try:
    # pip install opencv-python==4.1.2.30
    import cv2
    imread = cv2.imread
    imsave = cv2.imwrite
except:
    if False:
        cr("*** Couldn't import cv2 ***")
        if 'torch' in sys.modules:
            cr("Note, torch already imported. This can block normal cv2 import.")




try:
    def function_close_all_windows():
        import matplotlib.pyplot as plt
        plt.close('all')
        try:
            cv2.destroyAllWindows()
        except:
            pass
    CA = function_close_all_windows

    def mci(img,delay=33,title='mci',scale=1.0,color_mode=cv2.COLOR_RGB2BGR,fx=0,fy=0):
        title = d2s(title)
        if not fx and not fx:
            fx = scale
            fy = scale
        if len(shape(img)) == 2:
            color_mode = cv2.COLOR_GRAY2BGR
        img = cv2.cvtColor(img,color_mode)
        scale_img = cv2.resize(img, (0,0), fx=fx, fy=fy, interpolation=0)
        cv2.imshow(title,scale_img)
        k = cv2.waitKey(delay)
        return k


    def mcia(img_block,delay=33,title='mcia',scale=1.0,color_mode=cv2.COLOR_RGB2BGR):
        assert(len(shape(img_block)) == 4)
        for i in range(shape(img_block)[0]):
            k = mci(img_block[i,:,:,:],delay=delay,title=title,scale=scale,color_mode=color_mode)
            if k == ord('q'):
                return


    def mcia_folder(path,delay=33,title='mcia_folder',scale=1.0,color_mode=cv2.COLOR_RGB2BGR):
        l=load_img_folder_to_list(path)
        mcia(array(l),delay=delay,title=title,scale=scale,color_mode=cv2.COLOR_RGB2BGR)

except:
    print("Don't have cv2")


if __name__ == '__main__':
    
    eg(__file__)

    mci(z55(rndn(20,20,3)),scale=20)

    raw_enter()
#EOF