# Python-Chat-App
* Networking Class Project CS 364.
* This only usable for educatinoal porposes.
* Project depends on lessons from İstanbul Şehir University.
## Server.Py
```
HOST = '192.168.1.79' ## Server ip adress set yours by ipconfig and get your internet ip4 address.
PORT = 1234 ## Server PORT that is basic port you can use any if there is a collision just change it.
```
## Client.Py / Chat.py
```
HOST = input('HOST: ') ### Thats part will set and wait for input so if you give server HOST you can connect. You cange it make it const.
PORT = input('PORT: ') ### Same as HOST
if not PORT: ### If there is none you can use basic port which i declared here.
    PORT = 1234
```
## Authors

* **Cafer Yükseloğlu** - *Initial work* - [cfr.yksl](https://github.com/samuhay/)
* **Saurabh Chaturvedi** - *Documentation* - [medium.com](https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170)
See also the list of [contributors](https://github.com/samuhay/Python-Chat-App/graphs/contributors) who participated in this project.
