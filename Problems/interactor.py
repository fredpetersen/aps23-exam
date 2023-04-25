import random
import time
import goingincircles2 as prog


arrs = []

def createinput(n):
    newarr = []
    for i in range(n):
        newarr.append(random.randint(0,1))
    arrs.append(newarr)

#for i in range(45,1000):
#    createinput(i)

inc = 1

while inc < 5000:
    createinput(inc)
    inc *= 2


# call goingincircles2.ans() instead of responding to terminal

for arr in arrs:
    start_time = time.perf_counter()
    prog.initialize()
    currentcarriage = 0
    ans = prog.ans(arr[currentcarriage])

    while (not ans.startswith('!')):
        if (ans == "? left"):
            currentcarriage -= 1
        elif (ans == "? right"):
            currentcarriage += 1
        elif (ans == "? flip"):
            #print("Flipped from:")
            #print(arr[currentcarriage])
            arr[currentcarriage] += 1
            arr[currentcarriage] = arr[currentcarriage] % 2
            #print("Flipped to:")
            #print(arr[currentcarriage])
            #time.sleep(3)

        currentcarriage = (currentcarriage + len(arr)) % len(arr)
        
        # print(ans)
        # print(currentcarriage)
        # print(arr[currentcarriage])
        # print("===========")
        #time.sleep(0.1)
        ans = prog.ans(arr[currentcarriage])

    end_time = time.perf_counter()
    total_time = end_time - start_time
    _, answer = ans.split(" ")
    if int(answer) != len(arr):
        print(arr)
    else:
        print("(" + str(len(arr)) + "," +str(total_time) + ")")



print("Done!")