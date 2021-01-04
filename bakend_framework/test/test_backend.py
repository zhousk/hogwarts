from datetime import datetime

import requests

from bakend_framework.src.backend import Task, TestCase, db


def test_testcase_get():
    testcase_url = 'http://127.0.0.1:5000//'
    r = requests.post(
        testcase_url,
        json={
            'name': f'case1 {datetime.now().isoformat()}',
            'description': 'description 1',
            'steps': ['1', '2', '3']
        }
    )

    assert r.status_code == 200

    r=requests.get(testcase_url)
    print(r.json())
    assert r.json()['body']


def test_task_post():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.post(
        task_url,
        json={
            'testcases':
                [
                    {
                        'name': f'case3 {datetime.now().isoformat()}',
                        'description': 'description 1',
                        'steps': ['1', '2', '3']
                    },
                    {
                        'name': f'case4 {datetime.now().isoformat()}',
                        'description': 'description 1',
                        'steps': ['1', '2', '3']
                    }
                ]

        }
    )

    assert r.status_code == 200
    # assert r.json() == 'ok'

def test_task_delete():
    task_url = 'http://127.0.0.1:5000/task'
    r = requests.delete(
        task_url,
        json={
            'id': 6
        }
    )
    assert r.status_code == 200
    print(r.json())
    # assert r.json()['msg'] == 'ok'

def test_testCase_update():
    task_url = 'http://127.0.0.1:5000/testcase'
    r = requests.put(
        task_url,
        json={
            'id': 6,
            'name': f'change name {datetime.now().isoformat()}'
        }
    )
    assert r.status_code == 200
    # print(r.json())
    # assert r.json()['msg'] == 'ok'

def test_1():
    task = Task()
    task.testcases = [
        TestCase(name=f'case1 {datetime.now().isoformat()}', description='description 1',
                 steps=['1', '2', '3']),
        TestCase(name=f'case1 {datetime.now().isoformat()}', description='description1',
            steps = ['1', '2', '3'])
    ]
    db.session.add(task)
    db.session.commit()