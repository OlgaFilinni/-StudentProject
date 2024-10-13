file_zen_text = open("zen.txt")
list_zen_text = [line.strip() for line in file_zen_text]
file_zen_text.close()
list_zen_text.reverse()
list_rev = "\n".join(list_zen_text)
print(list_rev)
