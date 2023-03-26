import requests
import threading as th
import os
API_KEY="<YOUR API KEY HERE>"
API_BASE_URL="<YOUR API BASE URL>"

def send_complex_message(reciever_email, path_to_file, name_of_file,text_msg="",html_msg=""):
    file=os.path.join(path_to_file,name_of_file)
    URL="/messages".format(API_BASE_URL)
    return (requests.post(URL,
        auth=("api",API_KEY),
        files=[("attachment", ("test.jpg", open(file,"rb").read())),
               ],
        data={"from": "prateekasme@gmail",
              "to": f"{reciever_email}",
              "subject": "Security FIGHT Alert from : TEAM\t''>.<''\t'",
              "text": "{0}".format(text_msg),
              "html": "<html>{0}</html>".format(html_msg)}))


if __name__=="__main__":
    send_complex_message("<EMAIL_OF_RECIEVER>","","img.png",'yeah dekho','<a href="<URL_YOU LIKE>">click me to test me</a>')
