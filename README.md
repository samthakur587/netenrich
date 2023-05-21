# Documentation for Api 
Sure! Here's the documentation for all the APIs you provided:

### User Registration

**Endpoint:** `POST /register`

**Description:** Register a new user.

**Parameters:**
- `username` (string): The username of the user.
- `password` (string): The password of the user.

### User Login

**Endpoint:** `POST /login`

**Description:** Log in user by browser verfication this is basic browser based auth api you can login with username and password from which you resister just execute it.

**Parameters:**
- `credentials` (HTTPBasicCredentials): HTTP Basic authentication credentials containing the username and password.

Sure! Here's the documentation for the input you provided:

### Add User Personal Details

**Endpoint:** `POST /register/personal-detail`

**Description:** Add personal details for a registered user.

**Parameters:**
- `data` (UserInputModel): User's personal details.
- `skills` (list): List of user's skills.

#### UserInputModel

- `basic_detail` (object): Basic details of the user.
  - `first_name` (string): The first name of the user.
  - `last_name` (string): The last name of the user.
  - `date_of_birth` (string): The date of birth of the user in the format MM-dd-YYYY.
  - `email_id` (string): The email address of the user.
  - `contect_no` (string): The contact number of the user.
  - `year_joining_tu` (string): The year the user joined the university in the format YYYY.
  - `year_completion_tu` (string): The year the user is expected to complete the university in the format YYYY.
  - `department` (string): The department of the user.
  - `course` (string): The course of the user.
  - `current_sem` (string): The current semester of the user.
  - `bio` (string): A brief introduction or bio of the user.

- `secondary_school` (object): Details of the secondary school education.
  - `school_name` (string): The name of the secondary school.
  - `classes` (string): The class completed in secondary school (e.g., "10th").
  - `percent_cgpa` (string): The percentage or CGPA obtained in secondary school.
  - `passing_year` (string): The year of passing secondary school.
  - `remark` (string): Any additional remarks or notes.

- `high_school` (object): Details of the high school education.
  - `school_name` (string): The name of the high school.
  - `classes` (string): The class completed in high school (e.g., "12th").
  - `percent_cgpa` (string): The percentage or CGPA obtained in high school.
  - `passing_year` (string): The year of passing high school.
  - `remark` (string): Any additional remarks or notes.

- `ug` (object): Details of the undergraduate education.
  - `collage_name` (string): The name of the undergraduate college.
  - `degree` (string): The degree pursued in undergraduate education (e.g., "under graduate").
  - `percent_cgpa` (string): The percentage or CGPA obtained in undergraduate education.
  - `passing_year` (string): The year of passing undergraduate education.
  - `remark` (string): Any additional remarks or notes.

- `pg` (object): Details of the postgraduate education.
  - `collage_name` (string): The name of the postgraduate college.
  - `degree` (string): The degree pursued in postgraduate education (e.g., "post graduate").
  - `percent_cgpa` (string): The percentage or CGPA obtained in postgraduate education.
  - `passing_year` (string): The year of passing postgraduate education.
  - `remark` (string): Any additional remarks or notes.

**Example Request:**
```json
POST /register/personal-detail

{
  "data": {
    "basic_detail": {
      "first_name": "samunder",
      "last_name": "singh",
      "date_of_birth": "MM-dd-YYYY",


      "email_id": "xyz@gmail.com",
      "contect_no": "8741xxxx51",
      "year_joining_tu": "YYYY",
      "year_completion_tu": "YYYY",
      "department": "computer science",
      "course": "b.tech",
      "current_sem": "6",
      "bio": "xyz what you a doing currently a breif introduction of you"
    },
    "secondary_school": {
      "school_name": "string",
      "classes": "10th",
      "percent_cgpa": "string",
      "passing_year": "string",
      "remark": "string"
    },
    "high_school": {
      "school_name": "string",
      "classes": "12th",
      "percent_cgpa": "string",
      "passing_year": "string",
      "remark": "string"
    },
    "ug": {
      "collage_name": "string",
      "degree": "under graduate",
      "percent_cgpa": "string",
      "passing_year": "string",
      "remark": "string"
    },
    "pg": {
      "collage_name": "string",
      "degree": "post graduate",
      "percent_cgpa": "string",
      "passing_year": "string",
      "remark": "string"
    }
  },
  "skills": [
    "string"
  ]
}
```

**Example Response:**
```json
{
  "status": "success",
  "message": "User personal details added successfully."
}
```

Please note that this is a summary of the API documentation. Additional details such as request/response formats and validations may be required.
Sure! Here's the documentation for the `/search` endpoint:

### Search Users

**Endpoint:** `POST /search`

**Description:** Search for users based on various criteria.

**Parameters:**
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.
- `name` (string, optional): Name of the user to search for.
- `semester` (string, optional): Semester of the user to search for.
- `department` (string, optional): Department of the user to search for.
- `program` (string, optional): Program of the user to search for.
- `hostel` (string, optional): Hostel of the user to search for.
- `residence` (string, optional): Residence of the user to search for.
- `skills` (list of strings, optional): List of skills to search for.

**Example Request:**
```json
POST /search

{
  "name": "John Doe",
  "semester": "5",
  "department": "Computer Science",
  "program": "B.Tech",
  "hostel": "cmh",
  "residence": "City of assam",
  "skills": ["Python", "Java"]
}
```

**Example Response:**
```json
{
  "results": [
    {
      "name": "John Doe",
      "semester": "5",
      "department": "Computer Science",
      "program": "B.Tech",
      "hostel": "cmh",
      "residence": "johrat",
      "skills": ["Python", "Java"]
    },
    {
      "name": "Jane Smith",
      "semester": "5",
      "department": "Electrical Engineering",
      "program": "B.Tech",
      "hostel": "pmh",
      "residence": "tezpur",
      "skills": ["C++", "JavaScript"]
    }
  ]
}
```

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and response formats may be required.
Sure! Here's the documentation for the `/autocomplete/{prefix}` endpoint:

### Autocomplete

**Endpoint:** `GET /autocomplete/{prefix}`

**Description:** Get autocomplete suggestions based on a given prefix.

**Parameters:**
- `prefix` (string): The prefix to search for autocomplete suggestions.

**Query Parameters:**
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
GET /autocomplete/jo
```

**Example Response:**
```json
{
  "suggestions": [
    "John",
    "Johnny",
    "Joshua"
  ]
}
```

**Response Schema:**
- `suggestions` (list of strings): The autocomplete suggestions matching the given prefix.

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and response formats may be required.

Here's the documentation for the `/get_user_detail` endpoint:

### Get User Detail

**Endpoint:** `GET /get_user_detail`

**Description:** Get the basic details of a user.

**Query Parameters:**
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
GET /get_user_detail
```

**Example Response:**
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "MM-dd-YYYY",
  "email_id": "john.doe@example.com",
  "contact_no": "1234567890",
  "year_joining_tu": "YYYY",
  "year_completion_tu": "YYYY",
  "department": "Computer Science",
  "course": "B.Tech",
  "current_sem": "6",
  "bio": "A brief introduction about the user."
}
```

**Response Schema:**
- `first_name` (string): The first name of the user.
- `last_name` (string): The last name of the user.
- `date_of_birth` (string): The date of birth of the user in the format "MM-dd-YYYY".
- `email_id` (string): The email ID of the user.
- `contact_no` (string): The contact number of the user.
- `year_joining_tu` (string): The year of joining the university in the format "YYYY".
- `year_completion_tu` (string): The expected year of completion of studies in the university in the format "YYYY".
- `department` (string): The department of the user.
- `course` (string): The course of the user.
- `current_sem` (string): The current semester of the user.
- `bio` (string): A brief introduction about the user.

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and response formats may be required.
Here's the documentation for the `/delete_user` endpoint:

### Delete User

**Endpoint:** `DELETE /delete_user`

**Description:** Delete a user account.

**Query Parameters:**
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
DELETE /delete_user
```

**Example Response:**
```json
{
  "message": "User account deleted successfully"
}
```

**Response Schema:**
- `message` (string): A message indicating that the user account has been deleted successfully.

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.
- `404 Not Found`: Returned if the user account to be deleted is not found.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and error conditions may be required.

Here's the documentation for the `upload_file` function:

### Upload File

**Endpoint:** `POST /upload_file`

**Description:** Upload a file (resume) for a user.

**Request Parameters:**
- `file` (UploadFile, required): The file to be uploaded.
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
POST /upload_file
Content-Type: multipart/form-data

<file content here>
```

**Example Response (200 OK):**
```json
{
  "message": "Document updated successfully"
}
```

**Example Response (404 Not Found):**
```json
{
  "message": "Document not found"
}
```

**Response Schema:**
- `message` (string): A message indicating the result of the file upload operation.

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and error conditions may be required.

Here's the documentation for the `send` function:

### Send Friend Request

**Endpoint:** `POST /send`

**Description:** Send a friend request to another user.

**Request Parameters:**
- `username` (string, required): The username of the user to whom the friend request is being sent.
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
POST /send?username=<username>
Authorization: Basic <base64-encoded-credentials>
```

**Example Response (200 OK):**
```json
{
  "message": "Friend request sent to <username>"
}
```

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.
- `401 Unauthorized`: Returned if the sender and receiver usernames are the same.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and error conditions may be required.

Here's the documentation for the `accept` function:

### Accept Friend Request

**Endpoint:** `POST /accept_request`

**Description:** Accept a friend request from another user.

**Request Parameters:**
- `username` (string, required): The username of the user whose friend request is being accepted.
- `credentials` (HTTPBasicCredentials, optional): Basic authentication credentials.

**Example Request:**
```
POST /accept_request?username=<username>
Authorization: Basic <base64-encoded-credentials>
```

**Example Response (200 OK):**
```json
{
  "message": "You have accepted the friend request from <username>. Your friends are [<list of friends>]"
}
```

**Errors:**
- `401 Unauthorized`: Returned if the provided username or password is invalid.
- `401 Unauthorized`: Returned if the sender and receiver usernames are the same.
- `404 Not Found`: Returned if there is no friend request from the specified user.

Please note that this is a summary of the API documentation. Additional details such as authentication requirements and error conditions may be required.

Here's the documentation for the `check_friend_circle` function:

### Check Friend Circle

**Endpoint:** `POST /friend-circle/{user1}/{user2}`

**Description:** Check if two users belong to the same friend circle based on the given connections.

**Request Parameters:**
- `user1` (string, required): The username of the first user.
- `user2` (string, required): The username of the second user.

**Example Request:**
```
POST /friend-circle/{user1}/{user2}
```

**Example Response (200 OK):**
```json
{
  "result": true
}
```
or
```json
{
  "result": false
}
```

**Errors:**
- None

Please note that this is a summary of the API documentation. Additional details such as input validation and error handling may be required. Also, make sure to provide the correct connections list in the description so that users can check the friend circle correctly.
