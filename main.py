from flask import Flask, render_template, request, redirect, send_file
from job_scrap_wework import extract_jobs_we
from job_scrap_web3 import extract_jobs_web3
from job_scrap_berlin import job_detail_scrapper
from file import save_berlin, save_wework, save_web3

app = Flask(__name__)

wework_db = {}
web3_db = {}
berlin_db = {}


@app.route("/")
def home():
    return render_template("home.html")


# wework
@app.route("/search_wework")
def first_search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in wework_db:
        jobs = wework_db[keyword]
    else:
        jobs = extract_jobs_we(keyword)
        wework_db[keyword] = jobs
    return render_template("search_wework.html", keyword=keyword, jobs=jobs)


@app.route("/export_wework")
def export_wework():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in wework_db:
        return redirect(f"/search_wework?keyword={keyword}")

    save_wework(keyword, wework_db[keyword])
    return send_file(
        f"wework_{keyword}.csv",
        as_attachment=True,
        mimetype="text/csv; charset=UTF-8",
    )


# web3
@app.route("/search_web3")
def second_search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in web3_db:
        jobs = web3_db[keyword]
    else:
        jobs = extract_jobs_web3(keyword)
        web3_db[keyword] = jobs
    return render_template("search_web3.html", keyword=keyword, jobs=jobs)


@app.route("/export_web3")
def export_web3():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in web3_db:
        return redirect(f"/search_web3?keyword={keyword}")

    save_web3(keyword, web3_db[keyword])
    return send_file(
        f"web3_{keyword}.csv",
        as_attachment=True,
        mimetype="text/csv; charset=UTF-8",
    )


# berlin
@app.route("/search_berlin")
def third_search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in berlin_db:
        jobs = berlin_db[keyword]
    else:
        jobs = job_detail_scrapper(keyword)
        berlin_db[keyword] = jobs
    return render_template("search_berlin.html", keyword=keyword, jobs=jobs)


print(berlin_db)


@app.route("/export_berlin")
def export_berlin():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in berlin_db:
        return redirect(f"/search_berlin?keyword={keyword}")

    save_berlin(keyword, berlin_db[keyword])
    return send_file(
        f"berlin_{keyword}.csv",
        as_attachment=True,
        mimetype="text/csv; charset=UTF-8",
    )


if __name__ == "__main__":
    app.run()
