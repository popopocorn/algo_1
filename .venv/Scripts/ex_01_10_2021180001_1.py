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

    for i in range(left + 1, right + 1):
        v= arr[i]
        j=i-1
        while j>=left and arr[j] > v:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = v

def merge(arr, left, right, end):
    merged = []
    l, r=left, right
    while l < right and r<=end:
        if arr[l]<=arr[r]:
            merged.append(arr[l])
            l+=1
        else:
            merged.append(arr[r])
            r+=1
    while l<right:
        merged.append(arr[l])
        l+=1

    while r<=end:
        merged.append(arr[r])
        r+=1

    arr[left:end+1] = merged
    print(arr)

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
