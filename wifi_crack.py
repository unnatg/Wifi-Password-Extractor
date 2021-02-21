import subprocess

command = 'netsh wlan show profiles'
p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     universal_newlines=True)
result = p.communicate()[0]
with open('wifi_profile.txt', 'w') as file:
    file.write(result)
file.close()

with open("wifi_profile.txt", "r") as f:
    lines = f.readlines()
with open("wifi_profile.txt", "w") as f:
    for line in lines:
        if "All" in line:
            f.write(line)
    f.truncate()
f.close()

with open("wifi_profile.txt", "r") as f:
    lines = f.readlines()
with open("wifi_profiles_only.txt", "w+") as file_:
    for line in lines:
        line.rstrip()
        file_.write(line)
file_.close()
ls = []
with open("wifi_profiles_only.txt", "r") as file_:
    for line in file_:
        
        (key, val) = line.split(":")
        ls.append(val)
file_.close()
ls1 = []
for val in ls:
    if(val==" "):
        continue
    else:
        ls1.append(val)
for val in ls1:
    val=val.strip()   
    #print(val)
    command1 = 'netsh wlan show profiles '
    command2 = '"{}" key=clear'.format(val)
    command=command1+command2
    #print(command)
    p = subprocess.Popen(command,
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
    result = p.communicate()[0]
    with open("wifi_password.txt", "a") as file1:
        file1.write(result)

    
