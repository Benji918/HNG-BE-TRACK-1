# Number Classification API

A REST API that classifies numbers by calculating various mathematical properties and retrieving a fun fact about the number. This API determines if a number is prime, perfect, an Armstrong number, its digit sum, its parity (odd or even), and fetches a fun fact from the [Numbers API](http://numbersapi.com).

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [API Specification](#api-specification)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [CORS Handling](#cors-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Mathematical Classification:**  
  - Checks if a number is **prime**.
  - Checks if a number is **perfect**.
  - Checks if a number is an **Armstrong number**.
  - Calculates the **digit sum** of the number.
  - Identifies whether the number is **odd** or **even**.
  
- **Fun Fact:**  
  Retrieves a fun fact about the number from the [Numbers API](http://numbersapi.com).

- **Response Format:**  
  Returns JSON responses for both successful requests and error cases.

- **CORS Support:**  
  Configured to handle Cross-Origin Resource Sharing (CORS) so that the API can be called from different origins.

## Technology Stack

- **Backend Framework:** Django & Django REST Framework (DRF)
- **Programming Language:** Python
- **HTTP Client:** `requests` for external API calls (Numbers API)
- **Deployment:** (e.g., Heroku, AWS, DigitalOcean, etc. – ensure your project is deployed to a publicly accessible endpoint)
- **Version Control:** Git (repository hosted on GitHub)

## API Specification

### Endpoint

- **GET** `/api/classify-number?number=<number>`

### Query Parameter

- `number` (required): An integer value to classify.

### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
