#Import sys propuesto por Copilot
import sys
read = sys.stdin.readline

n, m = map(int, read().split())
pairs = []
maxB = 0
current_matches = 0
remaining_boxes = n

for i in range(m):
    pair = tuple(map(int, read().split()))
    pairs.append(pair)

pairs = [(matches, boxes) for boxes, matches in pairs]
pairs.sort(reverse=True)

for matches, boxes in pairs:
    if remaining_boxes > 0:
        if boxes < remaining_boxes:
            remaining_boxes -= boxes
            current_matches += boxes*matches
        else:
            take = remaining_boxes
            current_matches += take * matches
            remaining_boxes -= take

print(current_matches)