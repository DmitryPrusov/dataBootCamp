def is_correct(string,  i=0, count=0):
    if i == len(string): return count == 0
    if count < 0: return False
    if string[i] == "(" or string[i] == "{" or string[i] == "[" :
        return  is_correct(string, i + 1, count + 1)

    if string[i] == ")" or string[i] == "]" or string[i] == "}":
        return  is_correct(string, i + 1, count - 1)

for s in ["{)", "{()", "(())", "()()", ")("]:
    print ("{}: {}".format(s, is_correct(s)))
