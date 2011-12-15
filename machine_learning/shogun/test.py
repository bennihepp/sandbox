from sg import sg
from pylab import figure,pcolor,scatter,contour,colorbar,show,imshow
from numpy import meshgrid,reshape,linspace,ones,min,max,concatenate,transpose
from numpy import ravel,array
from numpy.random import randn
import numpy

num=200;
sg.send_command('loglevel ALL')
features=concatenate((randn(num,2)-1,randn(num,2)+1),0)
labels=concatenate((-ones([1,num]), ones([1,num])),1).flat
sg.set_features("TRAIN", features)
sg.set_labels("TRAIN", labels)
sg.send_command('set_kernel GAUSSIAN REAL 10 5')
sg.send_command('init_kernel TRAIN')
sg.send_command('new_svm GPBT')
sg.send_command('c 100')
sg.send_command('svm_train')
sv=sg.get_svm();
print sv
figure()

x1=linspace(1.2*min(features),1.2*max(features), 50)
x2=linspace(1.2*min(features),1.2*max(features), 50)
x,y=meshgrid(x1,x2);
testfeatures=transpose(array((ravel(x), ravel(y))))

sg.set_features("TEST", testfeatures)
sg.send_command('init_kernel TEST')
z=sg.svm_classify()

z.resize((50,50))
i=imshow(transpose(z),  origin='lower', extent=(1.2*min(features),1.2*max(features),1.2*min(features),1.2*max(features))) #for smooth visualization
scatter(features[:,0],features[:,1], s=20, marker='o', c=labels, hold=True)
contour(x, y, transpose(z), linewidths=1, colors='black', hold=True)
colorbar(i)
show()

