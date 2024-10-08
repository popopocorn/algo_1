coords = [

(620, 332), (784, 623), (182, 555), (1413, 451), (1092, 660),

(30, 217), (525, 148), (1311, 887), (1228, 353), (54, 68),

(1155, 838), (467, 563), (86, 535), (32, 630), (739, 766),

(1386, 16), (1565, 828), (868, 264), (1301, 786), (883, 415),

(479, 534), (1101, 35), (671, 405), (1478, 230), (1343, 834),

(647, 97), (972, 447), (327, 334), (716, 151), (233, 411),

(486, 431), (1017, 381), (329, 830), (1286, 739), (1528, 248),

(216, 294), (1306, 540), (204, 715), (77, 120), (97, 178),

(809, 28), (354, 205), (123, 551), (248, 828), (888, 139),

(594, 494), (576, 702), (64, 218)

]
y_sorted=[]
x_sorted=[]
def closest_pair(arr, left, right):
    size = right - left + 1
    '''배열의 사이즈를 확인해 1일경우 거리 X<<호출되는 일 없음
    2일 경우 두 점의 거리 return
    3읽경우 bruteforce
    4 이상일 경우 x의 값을 기준으로 정렬
    정렬 방법 1: coords에 sort 사용'''
    if size <= 1:
        return -1, -1, 0
    if size == 2:
        s, e, d = left, right, distance(arr[left], arr[right])
        return s, e, d
    if size==3:
        s, e, d=brute_force(arr, left, right)
        return s, e, d
    last_in_left=size//2+left-1

    ls, le, ld = closest_pair(arr, left, last_in_left) #왼쪽에서 가장 가까운 거리
    rs, re, rd= closest_pair(arr, last_in_left+1, right) #오른쪽 그룹에서 가장 가까운 거리
    s, e, d = (ls, le, ld) if ld<=rd else (rs, re, rd) # 둘이 비교

    cx1=arr[last_in_left][0] - d #가운데 점에서 d만큼 왼쪽
    cx2=arr[last_in_left][0] + d #       //      오른쪽
    index1, index2=-1, -1
    if [c[2] for c in x_sorted if c[0] >= cx1 and c[2] >= left]:
        index1=min(c[2] for c in x_sorted if c[0] >= cx1 and c[2] >= left)
    if [c[2] for c in x_sorted if c[0] <= cx1 and c[2] <= right]:
        index2=max(c[2] for c in x_sorted if c[0] <= cx1 and c[2] <= right)

    strip = [c for c in y_sorted if c[2] >=index1 and c[2] <=index2]
    n_strip=len(strip)
    for s1 in range(n_strip):
        c1=strip[s1]
        for s2 in range(s1 + 1,n_strip):
            c2=strip[s2]
            dy=c1[1] - c2[1]
            if dy<0: dy= -dy
            if dy>d:
                break
            dx = c1[0] - c2[0]
            if dx>d:
                continue
            dist=(dx**2+dy**2)
            if d > dist:
                d=dist
                s, e = c1[2], c2[2]

    return s, e, d


def distance(a, b):
    return (b[0]-a[0])**2+(b[1]-a[1])**2

def brute_force(arr, left, right):
    closest = [-1, -1, float('inf')]
    for i1 in range(left, right+1):
        c1=coords[i1]
        for i2 in range(i1+1, right+1):
            c2=coords[i2]
            dist = distance(c1, c2)
            if dist < closest[2]:
                closest = [c1, c2, dist]
    return closest

def devide_and_conquer():
    coords.sort(key=lambda x: x[0])
    global y_sorted, x_sorted
    x_sorted = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]

    y_sorted = sorted(x_sorted, key=lambda x: x[1])  # x좌표로 정렬되어 있는 coords의 인덱스를 유지하며 y로 정렬

    s,e,d = closest_pair(coords, 0, len(coords)-1)

    return s, e, d



    '''X좌표: 중간점X좌표-d~중간점x좌표+d
    index1: x좌표가 -d이상인 점들중 가장 왼쪽index
    index2: // +d 이하인 점들중 가장 오른쪽index
    strip=[t for t in y_sorted if t[2] >= index1 and t[2] <= index2]
    '''

s, e, d=brute_force(coords, 0, len(coords)-1)
print(f'brute_force\'s result: {s}, {e}, {d}')
s, e, d=devide_and_conquer()
print(f'devide_and_conquer\'s result: {s}, {e}, {d}')
