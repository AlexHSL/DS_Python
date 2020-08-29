message = "hello world!"

print(message.title())
print(message.upper())

message="A"+message
print(message.lower())

message = "  " + message + " "
print(message.strip()+"end")
print(message.lstrip()+"end")
print(message.rstrip()+"end")
print(message+"end")

test_string = "test\n\t"
print(test_string+"end")
print(test_string.strip()+"end")

