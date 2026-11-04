# -*- coding: utf-8 -*-
import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header

# ================= 文案配置（只改这里） =================
SUBJECT = f"每日问候 {datetime.now().strftime('%m月%d日')}"

BODY = """你好：

见字如面。

今天也想和你说一声，一切顺利，照顾好自己。

—— 你的名字
"""
# ========================================================


def main():
    sender = os.environ["MAIL_SENDER"]
    auth_code = os.environ["MAIL_AUTH_CODE"]
    receiver = os.environ["MAIL_RECEIVER"]

    msg = MIMEText(BODY, "plain", "utf-8")
    msg["Subject"] = Header(SUBJECT, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.qq.com", 465, timeout=20) as server:
        server.login(sender, auth_code)
        server.sendmail(sender, [receiver], msg.as_string())

    print(f"已发送 -> {receiver}")


if __name__ == "__&#8203;main__":
    main()
