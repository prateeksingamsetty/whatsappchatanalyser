f=open("harshith.txt","rt")
#cnt=0
#lines = f.readlines()
data = f.read()

#l=[+91 87906 64705,Prateek Singamsetty,+91 95537 92214,+91 93948 #78753,+91 99899 10731,+91 90300 33025,Nithya,Nikki,Vinta,Hari #Priya,Karthik,Satya Raj]



print("messages by " + i + " ",data.count("- " + i + ":"))
print("messages by roshan",data.count("- +91 87906 64705:"))
print("messages by prateek",data.count("- Prateek Singamsetty:"))
print("messages by harshit",data.count("- +91 95537 92214:"))
print("messages by pavan",data.count("- +91 93948 78753:"))
print("messages by yashwanth",data.count("- +91 99899 10731:"))
print("messages by harsha",data.count("- +91 90300 33025:"))
print("messages by nithya",data.count("- Nithya:"))
print("messages by nikki",data.count("- Nikki:"))
print("messages by vinta",data.count("- Vinta:"))
print("messages by hari priya",data.count("- Hari Priya:"))
print("messages by karthik",data.count("- Karthik:"))
print("messages by satya raj",data.count("- Satya Raj:"))

#print(lines)
