al = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
al = al.split(" ")


def get_index(ch):
    for i in range(len(al)):
        if ch == al[i]:
            return i


def get_cj(ch):
    return al[(get_index(ch) + 5) % 26]


def get_cifar(st):
    st = [get_cj(i) for i in st]
    return ''.join(st)


def get_counted_letter(wo):
    data = {}
    for ch in wo:
        if ch in data.keys():
            data[ch] += 1
        else:
            data[ch] = 1
    return data


def check_cifar(wr, ci):
    cdata = get_counted_letter(get_cifar(wr))
    gcdata = get_counted_letter(ci)
    cdata_keys = cdata.keys()
    gcdata_keys = gcdata.keys()
    for i in cdata_keys:
        if i not in gcdata_keys:
            return False
        if cdata[i] != gcdata[i]:
            return False
    return True


wr = input()
ci = input()
if (check_cifar(wr, ci)):
    print("Yes", end="")
else:
    print("No", end="")
