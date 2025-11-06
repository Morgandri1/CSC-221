# Final Project
Hello! Thanks for taking the time to read about my final project.

## What is it? 
For my final project, I decided to build a simple file upload app which allows users to store files on my webserver with a permanent link. 

## Structure
This app is in two major pieces: the API and the Web app. 
The API is built in Python using Quart, Solders, and the Werkzeug worker. 
The API uses Quart to asynchronously handle requests for better concurency, allowing short response times on individual requests. As a failsafe, the API also uses Solders to generate a unique filename for each uploaded file. This is done using a base58 encoded ED-25519 epliptic curve public key, which serves as a lightweight UUID. 
The web application is built in Next.Js using react, tailwind css, and Typescript for increased type safety to help eliminate runtime panics.
Both of these services are running independently on NGINX instances in the cloud, the API can be found in [Railway](https://railway.com/) and the app in [Vercel](https://vercel.com). I chose these providers because of their low-cost and lightweight NGINX hosting, as well as their exceptional configurability. 

## My experience building this app 
I was looking into Quart for another project outside of class, and noticed it had built-in modules for file handling. I decided this could be a good final project, as it allows me to handle user input remotely over HTTP(s). I decided to also implement Solders, a python library I have contributed to in the past. I ran into some trouble with the CORS requests, and needed to implement `quart-cors`, a library which automatically handles CORS (cross origin resource sharing) preflight requests.

## Hosted service links 
- [App](https://csc-221-final.vercel.app/)
- [Api](https://csc-221-production.up.railway.app/)