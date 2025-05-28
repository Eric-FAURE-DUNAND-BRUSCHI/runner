def save(score: int):
    try:
        with open("save.txt", "r") as f:
            best = f.read()
            try:
                int(best)
            except ValueError:
                best = "0"
            b_score = int(best)
    except FileNotFoundError:
        b_score = 0
    if b_score > score:
        return b_score
    with open("save.txt", "w") as f:
        f.write(f'{score}')
    return score