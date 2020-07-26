import heapq
from collections import Counter
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]
# Method 1 
def topKFrequent(k, keywords, reviews):
    '''
    k: int
    keywwords: list of string
    reviews: list of string
    '''
    word_list = []
    
    for review in reviews:
        word_list += set(review.lower().replace('[^a-z0-9]', '').split())
    
    
    count = Counter(word_list)
    heap = []
    for word, freq in count.items():
        if word in keywords:
            heapq.heappush(heap, [freq,word])
            if len(heap) > k:
                heapq.heappop(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)][::-1]


# Method 2 
def topKFrequent_2(k, keywords, reviews):
        word_list = []
        for review in reviews:
            word_list += set(review.lower().replace('[^a-z0-9]', '').split())
        count = Counter(word_list)
        def f(keyword):
            return (-count[keyword],keyword)

        return sorted(keywords, key=f)[:k]

if __name__ == '__main__':
    print(topKFrequent(k, keywords, reviews))
    print(topKFrequent_2(k, keywords, reviews))
    