# REST API In-class Exercise

This repository contains the implementation for the REST API in-class exercise. The project is broken down into three main sections:
1. Exploring external APIs with Python `requests`
2. Building a backend with FastAPI
3. Integrating the two together

## Exercise 1: External API Integration
We studied the FDA API (specifically the Food Adverse Event API). The goal was to practice making requests, handling query parameters, managing pagination, handling empty results, and extracting useful fields from real JSON data. 

This functionality was tested using Postman, curl, and Python.

### User Story
"As a user, I want to search for adverse food events related to a specific product industry, so that I can extract and read the types of physical reactions people reported."

## Exercise 2: FastAPI User & Note System
The second part of the exercise involves implementing a RESTful backend using FastAPI. This system manages user accounts and text notes based on the following required user stories:

### Implemented User Stories
* As a user, I can create an account with a username.
* As a user, I can retrieve my account by ID.
* As a user, I can list all users.
* If a username already exists during account creation, the API returns a 409 status code.
* As a user, I can add text notes.
* As a user, I can read my text notes.

## Final Exercise: Integration
The final exercise combines the functionality of Exercise 1 and Exercise 2. 

Specifically, for a user created in Exercise 2, the system successfully pulls an adverse food event from the FDA API (from Exercise 1) and saves that extracted data directly as a text note for the user.

## How to Run
1. Install the required dependencies: `pip install fastapi uvicorn requests`.
2. Start the FastAPI server: `py -m uvicorn exercise2:app --reload`.
3. On another terminal, you can send git and commands to `http://localhost:8000/`.
