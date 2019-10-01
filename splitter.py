import re


f = open('demo.srt', 'r')
content = f.read()

regex = re.compile(r'<.*?>')
content = regex.sub('', content)

regex = re.compile(r'\xef\xbb\xbf')
content = regex.sub('\r\n', content)

parts = content.split('\r\n\r')


for sub in parts:
    regex = re.compile(r'\r')
    sub = regex.sub('', sub)

    parts = sub.split('\n')
    
    duration = parts[2].split(' --> ')
    text=' '.join(parts[3:])
    print (duration, text)

f.close()
