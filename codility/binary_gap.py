# N integer, get the binary gap
def solution(N):
    grouped_0s=format(N,'b').strip('0').split("1")
    return len(max(grouped_0s))
