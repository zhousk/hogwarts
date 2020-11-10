from pytest2.cal import Cal
import pytest

# 文件命名conftest,自动加载，不用import
@pytest.fixture(scope='module')
def cal_init():
    print("setup_class")
    return Cal()
