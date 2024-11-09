from sqlite3 import connect, Row

database = "students.db"

def getprocess(sql):
    db = connect(database)
    db.row_factory = Row
    cursor = db.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    db.close()
    return [dict(row) for row in results]

def postprocess(sql):
    db = connect(database)
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()
    return True if cursor.rowcount > 0 else False

def add_record(table, **kwargs):
    keys = list(kwargs.keys())
    values = [kwargs[key] for key in keys]
    fld = "`,`".join(keys)
    val = "','".join(values)
    sql = f"INSERT INTO `{table}`(`{fld}`) VALUES('{val}')"
    return postprocess(sql)

def getall_records(table):
    sql = f"SELECT * FROM {table}"
    return getprocess(sql)
