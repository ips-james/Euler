# a = 97
# z = 122

input_list = []
with open("c:/users/James\Documents/Personal/Data Analysis/Python/p059_cipher.txt") as input_file:
    for line in input_file:
        input_list.append(line.strip().split(','))

result1 = 32
# check for space char

# max_hits = 0
# for key1 in range (97,123):
#     for key2 in range(97,123):
#         for key3 in range(97,123):
#             hits = 0
#
#             for char in range(0, len(input_list[0]) - 3,3):
#                 a = int(input_list[0][char])
#                 b = int(input_list[0][char + 1])
#                 c = int(input_list[0][char + 2])
#                 if a^key1 == result1 or b^key2 == result1 or c^key3 == result1:
#                     hits = hits +1
#             if hits > max_hits:
#                 max_hits = hits
#                 print (chr(key1), chr(key2), chr(key3), hits)

#decrypting
message = []
final_key = "god"
sum = 0
for char in range (0, len(input_list[0]) -2,3):
    sum = sum + (int(input_list[0][char])^ ord(final_key[0]))
    sum = sum + (int(input_list[0][char +1]) ^ ord(final_key[1]))
    sum = sum + (int(input_list[0][char +2]) ^ ord(final_key[2]))
    message.append(chr(int(input_list[0][char])^ord(final_key[0])))
    message.append(chr(int(input_list[0][char + 1]) ^ ord(final_key[1])))
    message.append(chr(int(input_list[0][char + 2]) ^ ord(final_key[2])))

## Todo: iterate the 3 key characters so that the final character is picked up.

print (len(input_list[0]))
print(len(message))
print (sum)