import pytest

def _test_pass():
    assert (1,2,3) == (1,2,3,4)


'''
➜  pytest git:(master) ✗ pytest test_startone.py 
======================================================================================== test session starts ========================================================================================
platform darwin -- Python 3.7.5, pytest-5.2.1, py-1.8.0, pluggy-0.13.1
rootdir: /Users/liliang/PycharmProjects/selenium-train/test/pytest
plugins: html-2.0.0, rerunfailures-7.0, metadata-1.8.0
collected 1 item                                                                                                                                                                                    

test_startone.py .

.表示：运行了一个测试用例，且测试通过(..表示两个测试用例通过)。如果想查看详情添加参数-v或--verbose (如： pytest -v|--verbose test_startone.py)
Failure（可能是使用xpass与strick冲突导致的） ： F
error(可能由fixture或hook函数引起的) ： E
skip（@pytest.mark.skip()或@pytest.mark.skipif()） ：S
xfail（@pytest.mark.xfail(),预期失败）：x
xpass （预期失败但通过）：X


pytest不支持__init__的类间层次关系，可以使用contest.py

配置虚拟环境
pip3 install -U virtualenv 
python3 -m virtualenv venv
source venv/bin/activate
pip install pytest

获取帮助：
pytest --help

platform darwin(mac,Windows) -- Python 3.7.5, pytest-5.2.1）, py-1.8.0（pytest包, pluggy-0.13.1（pytest包 -- /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
rootdir（当前起始目录）: /Users/liliang/PycharmProjects/selenium-train/test/pytest
inifile(配置文件)：可能是pytest.ini,tox.ini，setup.cfg


pytest执行的测试文件：test开头或_test结尾
测试函数、测试类方法应当命名为：test_<something>
测试类应命名为：Test<something>

1.3运行单个测试用例(::后是测试方法名)
pytest --verbose test_startone.py::test_default

--collect-only:展示在给定的配置中哪些测试用例被运行
-k 允许使用表达式指定希望运行的测试用例（如：pytest -v -k 'dicts or defaults'）
-m 标记测试后分组，以便快速的选中或运行，
Page31
'''

from collections import namedtuple
Task = namedtuple('Task',['summary','ower','done','id'])
Task.__new__.__defaults__ = (None,None,False,None)

def test_default():
    """测试default"""
    T1 = Task()
    T2 = Task(None,None,False,None)
    assert T1 == T2

def test_member_access():
    t = Task('my milk','brain')
    assert t.summary == 'my milk'
    assert t.ower == 'brain'
    assert (t.done,t.id) == (False,True)

def test_asdict():
    t_task = Task('do someting','okken',True,21)
    t_dict = t_task._asdict()
    expect = {'summary' : 'do something',
        'ower' : 'okken',
        'down' : True,
        'id' : 21
    }
    assert t_dict == expect


def test_replace():
    t_berfore = Task('finish book','brain',False)
    t_after = t_berfore._replace(id=10,done=True)
    t_expected = Task('finish book','brain',True,10)
    assert t_after == t_expected
