import typer
from .tools import pdf_utils, ppt_utils, mail_utils

app = typer.Typer(name='toolkit')
app.add_typer(pdf_utils.app, name='pdf')
app.add_typer(ppt_utils.app, name='ppt')
app.add_typer(mail_utils.app, name='mail')

def main():
    app()

if __name__ == '__main__':
    main()
