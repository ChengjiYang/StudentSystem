from django.shortcuts import render, redirect
import pymysql


def classes(request):
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yang15045629836',
                           db='StudentSystem', charset='utf8')
    # 创建游标
    cursor = conn.cursor()
    # 设置返回字典
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL，并返回收影响行数
    # effect_row = cursor.execute("update hosts set host = '1.1.1.2'")
    # 执行SQL，并返回受影响行数
    effect_row = cursor.execute("select id, title from class order by id",)
    class_list = cursor.fetchall()
    print(class_list)

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

    # 提交，不然无法保存新建或者修改的数据
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return render(request, 'classes.html', {'class_list': class_list})

def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        print(request.POST.get('title'))
        value = request.POST.get('title')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yang15045629836',
                               db='StudentSystem', charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        effect_row = cursor.execute("select max(id) as m from class")
        max_id = cursor.fetchall()
        print(max_id)
        print(max_id[0])
        print(max_id[0]['m'])

        cursor.execute("insert into class(id, title) value(%s, %s)", [str(max_id[0]['m'] + 1), value])

        # 提交，不然无法保存新建或者修改的数据
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

        return redirect('/classes/')

def del_class(request):
    cid = request.GET.get('cid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='yang15045629836',
                           db='StudentSystem', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 删除该条数据
    cursor.execute("delete from class where id=%s", [cid,])
    conn.commit()

    # 更新之后数据
    cursor.execute("update class set id = id - 1 where id > %s", [cid,])
    conn.commit()

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    return redirect('/classes/')
