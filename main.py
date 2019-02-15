from os import system as s

c='\033[1;36m'
r='\033[1;31m'
g='\033[1;32m'
w='\033[1;37m'
s('clear')
print("""%s
			 MENU-MAIN SPAM%s
 ,_     _‚
 |\\\___//|	%sAuthor: KANG-NEWBIE%s
 |=6   6=|	%sContact: https://t.me/kang_nuubi%s
 \=._Y_.=/	%sGithub: https://github.com/KANG-NEWBIE%s
  )  `  (    ,	%sTEAM: CRABS (t.me/CRABS_ID)%s
 /       \  ((
 |       |   ))
/| |   | |\_//
\| |._.| |/-`
 '"'   '"'
"""%(c,r,g,r,g,r,g,r,g,r))
print("""%s1. Spam Mail BPJS
2. Spam Mail Surveyon"""%(g))
pilih=input("%s[!] Masukan Pilihan =>%s "%(c,w))
if pilih == '1':
	s('python mail.py')
elif pilih == '2':
	s('python spamemail.py')
else:
	exit("%s[!]WRONG INPUT\n"%(r))
