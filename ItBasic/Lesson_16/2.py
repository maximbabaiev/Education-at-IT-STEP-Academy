users = [['user1', '111'],
         ['user2', '2222'],
         ['user3', '33333'],
         ['user1', '111'],
         ['user2', '2222'],
         ['user3', '33333']
         ]

def lst(*us):
    for i in range(len(us)):
        if i < len(us):
            print("login: {}".format(us[i][0]))

            print("password: {}".format(us[i][1]))



lst(*users)
# for j in users:
#     lst(j)
