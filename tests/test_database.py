import os

import pytest

from resourcepack.errors.base import ValidFileError

from resourcepack.database import Database

config_path = os.environ["CONFIG_PATH"]


@pytest.mark.pocketknife_organization
class TestCleanOrganization:
    def test_database_init(self):
        wrong_path = 'some/path'
        db = Database('clickhouse', wrong_path, 'wrong_db')
        # try:
        #
        # except ValidFileError as e:
        #     print(e)
