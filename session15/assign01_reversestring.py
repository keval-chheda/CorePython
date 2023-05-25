# #reverse a string
# #zaid = length:4
# def string_reverse(str1):
#
#     reverse_str1 = ""
#     index = len(str1)
#     while index > 0:
#         reverse_str1 += str1[index - 1]
#         index = index - 1
#     return reverse_str1
# print(string_reverse("1234rs"))

def reverse_strings(strings):
    result = list(map(lambda x: "".join(reversed(x)), strings))
    return result

strings = ["abc","sjkh","dlk","fjk","hlk"]
print("\nReverse strings of the said given list:", reverse_strings(strings))



