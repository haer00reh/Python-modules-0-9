import sys

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
else:
    i = 0
    scores = sys.argv[1:]
    while i < len(scores):
        try:
            scores[i] = int(scores[i])
        except ValueError:
            print(f"You typed '{scores[i]}', only decimal scores are allowed ('{scores[i]}' won't be assigned)")
            scores.pop(i)
            continue
        i +=1
    if len(scores) == 0:
        print("No scores were assigned, quitting...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
