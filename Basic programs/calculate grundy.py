
gru = []
vec = []
mx = 0

def calculate_grundy() :
    gru.append(0)
    for i in range(1, mx + 1) :
        poss = []
        for x in vec :
            if x > i :
                break
            else :
                poss.append(gru[i - x])
        inc = 0
        while True:
            flag = 0
            for x in poss :
                if x == inc :
                    flag = 1
                    break
            if flag == 0 or len(poss) == 0:
                break
            else :
                inc = inc + 1
        gru.append(inc)
  
#main function()
#calculate grundy
mx = int(input())
vec = list(map(int, input().split()))
vec.sort()
calculate_grundy()
print(gru)
