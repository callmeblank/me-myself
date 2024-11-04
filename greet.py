from sys import argv

if len(argv) != 2:
  print("hello, world")
else:
  print(f"hello, {argv[1]}")
