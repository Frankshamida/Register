from flask import Flask, render_template, request, redirect
from dbhelper import *

app = Flask(__name__)
uploadfolder = "static/images"
app.config['UPLOAD_FOLDER'] = uploadfolder
app.config['SECRET_KEY'] = '!@#%$$%$%' 

@app.route("/saveinformation", methods=['GET', 'POST'])
def saveinformation():
    name = request.args.get('name')
    imagename = f"{uploadfolder}/{name}.jpg"
    
    file = request.files['webcam']
    file.save(imagename)
    
    ok = add_record('registrations', name=name, imagename=imagename)
    return redirect("/")

@app.route("/")
def index():
    regs = getall_records('registrations')
    return render_template("index.html", pagetitle="REGISTRATION", regs=regs)

if __name__ == "__main__":
    app.run(debug=True)
