# Job Board Backend - ProDev BE

## Overview

This project focuses on developing the backend for a **Job Board Platform** that provides efficient job management and role-based access control. The backend allows users to post jobs, apply for them, and manage applications, while ensuring secure and efficient handling of data. Key features include advanced job search functionality, role-based authentication, image upload support, and comprehensive API documentation using Swagger.

## Project Goals

The primary objectives of this project are to:

- **API Development**: Create APIs for managing job postings, categories, and applications.
- **Access Control**: Implement role-based access control for admins and users.
- **Database Efficiency**: Optimize job search with advanced query indexing.

## Technologies Used

| **Technology** | **Purpose** |
|----------------|------------|
| Django         | High-level Python framework for rapid development |
| PostgreSQL     | Relational database for storing job board data |
| JWT            | Secure role-based authentication |
| Swagger        | API documentation and testing |

## Key Features

- **Job Posting Management**: 
  - APIs for creating, updating, deleting, and retrieving job postings.
  - Categorize jobs by industry, location, and employment type.

- **Role-Based Authentication**:
  - Admins have full control over job postings and categories.
  - Users can apply for jobs and manage their applications.

- **Optimized Job Search**:
  - Implement location-based and category-based filtering.
  - Use query indexing for faster and more responsive searches.

- **Image Upload**:
  - Users can upload job-related images which are stored and can be accessed from URLs.

- **API Documentation**:
  - Detailed Swagger API documentation hosted at `/api/docs` for easy frontend integration.

## Deployment

The backend is deployed on **Render** using **PostgreSQL** as the database.

- API URL: [https://alx-jobboard-api.onrender.com](https://alx-jobboard-api.onrender.com)
- Swagger Documentation: [https://alx-jobboard-api.onrender.com/api/docs/](https://alx-jobboard-api.onrender.com/api/docs/)

## URLs

### Job Posting APIs

- **Create a Job**: `POST /api/jobs/`
- **Retrieve Job**: `GET /api/jobs/{id}/`
- **Update Job**: `PUT /api/jobs/{id}/`
- **Delete Job**: `DELETE /api/jobs/{id}/`

### Application APIs

- **Create an Application**: `POST /api/applications/`
- **Retrieve Application**: `GET /api/applications/{id}/`
- **Update Application**: `PUT /api/applications/{id}/`
- **Delete Application**: `DELETE /api/applications/{id}/`

### User Registration API

- **Register a User**: `POST /api/users/register/`

### Token API

- **Access token**: `POST /api/token/`
- **Refresh token**: `POST /api/refresh/`


### Role-Based Authentication

- Admins can access endpoints for job and application management.
- Regular users can only apply for jobs and manage their applications.

