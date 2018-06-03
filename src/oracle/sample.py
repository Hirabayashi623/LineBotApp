import cx_Oracle as ora
import os

print(ora.clientversion())

if __name__ == '__main__':
    # 文字コードの指定を環境変数で行う
    os.environ["NLS_LANG"] = "JAPANESE_JAPAN.JA16SJISTILDE"

    try:
        tns = ora.makedsn("localhost", 1521, "XE")
        con = ora.connect("SAMPLE", "SAMPLE", tns)

        cur = con.cursor()


        # SELECT文
        cur.execute("select * from tbl_sample")
        rows = cur.fetchall()
        for r in rows:
            print(r)
            print(r[0], ":", r[1])

        # INSERT文
        cur.execute("insert into tbl_sample values (:id, :name)",
                    id=11,
                    name="user11")
        con.commit()

        # SELECT文
        cur.execute("select * from tbl_sample")
        rows = cur.fetchall()
        for r in rows:
            showStr = ""
            for s in r:
                showStr += str(s) + "\t"
            print(showStr)

        # DELETE文
        cur.execute("delete from tbl_sample where id = :id",
                    id=11)
        con.commit()

        # SELECT文
        cur.execute("select * from tbl_sample")
        rows = cur.fetchall()
        for r in rows:
            showStr = ""
            for s in r:
                showStr += str(s) + "\t"
            print(showStr)
    except (ora.DatabaseError) as ex:
        error, = ex.args
        print(error.message)