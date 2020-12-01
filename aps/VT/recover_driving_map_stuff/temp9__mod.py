from k3 import *
#,a
from k3.drafts.recover_driving_map_stuff.utils import *

Arguments = {}

Arguments['run'] = 'tegra-ubuntu_31Oct18_16h06m32s'#'Mr_Black_24Sep18_18h52m26s'#'tegra-ubuntu_31Oct18_16h06m32s'  # 


Colors = {'direct':'b','left':'r','right':'g'}

if 'o' not in locals():
  o = {}
assert type(o) is dict


if 'O' not in o:

  if len(sggo(opjD('Data/train/h5py',Arguments['run']))) > 0:
      run_type = 'train'
      #assert(False)
  elif len(sggo(opjD('Data/validate/h5py',Arguments['run']))) > 0:
      run_type = 'validate'
  else:
      clp(Arguments['run'],'not found')
      assert False

  o['L'],o['O'],__flip = open_run2(Arguments['run'])

  o['xy'] = [na([0,0])]

  L = o['L']
  cm(len(L['motor']))
  for i in rlen(L['motor']):
      cm(i)
      a = vec(
          L['gyro_heading_x_meo'][i],
          L['encoder_meo'][i],
          L['motor'][i],
      )
      o['xy'].append(o['xy'][-1]+a)

  o['S'] = lo(opjD('Data/outer_contours/output_2_data',run_type,Arguments['run']))
  cm(13)
cm(0)

def get_offshoot(A,B,r,theta):
  m,b = curve_fit(f___,(A[0],B[0]),(A[1],B[1]))[0]
  alpha = corrected_angle(m,B,A)
  C = B + na([0,r])
  D = rotatePoint(B,C,90-theta+alpha+0)
  return D







figure(1)
clf()
plt_square()
for i in range(5000,len(L['motor']),1):

  cm(1)

  figure(1)

  clf()

  if not L['drive_mode'][i]:
    cr(i,'d')
    continue

  if L['motor'][i] < 54 or L['encoder'][i] < 2.0:
    cr(i,'e')
    continue

  if i not in o['S']:
    cr(i)
    continue

  else:
    cm(i,ra=0)
    x,y  = o['xy'][i][0],o['xy'][i][1]

  clf();plt_square();xylim(x-20,x+20,y-20,y+20)



  b = o['S'][i]
  
  for s in ['left','right']:
    xy = b['outer_countours_rotated_'+s] + o['xy'][i]
    pts_plot(xy,color=Colors[s],sym='-')
    #plot(xy[:,0],xy[:,1],ms=3)
  plot(na([-10,10])+x,na([0,0])+y,'k:')
  plot(na([0,0])+x,na([-10,10])+y,'k:')
  plot(x,y,'ko')




  for s in ['left','right']:
    for j in rlen(b['outer_countours_rotated_'+s]):
      a = b['angles_'+s][j]
      a = min(np.abs(a),400)
      marker_size = int(a/2.)
      #pts_plot(b['outer_countours_rotated_'+s][j] + o['xy'][i],Colors[s],sym='.',ms=marker_size)
      if j > 0:
        if s == 'left':
          aa = 180-a
        else:
          aa = a-180
        D = get_offshoot( 
          b['outer_countours_rotated_'+s][j-1] + o['xy'][i],
          b['outer_countours_rotated_'+s][j] + o['xy'][i],
          np.abs(a)/10.,
          aa,
          )

        pts_plot([b['outer_countours_rotated_'+s][j] + o['xy'][i],D],Colors[s],sym='-')
        pts_plot(D,Colors[s])
        
















  
  #mci(o['O']['left_image']['vals'][i],title='left_image',scale=3.0)

  figure(9)
  mi(o['O']['left_image']['vals'][i],9)


  for s in ['left','right']:

      c = []
      q = b['outer_countours_rotated_'+s]
      w = double_interp_2D_array(q)#[:33,:])
      w = double_interp_2D_array(w)
      w = double_interp_2D_array(w)
      q = w
      #q = np.concatenate((w,q[33:,:]))

      for w in rlen(q):
          a = q[w,:]
          bb = fit3d.point_in_3D_to_point_in_2D(
              a,
              height_in_pixels = 94,
              width_in_pixels = 168,
              backup_parameter=1,
          )
          if False not in bb:
              c.append(bb)
      c = na(c)
      try:
          pts_plot(c,color=Colors[s],sym='.')
      except:
          clp('Exception, shape(c) =',shape(c),'`wrb')
  spause()
  #if i == 3400:
  #  raw_enter()
  time.sleep(0.00005)
  #cm(a,ra=1)

#,b


