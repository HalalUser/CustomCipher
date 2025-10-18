def TtN(text):
    result = []
    for i in text:
        if i.isalpha():
            answer = ord(i) - ord("a") + 1
            result.append(str(answer))
            result.append(" ")
        else:
            result.append("")
    return "".join(result)

        
userinput = input()
TextToNumber = TtN(userinput.lower())


def counter(text):
    result = []
    numbers = text.split(" ")
    for i in range(len(numbers)):
        answer = str(i + 1)
        result.append(answer)
    return result 

userinput = TextToNumber
b = list(map(int, userinput.split()))
a = list(map(int, counter(userinput))) 

result = [(x + y) % 26 or 26 for x, y in zip(a, b)]
z = " ".join(map(str, result))  


def numbertotext(text):
    result = []
    for i in text.split():
        if i.isdigit():
            n = int(i) 
            result.append(chr(ord("a") + n - 1))
        else:
            result.append("?")
    return "".join(result)

ans = numbertotext(z)
print(ans)