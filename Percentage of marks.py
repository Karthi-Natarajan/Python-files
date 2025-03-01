# To Calculate Total Percentage
marks=[]
i=0
while i < 5:
    marks.append(int(input(f"enter the num {i+1} :")))
    i+=1
total = 0
for mark in marks:
    total+=mark
percentage = total / 5
print(f"Percentage : {percentage :.2f}%")
