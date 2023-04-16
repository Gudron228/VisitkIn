from app import app
from flask import render_template, request, flash, abort, redirect, url_for, g
from fpdf import FPDF
from app.forms import Download


@app.route("/<profile_id>")
@app.route("/index<profile_id>")
def ind(profile_id):
    form = Download()
    if form.validate_on_submit():
        return redirect(url_for('qrcode'))
    return render_template('index.html', title='VisitkIn', form=form)


@app.route('/qrcode<profile_id>')
def qrcode(profile_id):
    return render_template('qrcode.html')

