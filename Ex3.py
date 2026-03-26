from collections import defaultdict

file = open("sample_data/scores.txt")

name_scores: dict[str, list[int]] = defaultdict(list[int])

for line in file:
    try:
        (name, score) = line.split(",")
        name_scores[name].append(int(score))
    except TypeError:
        print(f"invalid syntax: {line}")
        pass


for name, scores in name_scores.items():
    print(f"Name: {name}    Avg. score: {sum(scores) / len(scores):.2f}")
