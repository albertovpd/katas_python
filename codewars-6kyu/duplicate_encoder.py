# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# def duplicate_encode(word):
#     #your code here
#     result=""
#     word= word.lower()
#     for w in word:
#         if word.count(w)>1:
#             result+=")"
#         else:
#             result+="("
    
#     return result
       
def duplicate_encode(word):
    #your code here
    word = word.lower()
    return "".join(")" if word.count(w)>1 else "(" for w in word)