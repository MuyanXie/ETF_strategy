#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:





# In[2]:


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header


# In[3]:


# from_addr='1756314803@qq.com'   #邮件发送账号
# to_addrs='1756314803@qq.com'   #接收邮件账号

# smtp_server='smtp.qq.com'#固定写死
# smtp_port=465#固定端口


# In[4]:


# stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
# stmp.login(from_addr,qqCode)


# In[5]:


# message = MIMEText('运行\n成功', 'plain', 'utf-8')   #发送的内容
# message['From'] = Header("Python邮件预警系统", 'utf-8')   #发件人
# message['To'] = Header("管理员", 'utf-8')   #收件人

# from datetime import datetime

# subject = 'Jupyter Notebook 运行结果(时间： ' + str(datetime.now()) + ")"
# message['Subject'] = Header(subject, 'utf-8')  #邮件标题

# try:
#     stmp.sendmail(from_addr, to_addrs, message.as_string())
# except Exception as e:
#     print ('邮件发送失败--' + str(e))
# print ('邮件发送成功')


# In[7]:


def send(news):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    from_addr='1756314803@qq.com'
    to_addrs='1756314803@qq.com'  
    qqCode="" # this is the authorization code we need to get from qq.com; For security reasons, this is deleted
    smtp_server='smtp.qq.com'
    smtp_port=465
    stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
    stmp.login(from_addr,qqCode)
    message = MIMEText(news, 'plain', 'utf-8')
    message['From'] = Header("Python邮件预警系统", 'utf-8')
    message['To'] = Header("管理员", 'utf-8')

    from datetime import datetime

    subject = 'Jupyter Notebook 运行结果(时间： ' + str(datetime.now()) + ")"
    message['Subject'] = Header(subject, 'utf-8')

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
        print ('邮件发送成功')
    except Exception as e:
        print ('邮件发送失败--' + str(e))


# In[1]:


def news_maker(cur):
    tempo = ""
    for i in cur:
        #print(type(i))
        tempo= tempo + i+"\r\n"
    return tempo


# In[ ]:




