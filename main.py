for i in range(5):
  string = ' ' * i + '^' + ' ' * (8 - i * 2) + '^'
  print(string)

for i in range(4, -1, -1):
  string = ' ' * i + '^' + ' ' * (8 - i * 2) + '^'
  print(string)

# ^        ^
#  ^      ^
#   ^    ^
#    ^  ^
#     ^^
#     ^^
#    ^  ^
#   ^    ^
#  ^      ^
# ^        ^
