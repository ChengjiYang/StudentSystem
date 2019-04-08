# README

## Author:
Chengji Yang (杨承基)

## Review
1. Web 框架本质
    - 本质 socket
    - HTTP 协议
        - 头
        - 体
    - 模板引擎的渲染在**服务端**进行, 生成字符串是进入到 HTML, 传输的是**字符串**
2. Django

## 学员管理系统

### 介绍
学生系统, 进行学生的增删改查等操作

### 功能

1. 表
    - 班级 (id, title)
    - 学生 (id, title, classID)
    - 老师 (id, name)
    - 老师班级关系表 (id, teacherID, classID)
2. 单表操作
    - 增
    - 删
    - 改
    - 查
3. 一对多操作
    - 增
    - 删
    - 改
    - 查
4. 多对多操作
    - 增
    - 删
    - 改
    - 查