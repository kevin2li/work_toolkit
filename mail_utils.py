import smtplib
import traceback
from email.mime.text import MIMEText
from email.utils import formataddr
from loguru import logger
import typer

app = typer.Typer()

@app.command(name="mail", help="qq邮箱发送邮件")
def mail(
    subject: str = typer.Argument(..., help="邮件主题"),
    content: str = typer.Argument(..., help="邮件正文"),
    sender: str = typer.Argument(..., help="发件人邮箱"),
    password:str = typer.Argument(..., help="发件人POP3密码"),
    receiver:str = typer.Argument(..., help="收件人邮箱"),
):
    """ qq邮箱发送邮件

    Args:
        subject (str): 主题
        content (str): 正文
        sender (str): 发件人邮箱
        password (str): 密码
        receiver (str): 收件人邮箱
    """    
    try:
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr([sender, sender])
        msg['To'] = formataddr(["", receiver])
        msg['Subject'] = subject

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(sender, password)
        server.sendmail(sender, [receiver, ], msg.as_string())
        server.quit()
        logger.error("发送邮件成功！")
    except Exception:  
        logger.error("发送邮件失败！")
        traceback.print_exc()

if __name__ == '__main__':
    app()
