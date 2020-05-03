import os
import time 
_dir='/home/srd/Desktop/music/DL_Music/data/genres/'
fol=[x for x in os.listdir(_dir) if x[-2:]!='mf']
i=1
#t1=time.time()
for f in fol:
	for s in os.listdir(_dir+f+'/'):
		song=_dir+f+'/'+s
		#print(i, end=' ')
		#i=i+1
		os.system('python app.py -t dl -m ../models/custom_cnn_2d.h5 -s '+ song )
		#break
# t2=time.time()
# print('Time taken', t2-t1)
