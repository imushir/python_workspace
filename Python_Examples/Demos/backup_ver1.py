import os
import time

# 1.The files and directories to be backed up are specified in  source
source = ['/home/mushirahmed/Backup_python_Demo/Source_1','/home/mushirahmed/Backup_python_Demo/Source_2']

#2.The backup must be strored in main backup directory

target_dir = '/home/mushirahmed/Backup_python_Demo/Desti'

#3. The files are backed up into z zip file.
#4. The name of the zip archive is the current date and time

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

#5. We use the zip command(in Unix/Linux) to put files in zip archieve

zip_command = "zip -qr '%s' %s " % (target,''.join(source))

#Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to ',target
else:
    print 'Backup Failed'