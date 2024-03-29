import os

def ireplace(old, new, text):
  idx = 0
  while idx < len(text):
    index_l = text.lower().find(old.lower(), idx)
    if index_l == -1:
      return text
    if text[index_l - 1] != "\"" and text[index_l - 1] != "/" and text[index_l - 1] != "@" and not text[index_l - 1].isalnum():
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
        for i in range(1, len(linkword)):
          if linkword[i].isupper() and linkword[i - 1] != " ":
            l = list(linkword)
            l[i] = linkword[i].lower()
            linkword = "".join(l)
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
        replace = ">" + replace.strip() + "<"
        replace_file = open("preprocessor/" + words[0][1:] + ".txt", "r")
        replace_text = replace_file.read()
        replace_file.close()
        replace_text = replace_text.replace(">$<", replace)
        lines[i] = replace_text

    text = ""
    for line in lines:
      text += line + "\n"

    # add twitter links
    i = 0
    twitter_link_dict = { }
    while i < len(text):
      if text[i] == "@":
        j = i + 1
        while text[j].isalnum() or text[j] == "_":
          j += 1
        twitter_handle = text[i:j]
        twitter_link = "<a href=\"https://twitter.com/" + twitter_handle[1:] + "\">" + twitter_handle + "</a>"
        twitter_link_dict[twitter_handle] = twitter_link
      i += 1

    for key in twitter_link_dict:
      text = text.replace(key, twitter_link_dict[key])

    out_file = open(file, "w")
    out_file.write(text)
    out_file.close()
