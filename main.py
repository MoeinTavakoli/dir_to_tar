import os
import argparse
from compress import dir_to_tar , time_generator

if __name__ == '__main__':
       
    parser = argparse.ArgumentParser(description='Backup directory to a tar.gz file.')
    parser.add_argument('-d', '--directory', required=True, help='Directory to be backed up')
    args = parser.parse_args()

    local_path_dir = args.directory
    if os.path.exists(local_path_dir):
        print(f'local_path_dir = {local_path_dir}')
        date_now = time_generator()
        dir_to_tar(local_path_dir, f'{date_now}.tar.gz')
        print(f'backup successfully as {date_now}.tar.gz file ...')
    else:
        raise Exception("No such file or directory!")
