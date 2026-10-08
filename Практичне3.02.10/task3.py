def check_baggage(*weights):
    total=0
    for w in weights:
        total=total+w
    return total <= 50
