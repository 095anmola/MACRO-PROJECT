#opening all files
file1=open("condition.txt","r")
file2=open("nametab.txt","w")
file4=open("argtab.txt","w")
file5=open("output.txt","w")

#making nametab
f1=file1.read()
s1=f1.split("\n")                 #splitting into lines
l1=len(s1)                        #no. of lines
for i in range(0,l1):
    if "MACRO" in s1[i]:          #printing name into nametab
        p1=s1[i].split(" ")
        file2.write(p1[0])

    if s1[i]=="source:":                #printing into output file
        file5.write(s1[i]+"\n")
        for j in range(i+1,l1):
            if p1[0] in s1[j]:
                p3=s1[j].split("(")
                file5.write(p3[0]+"\n")
                p4=list(p3[1])
                file4.write(p4[0]+"\n")
                file4.write(p4[2])
                if(p4[0]==p4[2]):
                    p5=s1[2].split("(")
                    file5.write(p5[1])
                else:
                    p5=s1[4].split("(")
                    file5.write(p5[1])


