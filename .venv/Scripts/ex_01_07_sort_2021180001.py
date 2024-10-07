array = [
       46,      82,      21,      58,      22,      54,      71,     215,      99,     227,
       73,      24,      17,      44,     244,      78,      25,      66,      47,       3,
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92,
       83,     100,      94,      40,       5,     458,     364,      26,      64,     635,
       90,     489,      72,     504,      88,      97,     226,     218,     186,     268,
]
count = len(array)
def sort_bubble(arr):
    print('=' * 60)
    print(f'before: {arr}')

    end =  count - 1
    while end > 0:
        last=1
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last=i+1
        end=last-1
    print(f'after : {arr}')

def sort_select(arr):
    print('=' * 60)
    print(f'before: {arr}')

    for i in range(count-1):
        min_value = arr[i]
        min_at=i
        for j in range(i+1,count):
            if min_value > arr[j]:
                min_at = j
                min_value = arr[j]
        arr[i], arr[min_at] = arr[min_at], arr[i]

    print(f'after : {arr}')

def sort_insert(arr):
    print('=' * 60)
    print(f'before: {arr}')
    for i in range(1, count):
        cur = arr[i]
        cur_index = i
        while cur_index > 0:
            if arr[cur_index- 1] > cur:
                arr[cur_index] = arr[cur_index-1]
                cur_index-=1
            else:
                break
        arr[cur_index] = cur


    print(f'after : {arr}')

def sort_shell(arr):
    print('=' * 60)
    print(f'before: {arr}')
    for gap in [31, 15, 7, 3, 1]:
        for i in range(gap, count):
            cur = arr[i]
            cur_index = i
            while cur_index > 0:
                if arr[cur_index - 1] > cur:
                    arr[cur_index] = arr[cur_index - 1]
                    cur_index -= 1
                else:
                    break
            arr[cur_index] = cur
    print(f'after : {arr}')

def main():
    sort_bubble(array[:])
    sort_insert(array[:])
    sort_select(array[:])
    sort_shell(array[:])

if __name__ == '__main__':
  main()

