from sqlalchemy import create_engine, text


def create_books_table():
    engine = create_engine(
        f"postgresql://postgres:mypassword@postgres_container:5432/my_db"
    )

    with engine.begin() as con:
        with open("flaskr/sql/create_table.sql", "r") as f:
            create_table_sql = text(f.read())
        con.execute(create_table_sql)
