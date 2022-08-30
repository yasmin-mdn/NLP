import re
file = open("MyFile.txt","r")
answerfile = open("MyAnswers.txt","w")
lines=file.readlines()
regex1="((Doctor|Dr\.)( [A-Z][a-z\.]+)+)"
regex2="(([A-Z][a-z\.]+ )+M\.D\.)"
regex3="(([A-Za-z\.]+[ ]{0,1})+,[ ]{1}M\.D\.)"
for i in range(0, len(lines)):
    x =re.match(regex1, lines[i])
    y=re.match(regex2, lines[i])
    z=re.match(regex3, lines[i])
    tmp = x or y or z
    if tmp :
        answerfile.write("YES\n") 
    else:
        answerfile.write("NO\n")
       