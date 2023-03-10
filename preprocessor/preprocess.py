import os
for file in os.listdir("working"):
  if file.endswith(".html"):
    in_file = open("working/" + file, "r")
    in_text = in_file.read()
    in_file.close()

    lines = in_text.splitlines()
    for i in range(len(lines)):
      words = lines[i].split()
      if len(words) > 0 and words[0].startswith("$"):
        replace = ""
        for j in range(1, len(words)):
          replace += words[j] + " "
        replace_file = open("preprocessor/" + words[0][1:] + ".txt", "r")
        replace_text = replace_file.read()
        replace_file.close()
        replace_text = replace_text.replace("$", replace)
        lines[i] = replace_text

    out_text = ""
    for line in lines:
      out_text += line + "\n"

    out_file = open(file, "w")
    out_file.write(out_text)
    out_file.close()
