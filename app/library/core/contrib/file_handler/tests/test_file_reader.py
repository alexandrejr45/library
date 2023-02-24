import pytest

from library.core.contrib.file_handler.file_reader import FileReader

class TestFileReader:

    @pytest.fixture
    def file(self):
        pass

    def test_should_read_file_with_utf8_enconding(self):
        reader = FileReader().read_file(path='test_csv.csv')

        print()
        for row in reader:
            print(row)
