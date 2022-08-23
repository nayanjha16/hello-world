import os
dir_path_for_lexicon="/home/nayan/mfa_setup/lexicon"
lexicon_file_name="lexicon.txt"
updated_lexicon="updated_lexicon.txt"

with open(os.path.join(dir_path_for_lexicon,lexicon_file_name)) as f:
    lines = f.readlines()
updated_lex=[]
for line in lines:
    str_val=line.split(" ", 1)
    temp =str_val[0]+"\t"+str_val[1]
    print(temp)
    updated_lex.append(temp)
    
#create a empty file with the name "updated_lexicon.txt"
with open(os.path.join(dir_path_for_lexicon, updated_lexicon), 'w') as fp:
    pass
fp.close()


#opening the "updated_lexicon.txt" file and writing the new tab separated lexicon in it 
with open(os.path.join(dir_path_for_lexicon, updated_lexicon), 'w') as fp:
    for line in updated_lex:
        fp.write('%s\n' % line)
fp.close()
