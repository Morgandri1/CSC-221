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