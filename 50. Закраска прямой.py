n = int(input())
segments = []
for _ in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort()
total = 0
current = segments[0]  
for segment in segments[1:]:
    if segment[0] <= current[1]: 
        current = (current[0], max(current[1], segment[1]))
    else:      
        total += current[1] - current[0]
        current = segment
total += current[1] - current[0]

print(total)