import sys
  
# setting path
sys.path.append('../')

from meme import MemeInterpret

if __name__ == '__main__':
    m = MemeInterpret("x.meme")
    print(m.result(name="zzz"))
