#import build_album as bm
#from build_album import make_album as ma
#import build_album as ba
from build_album import *

music = make_album('Jimi Hendrix', 'Are you experienced')
print(music)
music = make_album('Prince', 'Purple Rain', 10)
print(music)
music = make_album('Pink Floyd', 'The Wall', 15)
print(music)