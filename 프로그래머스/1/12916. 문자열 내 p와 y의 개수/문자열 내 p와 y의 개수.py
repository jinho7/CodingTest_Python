def solution(s):
    return s.lower().count("p") == s.lower().count("y")

print(solution("pPoooyY"))
print(solution("Pyy"))