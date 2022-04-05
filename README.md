# Support_test
My test task

- python → 3.9
- django → 4.0
- celery → 5.2.5

## Development with Docker

 **1) Fork the repository**

 **2) Clone repository**

`git clone ref_generated_in_your_repository` 

 **3) Create at the root of the project env.dev**

*Template: env.dev.template*

 **4) Create an image**

`docker-compose build`

 **5) Run container**

`docker-compose up`

 **6) Create Superuser**

`docker exec django python manage.py createsuperuser`

 **7) If you need to clear the database**

`docker-compose down -v`

### Support Application.

There are two access classes:

> User
> 

> Supporter
> 

### User can:

- сreate a chat with a call
- create chat messages
- change message text
- sees supporter messages in chat
- when the supporter answers, he receives an e-mail

### Supporter can:

- add messages to a chat created by a user
- see all applications
- see active orders
- see frozen orders
- change the status of an order
- see the chats he is in

*P.s. In order to create a message in the chat, the supporter must connect to the chat*

*P.p.s I added a .env file to the repository to demonstrate that I used python-dotenv in this assignment. All keys are invalid. Email and password are invalid. She was disposable*
