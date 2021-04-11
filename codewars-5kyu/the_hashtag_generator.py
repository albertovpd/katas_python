# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

# def generate_hashtag(s):
#     result="#"
#     if s=="" or len(s)>140:
#         return False
#     else:
#         for s in s.split(" "):
#             result+=s.title()
            
#         return result

def generate_hashtag(s):
    if s=="" or len(s)>140:
        return False
    else:
        return '#'+ str(s.title().replace(' ',''))