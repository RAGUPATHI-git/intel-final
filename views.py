from flask import Blueprint, Flask, render_template,request,redirect,url_for
import google.generativeai as genai
import requests
import numpy as np
from datetime import datetime
import mysql.connector
# from optimum.intel import IPEXModelForCausalLM // intel tool-kit
from transformers import AutoModelForCausalLM 
con=mysql.connector.connect(host="localhost",user="root",password="Ramachandran@9842",database="signup")



API_URL = "https://api-inference.huggingface.co/models/renderartist/simplevectorflux"
headers = {"Authorization": "Bearer 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"}
genai.configure(api_key= "AIzaSyA0T-E9wSZngrAqsK1nz2JOVzonSxTxTOQ")
img_ids = []


def stable_diffusion(prompt):
    
   def query(payload):
            id = str(datetime.datetime.today()).replace(":", '').replace(' ','').replace('-','').replace('.','')
            img_ids.append(id)
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content
   image_bytes = query({
    "inputs": prompt,
    })
    # You can access the image with PIL.Image for example
   import io
   from PIL import Image
   image = Image.open(io.BytesIO(image_bytes))
   image.save('./static/images/saved/'+ id + '.png')






views = Blueprint('views', __name__)


@views.route('/')
def kick_start():
    return render_template('kick_start.html')


@views.route('/home')
def home():
    return render_template('home.html')


@views.route('/input')
def input():
    return render_template('input.html')

@views.route('/output', methods=['POST', "GET"])
def output():
    content = []
    no = 4
    file=open('./static/story.txt', mode='w')
    pro = request.form['userPrompt']
    model = genai.GenerativeModel('gemini-pro')
    # model = IPEXModelForCausalLM(model)
    prompt = f"{pro} "
    response =model.generate_content(prompt)
    file.write(response.text)
    file.close()
    with open('./static/story.txt', 'r', encoding='utf-8') as file:
       paragraphs = file.read()
    paragraphs = paragraphs.split('\n\n')
    for line in paragraphs:
        stable_diffusion(line)
        break
    return render_template('output.html',content= paragraphs,img_ids=img_ids)


@views.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        res=con.cursor()
        u_name=request.form['username']
        password=request.form['password']
        qry="SELECT * FROM USER WHERE u_name=%s"
        res.execute(qry,(u_name,))
        result=res.fetchall()
        if result[0][5]==password:
            return render_template("home.html")
        else:
            return render_template("login.html")
    return render_template("login.html")




@views.route('/signup',methods=["GET","POST"])
def signup():
    if request.method=='POST':
        f_name=request.form['firstname']
        l_name=request.form['lastname']
        u_name=request.form['username']
        email=request.form['email']
        password=request.form['password']
        res=con.cursor()
        qry="INSERT INTO USER (f_name,l_name,u_name,email,pass) VALUES (%s,%s,%s,%s,%s)"
        res.execute(qry,(f_name,l_name,u_name,email,password))
        con.commit()
        return render_template('login.html')
    return render_template("signup.html")