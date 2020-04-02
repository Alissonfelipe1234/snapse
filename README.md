<p align="center">
<img src="logo.png" title="Minimalist api" alt="Snapse logo">
</p>

# A image formater api

**What this software do?**

Snapse is a flask api that takes care of the image editing process for your system, in addition to being scalable it is fast and secure </br>

You can integrate with any system without knowing how it is done, because it doesn't matter

## How to dowload Snapse
```bash
$ git clone https://github.com/Alissonfelipe1234/snapse.git
$ cd snapse
```

## How to run the project
```bash
$ docker build .
$ docker-composer up -d
```

## The unit tests
```bash
$ python app/test.py
$ cd core/
$ python test.py
```
</br>

## Usage
| URL  | HTTP Verb | Param | Return  |
| ------------- |:--------------:|:-------------:| -----:|
| / | GET | None | all routes in JSON |
| /test | GET | None |a message status |
| /send | POST | Binary image | the file name generad|
