import typer

from .tools import (csv_utils, hash_utils, json_utils, mail_utils, pdf_utils,
                    ppt_utils, qrcode_utils)

app = typer.Typer(name='toolkit')
app.add_typer(pdf_utils.app, name='pdf')
app.add_typer(ppt_utils.app, name='ppt')
app.add_typer(mail_utils.app, name='mail')
app.add_typer(csv_utils.app, name='csv')
app.add_typer(json_utils.app, name='json')
app.add_typer(qrcode_utils.app, name='qrcode')
app.add_typer(hash_utils.app, name='hash')

def main():
    app()

if __name__ == '__main__':
    main()
