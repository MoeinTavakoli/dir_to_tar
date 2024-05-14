from datetime import datetime
import os
import tarfile
from progress.bar import ChargingBar # type: ignore


def dir_to_tar(path, name):
    try:
# Start to count to the dir 
        file_count = 0
        for root, dirs, files in os.walk(path):
            file_count += len(files)
####

# Init the progress bar
        bar = ChargingBar('Processing', max=file_count)

# Create the tar.gz file
        with tarfile.open(name, "w:gz") as tarhandle:
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        file_path = os.path.join(root, file)
                        tarhandle.add(file_path)
                        bar.next()  
                    except Exception as e:
                        print(f"Error adding file {file_path}: {e}")
        bar.finish()  # Finish the progress bar 
        
    except Exception as e:
        print(f"Failed to create tar file: {e}")

def time_generator():
    now = datetime.now()
    # Format the date and time string
    date_time = now.strftime("%Y-%m-%d_%H-%M")
    return date_time

