import sys
  
# setting path
sys.path.append('../')

from meme import Meme

if __name__ == '__main__':
    m = Meme("x.meme")
    print(m.print(name="zzz"))
