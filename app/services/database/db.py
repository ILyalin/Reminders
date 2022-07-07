import aiosqlite as sq

data = 'app/services/database/data1.db'


async def add_new_user(user_name, user_id):
    async with sq.connect(data) as con:
        cur = await con.cursor()
        await cur.execute("SELECT id FROM users WHERE id=?", (user_id,))

        if not (user_id,) in await cur.fetchall():
            await cur.execute("INSERT INTO users(name,id)"
                              "VALUES(?,?)",
                              (str(user_name), user_id,))
            await con.commit()
