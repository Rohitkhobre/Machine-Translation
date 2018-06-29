import string

eng_file = open("spanish2.txt", "r")
eng_lines = eng_file.readlines()
mod_lines = ['']

#sp_file = open("spanish2.txt", "r")
#sp_lines = sp_file.readlines();

for row in range(0,len(eng_lines)):
	line = eng_lines[row]
	out = line.translate(string.maketrans("",""), string.punctuation)
	mod_lines.append(out)

new_file = open("spanish1.txt", "w")
new_file.writelines(mod_lines)
new_file.close

