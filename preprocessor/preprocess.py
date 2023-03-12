import os

def ireplace(old, new, text):
    idx = 0
    while idx < len(text):
        index_l = text.lower().find(old.lower(), idx)
        if index_l == -1:
            return text
        text = text[:index_l] + new + text[index_l + len(old):]
        idx = index_l + len(new) 
    return text

for file in os.listdir("working"):
  if file.endswith(".html"):
    in_file = open("working/" + file, "r")
    text = in_file.read()
    in_file.close()
    
    ## add links
    for linkname in os.listdir("working"):
      if linkname.endswith(".html") and linkname != file:
        linkword = linkname
        linkword = linkword.replace(".html", "")
        linkword = linkword.replace("_", " ")
        linkword = linkword.title()
        linktext = "<a href=\"" + linkname + "\">" + linkword + "</a>"
        text = ireplace(linkword, linktext, text)

    # add macro text
    lines = text.splitlines()
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

    text = ""
    for line in lines:
      text += line + "\n"

    # add twitter links
    i = 0
    while i < len(text):
      if text[i] == "@":
        i += 1
        j = i
        while text[j].isalnum() or text[j] == "_":
          j += 1
        twitter_handle = text[i:j]
        twitter_handle_with_at = text[(i - 1):j]
        twitter_link = "<a href=\"https://twitter.com/" + twitter_handle + "\">" + twitter_handle_with_at + "</a>"
        text = text.replace(twitter_handle_with_at, twitter_link)
        i += len(twitter_link) * 2
      i += 1

    out_file = open(file, "w")
    out_file.write(text)
    out_file.close()
