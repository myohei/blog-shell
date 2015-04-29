import sys
import os
from bs4 import BeautifulSoup

__author__ = 'yohei'


file_dir = '/Users/yohei/Google Drive/blog_post/'

argvs = sys.argv
if (len(argvs) != 2):
    print('error')
    exit(2)

file_name = argvs[1]
extensions = file_name.split('.')[1]
file_name= file_dir + file_name
print('read file: ' + file_name)
f = open(file_name, mode='r+', encoding="UTF-8")
html = f.read()
if (extensions == "md"):
    html = markdown2.markdown(html)

html = html.replace('<pre><code>', '<pre class="prettyprint">').replace('</code></pre>', '</pre>')

soup = BeautifulSoup(html)

# add target attr to a tags.
atags = soup.find_all('a')
for a in atags:
    a['target'] = '_blank'

# write to file
outFileName = file_name.split('.')[0]
outFileName += '_rewrite.html'
print('make file ' + outFileName)
outFile = open(outFileName, 'w', encoding='UTF-8')
outFile.write(str(soup.html))
outFile.flush()
outFile.close()

# delete source file
if (extensions != "md"):
    os.remove(file_name)
    print('delete file: ' + file_name)

os.system("open -a /Applications/Sublime\ Text.app " + outFileName)
