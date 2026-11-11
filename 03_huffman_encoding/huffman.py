import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def get_codes(node, code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = code or "0"
        return
    get_codes(node.left, code + "0", codes)
    get_codes(node.right, code + "1", codes)


text = input("Enter text: ")

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

heap = [Node(ch, f) for ch, f in freq.items()]
heapq.heapify(heap)

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    parent = Node(None, a.freq + b.freq)
    parent.left = a
    parent.right = b
    heapq.heappush(heap, parent)

codes = {}
get_codes(heap[0], "", codes)

print("Character codes:")
for ch, code in codes.items():
    print(repr(ch), ":", code)

print("Encoded text:", "".join(codes[ch] for ch in text))
