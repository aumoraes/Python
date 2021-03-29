
from src.hello import HelloWorld
import pytest
from pprint import pprint
class TestMainClass():
    def test_capital_case(self):
        assert HelloWorld().capital_case('semaphore') == 'Semaphore', "erro, estava esperando por "

    def test_raises_exception_on_non_string_arguments(self):
        with pytest.raises(TypeError):
            HelloWorld().capital_case(9)

    # content of test_tmpdir.py
    #@pytest.mark.usefixtures("tmpdir")
    def test_create_file(self, tmpdir):
        pprint(tmpdir)
        p = tmpdir.mkdir("sub").join("hello.txt")
        p.write("content")
        assert p.read() == "content"
        assert len(tmpdir.listdir()) == 1
        # assert 0
        
@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass