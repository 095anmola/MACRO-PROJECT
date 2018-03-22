#opening all files
file1=open("main.txt","r")
file2=open("nametab.txt","w")
file3=open("deftab.txt","w")
file4=open("argtab.txt","w")
file5=open("output.txt","w")

#making nametab
f1=file1.read()
s1=f1.split("\n")                 #splitting into lines
l1=len(s1)                        #no. of lines
for i in range(0,l1):
    if "//" in s1[i]:
        continue
    
 

    else:
        if "MACRO" in s1[i]:
            p1=s1[i].split(" ")
            file2.write(p1[0]+"\n")
            if("Hello" in p1[0]):
                file3.write(p1[0]+"\n")                   #printing 1st line in deftab
            if("&" in p1[2]):
                file3.write(" "+p1[2]+"\n")

        if s1[i]=="Source:":                  #argtab
            for j in range(i+1,l1):
                if "Hello" in s1[j]:
                    p3=s1[j].split(" ")
                    p4=p3[1].split(",")
                    l2=len(p4)
                    for k in range(0,l2):
                        file4.write(p4[k]+"\n")

        if "#" in s1[i]:
            p5=s1[i].split(" ")
            l3=len(p5)
            for j in range(2,l3):
                file5.write(p5[j]+" ")
            file5.write("\n ")

for i in range(5,l1):
    if "//" in s1[i]:
        continue
    flag=0
    if "<<" in s1[i]:
        for m in range(i+1,l1):
            if ">>" not in s1[m]:
                continue

            else:
                i=m+1
                flag=1
                break
    if flag==1:
        continue


    else:                                    #value of i is not equals 5 which it should be
        if("MEND" in s1[i]):
            break
        if "&" in s1[i]:
            p2=s1[i].split(" ")
            file3.write(p2[0]+" ")               #printing before &
            a1=list(p2[1])                       #splitting after &
            file3.write(a1[2]+"\n");
        elif("MACRO"  in s1[i]):
            s2=s1[i].split(" ")
            file3.write(s2[0])                   #for other lines than &
        else:
            file3.write("\n"+s1[i])
#output file:
for i in range(0,l1):
    if "//" in s1[i]:
        continue
    flag=0
    if "<<" in s1[i]:
        for m in range(i+1,l1):
            if ">>" not in s1[m]:
                continue

            else:
                i=m+1
                flag=1
                break
        if flag==1:
            continue

    else:
        if s1[i]=="Source:":
            file5.write(s1[i]+"\n")
            for j in range(i+1,l1):
                if "Hello" in s1[j]:
                    file5.write(s1[j]+"\n")
                    for k in range(5,l1):
                        if "//" in s1[k]:
                            continue
                        flag=0
                        if "<<" in s1[i]:
                            for m in range(i+1,l1):
                                if ">>" not in s1[m]:
                                    continue

                                else:
                                    i=m+1
                                    flag=1
                                    break
                            if flag==1:
                                continue

                        if("MEND" in s1[k]):
                            break
                        if "&" in s1[k]:
                            p2=s1[k].split(" ")
                            file5.write(p2[0]+" ")
                            a1=list(p2[1])
                            file5.write(a1[2]+"\n");
                        elif("MACRO"  in s1[k]):
                            s2=s1[k].split(" ")
                            file5.write(s2[0])                   #for other lines than &
                        else:
                            file5.write("\n"+s1[k])



