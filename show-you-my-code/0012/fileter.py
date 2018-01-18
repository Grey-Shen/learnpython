def filterwords(x):
    with open(x,'r') as f:
        text=f.read()
    print(text.split('\n'))
    userinput=raw_input('myinput:')
    for i in text.split('\n'):
        if i in userinput:
            replace_str='*'*len(i.decode('utf-8'))
            word=userinput.replace(i,replace_str)
            return word

print(filterwords('filtered_words.txt'))
