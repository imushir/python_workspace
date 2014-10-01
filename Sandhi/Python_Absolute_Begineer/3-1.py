Name = ""
Desc = ""
Gender = ""
Race = ""
Name = raw_input("What is your Name?")
Desc = raw_input('Describe yourself')
Gender = raw_input('what Gender are you?(male/female/unsure) :')
Race = raw_input('What fantasy Race are you ? = (A/B/C):')

#output the character sheet
fancy_line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
print("\n",fancy_line)
print("\t",Name)
print("\t",Race,Gender)
print("\t",Desc)
print(fancy_line,"\n")