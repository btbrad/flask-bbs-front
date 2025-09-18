import random
import string
from flask import Blueprint, jsonify, render_template, request, current_app
from flask_mail import Message
from exts import mail, cache

bp = Blueprint("front", __name__, url_prefix="/")


@bp.route("/")
def hello_world():
    return "Hello World!"


# @bp.get("/email/captcha/")
# def email_captcha():
#     email = request.args.get("email")
#     if not email:
#         return jsonify({"code": 400, "message": "请输入邮箱"})
#     source = list(string.digits)
#     captcha = "".join(random.sample(source, 6))
#     message = Message(
#         subject="flask_bbs注册邮箱验证",
#         body=f"您的验证码是：{captcha}",
#         recipients=[email],
#     )
#     try:
#         mail.send(message)
#     except Exception as e:
#         print("邮件发送失败")
#         print(e)
#         return jsonify({"code": 500, "message": "邮件发送失败"})
#     return jsonify({"code": 200, "message": "邮件发送成功"})


@bp.get("/email/captcha/")
def email_captcha():
    email = request.args.get("email")
    if not email:
        return jsonify({"code": 400, "message": "请输入邮箱"})
    source = list(string.digits)
    captcha = "".join(random.sample(source, 6))
    subject = "flask_bbs注册邮箱验证"
    body = f"您的验证码是：{captcha}"
    current_app.celery.send_task("send_mail", (email, subject, body))
    cache.set(email, captcha)
    print(cache.get(email))
    return jsonify({"code": 200, "message": "邮件发送成功"})


@bp.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("front/login.html")


@bp.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        pass
    else:
        return render_template("/front/register.html")
