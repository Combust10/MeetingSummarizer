with open('Transcripts/transcript.txt', 'r+') as f:
    lines = f.readlines()
    print(lines)
    if(lines[0] == '0'):
        f.truncate(0)
        f.seek(0)
        f.write('1')
    else:
        f.truncate(0)
        f.seek(0)
        f.write('0')
