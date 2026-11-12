import heapq

text = input("Enter text: ")
if text == "":
    print("Nothing to encode")
    exit()

freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# each heap item: (frequency, tie-breaker, {character: code so far})
heap = []
count = 0
for ch in freq:
    heap.append((freq[ch], count, {ch: ""}))
    count += 1
heapq.heapify(heap)

while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)
    merged = {}
    for ch in left:
        merged[ch] = "0" + left[ch]
    for ch in right:
        merged[ch] = "1" + right[ch]
    heapq.heappush(heap, (f1 + f2, count, merged))
    count += 1

codes = heap[0][2]
for ch in codes:
    if codes[ch] == "":
        codes[ch] = "0"

print("\nCharacter  Frequency  Code")
for ch in codes:
    print(f"{ch!r:9}  {freq[ch]:9}  {codes[ch]}")

encoded = ""
for ch in text:
    encoded += codes[ch]

print("\nEncoded text:", encoded)
print("Original size:", len(text) * 8, "bits")
print("Encoded size :", len(encoded), "bits")
