import sqlite3

from inspect import cleandoc


def sql_lite():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("db.sqlite3")

    cur = con.cursor()

    # Return all results of query
    cur.execute("SQL")

    # Be sure to close the connection
    con.close()


photo_names = []
photo_type = "wildlife"
values = []
for photo in set(photo_names):
    values.append(f"('media/images/{photo}', '{photo_type}', current_timestamp)")

value_str = ",\n".join(values)
sql = f"""
insert into
    api_photo("photo", "photo_type", "created_at")
values
{value_str};
"""

print(f"{cleandoc(sql)}\n")
