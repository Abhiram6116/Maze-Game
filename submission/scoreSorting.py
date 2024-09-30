import os
# This python file is to update the score into scoreSorted.txt

class Sorting:
    def Sort(self,lvl,blah):
        if int(blah/1000) >= 1:
            n='4,'
        elif int(blah/100) >= 1:
            n='3,'
        elif int(blah/10) >= 1:
            n='2,'
        f=open('scoreSorted.txt','r+')
        old = f.read()
        f.seek(0)
        f.write(n+str(blah)+","+lvl[1]+lvl[0]+'\n'+old)
        f.seek(0)
        lin=f.readlines()
        f.close()
        os.remove('scoreSorted.txt')
        lin.sort(reverse=True)
        g=open('scoreSorted.txt','w')
        g.writelines(lin)
        g.close()
