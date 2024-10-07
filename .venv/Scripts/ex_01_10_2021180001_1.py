#merge sort
words = [

  '2021180001', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',

  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',

  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',

  'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell',

  'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude',

  'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor',

  'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck',

  'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote',

  'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop',

  'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise',

  'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse',

]

def insertion_sort(arr,left,right):
    count = right-left+1
    for i in range(1, count):
        v= arr[i]
        j=i
        while j>0:
            if arr[j-1]>v:
                arr[j] = arr[j-1]
                j-=1
            else:
                break
        arr[j] = v
#여기서 문제 생겼나?
def merge(arr, start_of_first, start_of_second, end_of_second):
    merged = []
    l, r=start_of_first, start_of_second
    while l < start_of_second and r<=end_of_second:
        if arr[l]<=arr[r]:
            merged.append(arr[l])
            l+=1
        else:
            merged.append(arr[r])
            r+=1
    while l<start_of_second:
        merged.append(arr[l])
        l+=1

    while r<=end_of_second:
        merged.append(arr[r])
        r+=1
    print(merged)
    arr[start_of_first:end_of_second+1] = merged
def merge_sort(arr, start, end):#end=inclusive

    if end - start + 1 <= 5:
      insertion_sort(arr, start, end)
      return

    first_index_in_right = ((start+end)//2)+1

    merge_sort(arr, start, first_index_in_right-1)
    merge_sort(arr, first_index_in_right, end)
    merge(arr, start, first_index_in_right, end)

merge_sort(words, 0, len(words)-1)
print(words)
