import time,os
class test:
    u = 0
    p = 0
    def __init__(self,a,b):
        self.u = a
        self.p = b
    def tt(self):
        print self.p
        print self.u
a = 10
def re_exe(cmd, inc = 60):
    while (a):
        os.system(cmd)
        time.sleep(inc)
re_exe("echo %time%", 5)
tt = test(3,2)
tt.tt()
