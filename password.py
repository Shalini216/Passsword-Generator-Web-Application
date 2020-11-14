from flask import Flask, render_template, request
import random, string, pyperclip
app = Flask(__name__)

@ app.route('/')
def password():
    return render_template('inputbox.html')
@ app.route('/g',methods=['POST'])
def others():
    password_inputs=[]
    pass_len=request.form.get('length')
    pass_len=int(pass_len)
    if request.form.get('symbol'):
        s1=string.punctuation
        password_inputs.extend(list(s1))
    if request.form.get('number'):
        s2=string.digits
        password_inputs.extend(list(s2))
    if request.form.get('capital'):
        s3=string.ascii_uppercase
        password_inputs.extend(list(s3))
    if( request.form.get('small')):
        s4=string.ascii_lowercase
        password_inputs.extend(list(s4))

    if request.form.get("Generate"):
        Your_password="".join(random.sample(password_inputs, pass_len))
        return (Your_password)


app.run(debug=True)