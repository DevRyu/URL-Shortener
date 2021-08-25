from models import Link

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_latest_short_id():
    latest_short_id = Link.get_recent_one()
    return latest_short_id


def get_next_id(id):
    curr_id = decode_62(id)
    print(curr_id)
    next_id = encode_62(curr_id + 1)
    return next_id


def encode_62(num, alphabet=BASE62):
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    result = "".join(arr)
    if len(result) != 5:
        for _ in range(5 - len(result)):
            result = "0" + result

    return result


def decode_62(string, alphabet=BASE62):
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
    for char in string:
        power = strlen - (idx + 1)
        num += alphabet.index(char) * (base ** power)
        idx += 1
    return num


def get_unique_short_id():
    recent_id = get_latest_short_id()
    if recent_id == None:
        next_id = get_next_id("00000")
    else:
        next_id = get_next_id(recent_id.shortId)
    return next_id
