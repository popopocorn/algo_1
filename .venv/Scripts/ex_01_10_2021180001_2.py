#quick sort
import random
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

def partition(arr, start, end):
    random_index = random.randint(start, end)
    arr[start], arr[random_index] = arr[random_index], arr[start]
    p=start+1
    q=end
    while True:
        while True:
            p+=1
            if q<p: break
            if p> end or arr[p]>=arr[random_index]: break
        while True:
            q-=1
            if q<p: break
            if q<start or arr[q]<arr[random_index]: break

        if p>=q: break
        arr[p], arr[q] = arr[q], arr[p]
    if start !=q:
        arr[start], arr[q] = arr[q], arr[start]

    return q


def insertion_sort(arr,left,right):

    for i in range(left + 1, right + 1):
        v= arr[i]
        j=i-1
        while j>=left and arr[j] > v:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = v

def quick_sort(arr, start, end):
    size = end - start + 1
    if size <=5:
        #insertion_sort(arr, start, end)
        return
    pivot_index = partition(arr, start, end)
    quick_sort(arr, start, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, end)





quick_sort(words, 0, len(words) - 1)
insertion_sort(words, 0, len(words) - 1)
print(words)