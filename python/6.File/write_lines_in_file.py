
fw=open("z.txt","w")

str1=["rno "," name "," percentage"]
fw.writelines(str1)


str2=str(["15","pradeep","90.11"])
fw.writelines(str2)

fw.close()