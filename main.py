# -*- coding: utf-8 -*-
"""
每日定时给指定收件人发送固定文案的邮件。

想改内容，只改下面「文案配置」这一段即可，其余不用动。
改完在 GitHub 网页上提交，下一封邮件就会用新文案。
"""

import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header

# ================= 文案配置（只改这里） =================
# 标题：带日期可降低被判定为垃圾邮件的概率，不想要日期就写死一句
SUBJECT = f"每日问候 {datetime.now().strftime('%m月%d日')}"

# 正文：三个引号之间的内容原样变成邮件正文，空行就是分段
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


if __name__ == "__main__":
    main()
