f = open("test.txt", 'a+')
# dino = f.read()
# print(dino)
# while True:
#     dino = f.read()
#     print(dino)
#     if not dino:
#         break
for i in range(3):
    f.write("\nnew line" + str(i))
f.close()
