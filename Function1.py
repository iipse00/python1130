def setValue(newValue):
    x = newValue
    print("함수내부:",x)


result = setValue(5)
print(result)


def swap(x,y):
    return y,x

result = swap(5,6)
print(result)
print(result[0],result[1])


def union(prelist,postlist):
    # 교집합 문자를 저장하기 위한 지역 변수
    result = []

    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result


print(union("HAM","SPAM"))