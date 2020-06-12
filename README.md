## Flask emotional facebook messenger bot


```bash
git clone https://<user_name>@bitbucket.org/vladyslava_solovei/emotional-bot.git

cd emotional-bot

virtualenv venv -p python3

source venv/bin/activate

pip3 install -r requirements.txt
```


## Set credentials

First you need an IBM account [activated](https://cloud.ibm.com/).



1. Create service [here](https://cloud.ibm.com/catalog/services/tone-analyzer)

2. Copy the credentials to authenticate to your service instance:

On the Manage page, click Show Credentials to view your credentials.

Copy the API Key(IAM_AUTHENTICATOR) and URL(SERVICE_URL) values and paste assign to values in credentials.py



## Run server


```
# on unix
gunicorn app:app

# on windows
set FLASK_ENV=development
flask run
```



## How to create a (private) facebook messenger bot



First of all you need a facebook account, logged in, with developer mode [activated](https://developers.facebook.com/).



1. Create a new FB App [here](https://developers.facebook.com/quickstarts/?platform=web), just type in the name of your app (choose wisely, difficult to change afterwards), your contact mail and a captcha. Then click on "pass everything" on the top right. Go to your App, click "Products +" and set up Messanger.



2. Create a new FB Page [here](https://www.facebook.com/pages/create), choose a category, a name (there's a special naming convention. choose wisely, also difficult to change afterwards).



3. Go back to your app and click on "configure" on the messenger's tab.



4. In the "token generation" section, select the page you create earlier to generate an ACCESS_TOKEN. Assign it to variable ACCESS_TOKEN in credentials.py.(it's a big string like : EAACrKioFH4oBAM89bjAPrFmY[...])



5. Create a VERIFY_TOKEN [with uuid](https://www.uuidgenerator.net/version4), assign it to VERIFY_TOKEN variable in credentials.py (for example : b030bde8-bd27-419d-a0b3-[...])



6. Deploy your app. You will need a HTTPS url. Heroku provides free plans to host an app, and it should work out of the box.



(https://heroku.com/deploy)



or use ngrok for testing:


```
ngrok http $PORT
```


7. Click 'Add Callback URL' back in the Facebook Developers page (still in the Messenger tab). Paste the callback URL and paste your VERIFY_TOKEN created earlier.



Check at least the 'messages' box in Subscription Fields, others are optional for the moment.



8. Verify and Save



9. If you did it correctly, your page should respond correctly.
