#
# You are given a stream of logging statements for a server as a list.
# Your product manager wants to know what categories of error are the most
# common, as well as what errors in the most common categories are the most
# common.
#
# Here are a few log lines, each is a string structured similarly to this:
# [
# '[WARNING] 403 Forbidden: No token in request parameters',
# '[ERROR] 500 Server Error: int is not subscriptable',
# '[INFO] 200 Login Successful',
# '[INFO] 200 User sent a message',
# '[ERROR] 500 Server Error: int is not subscriptable'
# ]
#
# Return a dictionary with logging statistics, that is
# formatted like so
# ( don't worry about spacing or formatting, only the data matters )
#  {'WARNING': {'403': {'Forbidden': {'No token in request parameters': 1}}},
#  'ERROR': {'500': {'Server Error': {'int is not subscriptable': 2}}},
#  'INFO': {'200': {'OK': {'Login Successful': 1, 'User sent a message': 1}}}}

test_data = [
'[WARNING] 403 Forbidden: No token in request parameters',
'[ERROR] 500 Server Error: int is not subscriptable',
'[INFO] 200 OK: Login Successful',
'[INFO] 200 OK: User sent a message',
'[ERROR] 500 Server Error: int is not subscriptable'
]


def log_stats(logs):
    errors = {}
    # error_num = {}
    # error_type = {}
    # error_message = {}
    for string in logs:
        message = string.split(":")[-1:][0] #split with : as a delimiter to keep message intact :)
        lines = string.split(":")[0].replace("[", "").replace("]", "")
        tokens = lines.split()
        tokens.append(message)
        if tokens[2] == "Server":
            tokens.insert(2, tokens[2] +" "+ tokens[3])
            tokens.pop(3)
            tokens.pop(3)
        if tokens[0] in errors:
            print(tokens[3].count(message), "message count")
            errors[tokens[0]][tokens[1]][tokens[3]] = {tokens[3].count(message)}
        else :
            errors[tokens[0]]= {tokens[1] :{tokens[2] :{tokens[3] :count}}}
        print(errors)
# people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
#           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
#
# print(people)
    print(errors, "FINALLL")
print(log_stats(test_data))
