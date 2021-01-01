from sys import exit
from argparse import ArgumentParser
from spec import settings, configurations
from handler.filehandler import FilePreprocess
from helper.functions import DataStoreCRD


# Arguemts

parser = ArgumentParser()
parser.add_argument('--datastore', help='Enter absolute path.')
args = parser.parse_args()

# Selecting the DataStore Directory.
# Select user provided datastore path else, select the default path.
if args.datastore:
    db_path = args.datastore
else:
    db_path = configurations.DEFAULT_DB_PATH

# DATABASE creation

directory_created = FilePreprocess(db_path).create_folder()
if not directory_created:
    print(f"Permission denied: You can not create the directory `{db_path}`.\n")
    exit(0)


key = 'Car'


################################
'''DELETE DATA FROM DATASTORE'''
_data_found, message = DataStoreCRD().check_delete_data(key, db_path)
print(message)
################################
