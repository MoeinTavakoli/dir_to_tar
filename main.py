import sys
import os
from compress import dir_to_tar , time_generator

if __name__ == '__main__':

    if len(sys.argv) > 1 : 
      local_path_dir = sys.argv[1]
      if os.path.exists(local_path_dir):          
         print(f'local_path_dir = {local_path_dir}')
         dir_to_tar(local_path_dir, f'{time_generator()}.tar.gz')
         print(f'backup succesfuly as {time_generator()}.tar.gz file ...')
      else:
         raise Exception("No such file or directory !")
    else:
     raise Exception("argument is not define ! ")