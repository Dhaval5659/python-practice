with open("myfile.txt", "w") as f:
  f.write("This is new content! for me")
  f.write("This is new content for me and 2rd line")

with open("myfile.txt") as f:
  print(f.read(5))


