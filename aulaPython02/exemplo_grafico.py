from pylab import *

ent1 = arange(0., 7., .1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai2 - sai1

subplot(211)
plot(ent1, sai1, 'bo;', ent1, sai2, 'g^-')
legend(['Cossenos', "Senos"])
