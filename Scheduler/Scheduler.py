import os
import datetime
from zipfile import ZipFile

BACKUP_DIR_NAME = "WingspanBirdsBackup"
DAYS_TO_KEEP_BACKUP = 4
FILE_PREFIX = "WB_Backup"
FILE_SUFFIX_DATE_FORMAT = "%Y%m%d%H%M%S"
USERNAME = "username"
DBNAME = USERNAME+"$dbname"

# get today's date and time
timestamp = datetime.datetime.now().strftime(FILE_SUFFIX_DATE_FORMAT)
backup_filename = BACKUP_DIR_NAME+"/"+FILE_PREFIX+timestamp+".sql"

os.system("mysqldump -u "+USERNAME+" -h "+USERNAME+".mysql.pythonanywhere-services.com '"+DBNAME+"'  > "+backup_filename)

# creating zip file
zip_filename = BACKUP_DIR_NAME+"/"+FILE_PREFIX+timestamp+".zip"
with ZipFile(zip_filename, 'w') as zip:
    zip.write(backup_filename, os.path.basename(backup_filename))


os.remove(backup_filename)

# deleting old files

list_files = os.listdir(BACKUP_DIR_NAME)

back_date = datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_BACKUP)
back_date = back_date.strftime(FILE_SUFFIX_DATE_FORMAT)

length = len(FILE_PREFIX)

# deleting files older than DAYS_TO_KEEP_BACKUP days
for f in list_files:
    filename = f.split(".")[0]
    if "zip" == f.split(".")[1]:
        suffix = filename[length:]
        if suffix < back_date:
            print("Deleting file : "+f)
            os.remove(BACKUP_DIR_NAME + "/" + f)



# restoring backup - run this command in the home directory
# mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  < db-backup.sql