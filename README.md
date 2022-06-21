# 自用办公常用工具集

## PDF常用工具

1. 截取页面

   ```
   Usage: pdf_utils.py subset [OPTIONS] INPUT_PATH

     截取pdf文件部分页面

   Arguments:
     INPUT_PATH  [required]

   Options:
     -s, --start-page INTEGER  start page number  [default: 1]
     -e, --end-page INTEGER    end page number  [default: -1]
     -o, --output-path TEXT    output path
     --help                    Show this message and exit.
   ```
2. 拼接页面

   ```
   Usage: pdf_utils.py merge [OPTIONS] INPUT_PATHS...

     拼接指定的pdf文件路径列表

   Arguments:
     INPUT_PATHS...  [required]

   Options:
     -o, --output-path TEXT  output path
     --help                  Show this message and exit.
   ```
3. 旋转页面

   ```
   Usage: pdf_utils.py rotate [OPTIONS] INPUT_PATH

     旋转指定pdf文件页面

   Arguments:
     INPUT_PATH  [required]

   Options:
     -s, --start-page INTEGER  start page number  [default: 1]
     -e, --end-page INTEGER    end page number  [default: -1]
     -a, --angle INTEGER       angle to rotate  [default: 90]
     -o, --output-path TEXT    output path
     --help                    Show this message and exit.
   ```

## PPT常用工具

1. 提取备注
   ```
   Usage: ppt_utils.py [OPTIONS] INPUT_PATH

     提取pptx备注

   Arguments:
     INPUT_PATH  [required]

   Options:
     -o, --output-path TEXT          output path
     --install-completion [bash|zsh|fish|powershell|pwsh]
                                     Install completion for the specified shell.
     --show-completion [bash|zsh|fish|powershell|pwsh]
                                     Show completion for the specified shell, to
                                     copy it or customize the installation.
     --help                          Show this message and exit.
   ```


## 邮箱常用工具

1. 发送邮件

```
Usage: mail_utils.py [OPTIONS] SUBJECT CONTENT SENDER PASSWORD RECEIVER

  qq邮箱发送邮件

Arguments:
  SUBJECT   邮件主题  [required]
  CONTENT   邮件正文  [required]
  SENDER    发件人邮箱  [required]
  PASSWORD  发件人POP3密码  [required]
  RECEIVER  收件人邮箱  [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.
```
