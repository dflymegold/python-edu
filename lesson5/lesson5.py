import  sqlite3
conn = sqlite3.connect('cityid.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS CityId(
   country TEXT,
   city TEXT,
   cityid TEXT PRIMARY KEY
   );
""")

with open("full_city_list.txt", "r") as f:
    rows = f.readlines()
    for row in rows:
        fields = row.split(';')
        c.execute(f'INSERT INTO CityId (country, city, cityid)'\
                  f"VALUES ('{fields[0]}','{fields[1]}','{fields[2]}')")

conn.commit()

for row in c.execute('SELECT * FROM CityId'):
    print(row)

conn.close()
