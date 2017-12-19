import time
import visa
rm=visa.ResourceManager()
li=rm.list_resources()
for index in range(len(li)):
    print(str(index)+" - "+li[index])
choice = input("Which device?: ")
vi=rm.open_resource(li[int(choice)])

print(vi.query("*idn?"))

vi.write("outp on")
vi.write("apply ch1,0.050,2")
command = "apply ch1,"
for lev in range(100):
    cmd = command + str(lev*0.005) + ",2"
    #print(cmd)
    vi.write(cmd)
    time.sleep(1)
time.sleep(1)
vi.write("outp off")
