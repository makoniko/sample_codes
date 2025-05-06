from flaskr import app
from flask import render_template, request, redirect, url_for
from sqlalchemy import create_engine, text

engine = create_engine(
    f"postgresql://postgres:mypassword@postgres_container:5432/my_db"
)


# @app.route()で指定されたパスのページにアクセスがあったときに対象の関数が呼ばれる
@app.route("/")
def index():

    with engine.begin() as con:
        with open("flaskr/sql/select_all_from_books.sql", "r") as f:
            select_all_from_books_sql = text(f.read())
        db_books = con.execute(select_all_from_books_sql).fetchall()

    books = []
    for row in db_books:
        books.append({"title": row[0], "price": row[1], "arrival_day": row[2]})

    # render_template()はtemplatesフォルダ配下の対象ページをクライアントに返す
    return render_template("index.html", books=books)


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/register", methods=["POST"])
def register():
    title = request.form["title"]
    print(title)
    price = request.form["price"]
    print(price)
    arrival_day = request.form["arrival_day"]
    print(arrival_day)

    with engine.begin() as con:
        con.execute(
            text(f"INSERT INTO books VALUES('{title}', '{price}', '{arrival_day}')")
        )
        con.commit()

    # url_for()で指定した関数を実行し、対象関数のrender_template()で指定したページをクライアントに表示させる
    return redirect(url_for("index"))
