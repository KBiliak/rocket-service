def create_rocket(mysql, rocket):
    with mysql.connection.cursor() as cursor:
        sql = f"insert into rocket(name, destination, owner)" \
              f"value('{rocket['name']}', " \
              f"'{rocket['destination']}'," \
              f"'{rocket['owner']}') "
        cursor.execute(sql)
        mysql.connection.commit()


def get_rocket(mysql):
    with mysql.connection.cursor() as cursor:
        sql = f"select * from rocket"
        cursor.execute(sql)
        rows = cursor.fetchall()
        result = []
        for row in rows:
            rocket = {
                "id": row[0],
                "name": row[1],
                "destination": row[2],
                "owner": row[3]
            }
            result.append(rocket)
    return result

def update_rocket_id(mysql, rocket, id):
    with mysql.connection.cursor() as cursor:
        sql = f"update rocket set name = '{rocket['name']}', destination = '{rocket['destination']}', " \
              f"owner = '{rocket['owner']}' where id = {id} "
        cursor.execute(sql)
        mysql.connection.commit()