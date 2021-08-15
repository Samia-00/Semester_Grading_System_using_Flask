from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///cgpa.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class cgpa(db.Model):
  Serial_No=db.Column(db.Integer,primary_key=True)
  sub=db.Column(db.String(200),nullable=False)
  title= db.Column(db.Integer,nullable=False)
  desc=db.Column(db.Integer,nullable=False)
 
  def __repr__(self) -> str:
        return f"{self.Serial_No} - {self.title}"

@app.route("/",methods =['GET','POST'])
def hello_world():
    if request.method=='POST':
        sub = request.form['sub']
        title = request.form['title']
        desc = request.form['desc']
        Cgpa=cgpa(sub=sub,title=title,desc= desc)
        db.session.add(Cgpa)
        db.session.commit()
    allcgpa = cgpa.query.all() 
    return render_template('index.html', allcgpa=allcgpa)
    
@app.route('/Update/<int:Serial_No>',methods =['GET','POST'])
def update(Serial_No):
    if request.method=='POST':
        sub = request.form['sub']
        title = request.form['title']
        desc = request.form['desc']
        Cgpa = cgpa.query.filter_by(Serial_No=Serial_No).first()
        Cgpa.sub=sub
        Cgpa.title=title
        Cgpa.desc=desc
        db.session.add(Cgpa)
        db.session.commit()
        return redirect("/")
    Cgpa = cgpa.query.filter_by(Serial_No=Serial_No).first()
    return render_template('update.html', Cgpa=Cgpa)
    
@app.route('/Delete/<int:Serial_No>')
def delete(Serial_No):
    Cgpa = cgpa.query.filter_by(Serial_No=Serial_No).first()
    db.session.delete(Cgpa)
    db.session.commit()
    return redirect("/")
    
@app.route('/sgpa', methods=['GET', 'POST'])
def sgpa():
    
    return render_template('sgpa.html')
    
if __name__ == '__main__':
      app.run(debug=True)
