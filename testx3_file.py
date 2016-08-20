#ver 0.1
import os
import time

source=[r'E:\pythonTest\demo\test2',r'E:\pythonTest\demo\test2']

target_dir='/mnt/e/backup/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr'%s'%s"%(target,''.join(source))

if os.system(zip_command)==0:
    print 'Successful backup',target
else:
    print 'Backup FAILED'
    
