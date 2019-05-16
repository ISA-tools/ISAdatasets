#!/usr/bin/env python3
import ftplib
from isatools.net import mtbls
import os

EBI_FTP_SERVER = 'ftp.ebi.ac.uk'
MTBLS_BASE_DIR = '/pub/databases/metabolights/studies/public'
ftp = ftplib.FTP(EBI_FTP_SERVER)
response = ftp.login()
if '230' in response:
    print('Login successful')
    ftp.cwd(MTBLS_BASE_DIR)
    nlist = ftp.nlst()
    mtbls_list = [x for x in nlist if 'MTBLS' in x]
    for mtbls_study in mtbls_list:
        print('Getting ' + mtbls_study)
        os.mkdir(os.getcwd() + '/' + mtbls_study + '/')
        mtbls.get(mtbls_study, mtbls_study)
else:
    print('Could not login to ftp server')
