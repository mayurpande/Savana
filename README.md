# Savana

> An application that allows a user to upload a PDF file and returns a TXT file or upload a TXT file and returns
> specific content in JSON form.

As requested in the description: The main purpose of this application is to be able to convert PDF file format 
to TXT file format. Also you should be able to extract some specific information from a TXT file with a rehashed id 
(MR number in the TXT file) and return JSON from it. 

According to the considerations I choose to use the framework Django for this project as I have built it as an monolithic
app. The reason for building a monolithic app was as this project was on a small scale, I believed it would be more suited
to be monolithic. 

I did think about building a microservices app using Flask where one microservice would have been the
PDF to TXT converter and the other would have been the TXT to JSON converter (with a database). The two microservices would
have been connected but able to work alone, so for example if a user where to use the PDF to TXT converter, there would 
be an option to convert the returned TXT file into JSON straight away, thus making use of the second microservice. Or if
a user just wanted to convert TXT to JSON they would be able to use that service as a stand-alone. However this would have been
my first microservices project and to follow the other consideration of KISS, I decided to go ahead with the monolithic app.


## Workflow
I followed a TDD approach for this project. My thought process was to have two pages that had forms on them that allows
a user to upload a PDF file on one page and a TXT file on the other and return the related content.

My first port of call was to create a functional test for handling user stories. So what I did was create a driver using 
the Selenium package. Then I created a class that inherits from Django's `StaticLiveServerTestCase` this is in order to be
able to render the static files from the app. Then using Selenium I wrote some commands to act how a user would on my site.
So for example the user loads up the webpage they try to submit an empty form, for this case I would want the form not to submit
and show an error. 

This is where my FT first failed. So then this prompts me to write a unit test. So I wrote a unit test
to handle the GET request for the method. The this fails indicating that there was no url, so I create a url, run the test
again and it prompted there was no view, so I create a view. The unit test passed.

So then I again run the FT, and it fails as there was no element type `form` on the page. So I adjusted the unit test, to 
`assertTemplateUsed` and run the test again it failed, so I created a template.

This was the general flow I followed, run the FT if it fails, create a unit test, when that fails, write some code.
Run the unit tests again, if they pass go back to the FT, if not edit the code.

I wrote unit tests for the handling of the forms as I wanted to validate against bad input (i.e. no input/wrong file type).
As well as if form submits.

Then I went back to the testing the views, so in my test up a opened an test file (PDF or TXT depending view class being 
tested) created a POST response.

For the PDF converter, I used the `pdftotext` package the test methods consisted of checking whether the text file output saved.
If the text file started and ended with specific strings. I also tested whether the returned HTTP response was a file that was downloaded.

For the TXT to JSON converter I made use of the sqlitedb normally I would use either MySQL or PostgreSQL. However as I only 
created one table it made sense to make use of this. I created a model with columns: `patient_id`, `document_text`, `mr_num`.
The `patient_id` was a unique id generating using the `uuid` package, this was in order to return json with an id relating
to the MR (patient id) in the TXT file. This was using the `patient_id` uuid it is able to retrieve the information for the patient.
However in the description it was unclear whether it wanted all data of the patient stored in the db or in a separate table with a
reference to it (one-to-one join). So this is why I choose to only insert the data that is required for the JSON.

I used regex to search the TXT file for the MR and then I to the index of where "DIAGNOSES" occurred and sliced the string from 
there onwards to get the free text.

The test for the view was to see if the row on post had been inserted with the correct mr num and it passed.
I then proceeded as for the PDF converter and returned a HTTP response with the downloaded json file.

## Development Setup

#### OS Dependencies (from the pdftotext github repo)

##### Debian, Ubuntu, and friends

```
sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
```
 
##### Fedora, Red Hat and friends

```.env
sudo yum install gcc-c++ pkgconfig poppler-cpp-devel python3-devel
```

##### macOS

```
brew install pkg-config poppler python
```

#### Windows

Currently tested only when using conda:

 - Install the Microsoft Visual C++ Build Tools
- Install poppler through conda:
  `conda install -c conda-forge poppler`


Create a virtual environment within the repo and then install `requirements.txt`: 

``` 
user@pc~Savana/$ python3 -m venv env 

user@pc~Savana/$ source env/bin/activate 

(env) user@pc~Savana/$ pip install -r requirements.txt 

(env) user@pc~Savana/$ python manage.py makemigrations

(env) user@pc~Savana/$ python manage.py migrate

(env) user@pc~Savana/$ python manage.py runserver
``` 

Windows: 

Create a virtual environment within the repo and then install `requirements.txt`: 

``` 
C:\Users\your_user\Documents\Savana\>py -m venv env 

C:\Users\your_user\Documents\Savana\>env\Scripts\activate.bat 

(env) C:\Users\your_user\Documents\Savana\> pip install -r requirements.txt 

(env) C:\Users\your_user\Documents\Savana\> python manage.py makemigrations

(env) C:\Users\your_user\Documents\Savana\> python manage.py migrate

(env) C:\Users\your_user\Documents\Savana\> python manage.py runserver

```

Proceed to 127.0.0.1:8000 in your browser and you are able to use the site.

Testing (using existing activated virtual environment)

Linux:


Unit Tests
```
(env) user@pc~Savana/$ python manage.py test converter
```
Functional Tests
```
(env) user@pc~Savana/$ python manage.py test functional_tests
```

Windows:

Unit Tests
```
(env) C:\Users\your_user\Documents\Savana\> python manage.py test converter
```

Functional Tests
```
(env) C:\Users\your_user\Documents\Savana\> python manage.py test functional_tests
```
 
## Release History 

* 0.0.1 
