import os
for file in os.listdir("working"):
  if file.endswith(".html"):
    in_file = open("working/" + file, "r")
    text = in_file.read()
    in_file.close()

    # Preprocess here

    out_file = open(file, "w")
    out_file.write(text)
    out_file.close()
