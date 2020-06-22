<img src="https://github.com/Alissonfelipe1234/snapse/workflows/Python%20unittest/badge.svg" title="unit tests" alt="Unit test logo">
<p align="center">
<img src="logo.png" title="Minimalist api" alt="Snapse logo">
</p>

# A image formater api

**What this software do?**

Snapse is a flask api that takes care of the image editing process for your system, in addition to being scalable it is fast and secure </br>

You can integrate with any system without knowing how it is done, because it doesn't matter.</br>

And it's faster than working locally.

## How does it work?
The REST API is servicing all request, while the rabbitMq queue connects the consumer that resizes image and saves it in PNG format on Amazon S3 Cloud Storage Service. </br>

You send the image and the system returns with new file name.

## How to dowload Snapse
```bash
$ git clone https://github.com/Alissonfelipe1234/snapse.git
$ cd snapse
```

## How to run the project
```bash
$ bash run_app.sh
```

## The unit tests
```bash
$ python app/test.py
$ python core/test.py
```
</br>

## Usage
| URL  | HTTP Verb | Param | Return  |
| ------------- |:--------------:|:-------------:| -----:|
| / | GET | None | all routes in JSON |
| /test | GET | None |a message status |
| /resize | POST | Binary image | the file name generad|
