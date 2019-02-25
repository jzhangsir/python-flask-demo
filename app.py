# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session, flash
from connectsql import db, app, Student


# 显示显示信息
@app.route('/mange', methods=['GET', 'POST'])
def mange():
    if request.method == 'GET':
        stu = Student.query.all()
        for p in stu:
            app.logger.debug(p.studentname)
            a = p.studentid
            b = p.studentname
            c = p.subject
            d = p.college
            return render_template('mange.html', stu=stu)


# 添加学生信息
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        sid = request.form.get('sid')
        sname = request.form.get('sname')
        szy = request.form.get('szy')
        sxy = request.form.get('sxy')
        if sid and sname and szy and sxy:
            student = Student.query.filter(Student.studentid == sid, Student.studentname == sname,
                                           Student.subject == szy,
                                           Student.college == sxy)
            if student:
                student = Student(studentid=sid, studentname=sname, subject=szy, college=sxy)
                db.session.add(student)
                db.session.commit()
                return redirect(url_for('mange'))
            else:
                return '添加失败'
        else:
            return '请重新输入'


# 删除学生信息
@app.route('/delete/<studentid>', methods=['GET', 'POST'])
def delete(studentid):
    if request.method == 'GET':
        student = Student.query.get(studentid)
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect(url_for('mange'))


# 查询学生信息
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        sid = request.form.get('sid')
        if not sid:
            return '请输入学号'
        else:
            stu = Student.query.filter(Student.studentid == sid).all()
            if not stu:
                return '查询的学生不存在'
            else:
                for p in stu:
                    app.logger.debug(p.studentid)
                    a = p.studentid
                    b = p.studentname
                    c = p.subject
                    d = p.college
                return render_template('index.html', stu=stu)


# 更新学生信息
@app.route('/update/<studentid>', methods=['GET', 'POST'])
def update(studentid):
    if request.method == 'GET':
        student = Student.query.filter(Student.studentid == studentid).first()
        return render_template('update.html', sid=student.studentid, sname=student.studentname, szy=student.subject,
                               sxy=student.college)
    else:
        student = Student.query.filter(Student.studentid == studentid).first()
        sid = request.form.get('sid')
        sname = request.form.get('sname')
        szy = request.form.get('szy')
        sxy = request.form.get('sxy')
        student.studentid = sid
        student.studentname = sname
        student.subject = szy
        student.college = sxy
        db.session.commit()
        return redirect(url_for('mange'))


if __name__ == '__main__':
    app.debug = True
    app.run()
