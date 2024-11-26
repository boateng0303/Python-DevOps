import csv

# f = open('filename', 'w') # "w" 'r', 'a' # t or b

# f.close()


# Preference 

# with open('text.txt', 'r') as f:
#     #f.write("\nhello Richard\n")
#     content=f.read()      #realines reads everything as a list
#     print(content)


with open('jenkins.csv','w', newline='') as j:
    pen = csv.writer(j, delimiter=",")
    pen.writerow(["USER_NAME", "CELL_PHONE", "INSTANCE_TYPE", "REGION"]) 
    pen.writerow(['kserge', '555 555 555', 't2.xlarge', 'us-east-1'])



