from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
DB = "blog.db"


# ---- FRONT PÚBLICO ----

@app.route("/")
def index():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas")
    entradas = cur.fetchall()
    con.close()
    return render_template("index.html", entradas=entradas)

@app.route("/entrada/<int:id>")
def entrada(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas WHERE id=?", (id,))
    entrada = cur.fetchone()
    con.close()
    return render_template("entrada.html", entrada=entrada)


# ---- ADMIN ----

@app.route("/admin")
def admin():
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT * FROM entradas")
    entradas = cur.fetchall()
    con.close()
    return render_template("admin.html", entradas=entradas)

@app.route("/admin/nueva", methods=["GET", "POST"])
def entrada_nueva():
    if request.method == "POST":
        con = sqlite3.connect(DB)
        cur = con.cursor()
        cur.execute("INSERT INTO entradas (titulo, fecha, autor, contenido) VALUES (?, ?, ?, ?)",
            (request.form["titulo"], request.form["fecha"],
             request.form["autor"], request.form["contenido"]))
        con.commit()
        con.close()
        return redirect("/admin")
    return render_template("entrada_form.html", entrada=None)

@app.route("/admin/editar/<int:id>", methods=["GET", "POST"])
def entrada_editar(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    if request.method == "POST":
        cur.execute("UPDATE entradas SET titulo=?, fecha=?, autor=?, contenido=? WHERE id=?",
            (request.form["titulo"], request.form["fecha"],
             request.form["autor"], request.form["contenido"], id))
        con.commit()
        con.close()
        return redirect("/admin")
    cur.execute("SELECT * FROM entradas WHERE id=?", (id,))
    entrada = cur.fetchone()
    con.close()
    return render_template("entrada_form.html", entrada=entrada)

@app.route("/admin/eliminar/<int:id>")
def entrada_eliminar(id):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("DELETE FROM entradas WHERE id=?", (id,))
    con.commit()
    con.close()
    return redirect("/admin")


# ---- ARRANQUE ----

if __name__ == "__main__":
    app.run(debug=True)