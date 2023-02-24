import csv
from typing import Any

class FileReader:


    def read_file(self, path: str) -> Any:
        csv_file = []

        with open(file=path, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                csv_file.append(row)

        return csv_file