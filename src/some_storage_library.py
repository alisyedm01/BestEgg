import os
import shutil
from pathlib import Path

class SomeStorageLibrary:

    def __init__(self):
        print("Instantiating storage library...")
        self.destination = Path(__file__).parent.parent.resolve() / 'data/destination'
        if not self.destination.is_dir():

            self.destination.mkdir(parents=True)

    def load_csv(self, filename: str) -> None:
        dest_file = self.destination / Path(filename).name
        if dest_file.exists():


            print(f"File already exists: {dest_file}. Skipping operation.")
            return

        print(f"Loading the following file to storage medium: {filename}")
        
        shutil.move(filename, self.destination)
        print('Load completed!')