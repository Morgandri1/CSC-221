# create a var w/ input of name
# create another string var
# print message to user using both vars
welcome_message = "Hello, <>. How are you doing today?"
name = input("What is your name?\n") # add a newline to make it chat-esque
print(welcome_message.replace("<>", name))