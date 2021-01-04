import json
from typing import List

from flask import app, Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
# sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/hogwarts'

db = SQLAlchemy(app)

# fake db
app.config['db'] = []


@app.route('/')
def hello():
    return 'hello from ceshiren.com'


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=True)
    steps = db.Column(db.String(1024), nullable=True)
    # 关联字段必须在多的一方
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
                        nullable=False)
    # 这个关联关系在多的一方和少的一方都行，字段testcases可以用于方向关联执行增删改查,是这样一个类型InstrumentedList
    task = db.relationship('Task', backref='testcases', lazy=True)

    def __repr__(self):
        return '<TestCase id:%r; name:%r; description:%r; task_id:%r; steps:%r>' % (
            self.id,self.name, self.description, self.task_id, json.loads(self.steps))


class TestCaseService(Resource):
    def get(self):
        """
        测试用例的浏览获取 /testcase.json /testcase.json?id=1
        """
        testcases: List[TestCase] = TestCase.query.all()
        res = [{
            'id': testcase.id,
            'name': testcase.name,
            'description': testcase.description,
            'steps': json.loads(testcase.steps)
        } for testcase in testcases]
        return {
            'body': res
        }

    def post(self):
        """
        上传用例， 更新用例
        /testcase.json  {'name': 'xx', 'description': 'xxx', 'steps': []}
        """
        testcase = TestCase(
            name=request.json.get('name'),
            description=request.json.get('description'),
            steps=json.dumps(request.json.get('steps'))
        )
        db.session.add(testcase)
        db.session.commit()
        return 'ok'

    def put(self):
        id = request.json.get("id")
        TestCase.query.filter_by(id=id).update(request.json)
        # 这里会报错'SQLAlchemy' object has no attribute 'sesison'，貌似前面没用session这里就不用commit
        # db.sesison.commit()



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # testCases = db.relationship('TestCase', backref='task', lazy=True)


# todo: 作业1
# 完成TaskService的功能，基本的增删改查
# 拔高：增加的时候关联TestCase.
class TaskService(Resource):
    def get(self):
        id = request.args.get('id')
        if id:
            task = Task.query.filter_by(id=id).first()
            return {
                'msg': 'ok',
                'body': str(task.testcases)
            }
        else:
            tasks = Task.query.all()
            return {
                'msg': 'ok',
                'body': [str(task.testcases) for task in tasks]
            }

    def post(self):
        """
        上传用例， 更新用例
        /task.json  {'na': 'xx', 'description': 'xxx', 'steps': []}
        """
        testCasesJson = request.json.get('testcases')
        # testcases = [{
        #     'name': testcase.get('name'),
        #     'description': testcase.get('description'),
        #     'steps': testcase.get('steps')
        # } for testcase in testCasesJson]
        # task = Task()
        # task.testcases = testcases
        task = Task()
        for testcaseJson in testCasesJson:
            testcase = TestCase(name=testcaseJson.get('name'), description=testcaseJson.get('description'),
                                steps=json.dumps(testcaseJson.get('steps')))
            task.testcases.append(testcase)

        db.session.add(task)
        db.session.commit()
        return 'ok'

    def delete(self):
        # task = Task.query.filter_by(id=id).first()
        # TestCase.query.filter_by(task_id == task.id).delete()
        id = request.json.get('id')
        db.session.query(TestCase).filter(TestCase.task_id == id).delete()
        Task.query.filter_by(id=id).delete()
        db.session.commit()


class ReportService(Resource):
    def get(self):
        pass


api.add_resource(TestCaseService, '/testcase')
api.add_resource(TaskService, '/task')
api.add_resource(ReportService, '/report')

if __name__ == '__main__':
    app.run(debug=True)
