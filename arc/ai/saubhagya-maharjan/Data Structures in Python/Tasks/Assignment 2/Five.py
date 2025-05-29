#peak element = element that is greater then its immediate neighbours
# i.e arr[i] < arr[i+1] > arr[i+2]

x = [1, 2, 3, 1, 10, 8]
peaks = []

for i in range (1,len(x)-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
        peaks.append(x[i])

print(f"Peaks: {peaks}")