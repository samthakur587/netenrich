from fastapi import FastAPI, HTTPException, Depends, File, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pymongo import MongoClient
from enum import Enum
from fastapi import FastAPI, Query
import pandas as pd
import os
import re
from typing import List,Dict,Union,Tuple
from pydantic import BaseModel
security = HTTPBasic()
app = FastAPI()
client = MongoClient('mongodb+srv://singhsamunder270:samunder123@firstdb.5ntyfd9.mongodb.net/?retryWrites=true&w=majority')
db = client["net"]
users_collection = db["signup"]
collection = db["test"]
class Hostel(str, Enum):
    CMH = 'cmh'
    PMH = 'pmh'
    NMH = 'nmh'
    KMH = 'kmh'
    NWH = 'nwh'
    JWH = 'jwh'
    BWH = 'bwh'
    PWH = 'pwh'
    KWH = 'kwh'
    SWH = 'swh'
    TMH = 'tmh'
    MWH = 'mwh'
class Distric(str, Enum):
    JORHAT = 'jorhat'
    BARPETA = 'barpeta'
    CACHAR = 'cachar'
    CHIRANG = 'chirang'
    DHEMAJI = 'dhemaji'
    DIBRUGARH = 'dibrugarh'
    GOALPARA = 'goalpara'
    HAILAKANDI = 'hailakandi'
    KAMRUP_METROPOLITAN = 'kamrup metropolitan'
    KARBI_ANGLONG = 'karbi anglong'
    KOKRAJHAR = 'kokrajhar'
    MAJULI = 'majuli'
    NAGAON = 'nagaon'
    SIVASAGAR = 'sivasagar'
    SOUTH_SALMARA_MANKACHAR = 'south salmara-mankachar'
    UDALGURI = 'udalguri'
    BAKSA = 'baksa'
    BONGAIGAON = 'bongaigaon'
    CHARAIDEO = 'charaideo'
    DARRANG = 'darrang'
    DHUBRI = 'dhubri'
    DIMA_HASAO = 'dima hasao'
    GOLAGHAT = 'golaghat'
    KAMRUP = 'kamrup'
    KARIMGANJ = 'karimganj'
    LAKHIMPUR = 'lakhimpur'
    MORIGAON = 'morigaon'
    NALBARI = 'nalbari'
    SONITPUR = 'sonitpur'
    TINSUKIA = 'tinsukia'
    WEST_KARBI_ANGLONG = 'west karbi anglong'
class search_type(str,Enum):
    name = 'First Name',
    place = 'Place of Residence',
    semester = 'Current Semester',
    department = 'Department',
    program = 'Course',
    hostel = 'hostel',
    skills = 'skills'
tu_hostel = ['cmh', 'pmh', 'nmh', 'kmh', 'nwh', 'jwh', 'bwh', 'pwh', 'kwh', 'swh', 'tmh', 'mwh']
distric = ['Jorhat', 'Barpeta', 'Cachar', 'Chirang', 'Dhemaji', 'Dibrugarh', 'Goalpara', 'Hailakandi',
           'Kamrup Metropolitan', 'Karbi Anglong', 'Kokrajhar', 'Majuli', 'Nagaon', 'Sivasagar',
           'South Salmara-Mankachar', 'Udalguri', 'Baksa', 'Bongaigaon', 'Charaideo', 'Darrang',
           'Dhubri', 'Dima Hasao', 'Golaghat', 'Kamrup', 'Karimganj', 'Lakhimpur', 'Morigaon',
           'Nalbari', 'Sonitpur', 'Tinsukia', 'West Karbi Anglong']

class User(BaseModel):
    first_name: str 
    last_name : str 
    date_of_birth : str
    email_id : str 
    contect_no : str 
    year_joining_tu:str
    year_completion_tu:str 
    department: str 
    course:str 
    current_sem:str 
    bio:str 
    class Config:
        schema_extra = {
            "example": {
                "first_name": "samunder",
                "last_name": "singh",
                "date_of_birth": "MM-dd-YYYY",
                "email_id": "xyz@gmail.com",
                "contect_no": "8741xxxx51",
                "year_joining_tu": 'YYYY' ,
                "year_completion_tu":'YYYY',
                "department":'computer science',
                "course":'b.tech',
                "current_sem":'6',
                "bio":'xyz what you a doing currently a breif introduction of you'
            }
        }

class secondary_school(BaseModel):
    school_name : str or None = None
    classes : str = '10th'
    percent_cgpa:str or None = None
    passing_year: str or None=None 
    remark:str or None = None
class high_school(BaseModel):
    school_name : str or None = None
    classes : str = '12th'
    percent_cgpa:str or None = None
    passing_year: str or None=None 
    remark:str or None = None
class ug(BaseModel):
    collage_name : str or None = None
    degree : str = 'under graduate'
    percent_cgpa:str or None = None
    passing_year: str or None=None 
    remark:str or None = None
class pg(BaseModel):
    collage_name : str or None = None
    degree : str = 'post graduate'
    percent_cgpa:str or None = None
    passing_year: str or None=None 
    remark:str or None = None
class UserInputModel(BaseModel):
    basic_detail:Union[User,None]
    secondary_school: Union[secondary_school, None]
    high_school: Union[high_school, None]
    ug: Union[ug, None]
    pg: Union[pg, None]
class skills(BaseModel):
    skills: str or None = None 
class intership(BaseModel):
    internship_comapny : str
    position : str
    start_date: str
    end_date : str
# User register
@app.post("/register")
async def register(username: str, password: str):
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")
    p = re.compile(regex)
    
    if (password == None):
        raise HTTPException(status_code=400, detail="Please enter any charector in password string.")
    elif not (re.search(p, password)):
       raise HTTPException(status_code=400, detail="Use atleast one upercase one lower case one spacial charector and a number.") 
    elif users_collection.find_one({"username": username}):
        raise HTTPException(status_code=400, detail="Username already exists.")
    elif len(list(password))<8:
        raise HTTPException(status_code=400, detail="please enter the password with atleast 8 charectore.")
    else:
        user = {"username": username, "password": password}
        users_collection.insert_one(user)
    return {"message": "User registered successfully."}

# User login
@app.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = users_collection.find_one({"username": credentials.username})
    if not user or user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    
    return {"message": "Login successful."}
@app.post("/register/personal-detail")
async def add_detailes(data:UserInputModel,skills: list[str],credentials: HTTPBasicCredentials = Depends(security),hostel: Hostel = Query(..., title="Hostel",description="the name of hostel where you currently staying"),distric: Distric = Query(..., title="Distric",description="choose the place of residence from given")):
    
    username = users_collection.find_one({"username": credentials.username, "password": credentials.password})
    if not username:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    user = {'First Name':data.basic_detail.first_name,'Last Name':data.basic_detail.last_name,
                'Date of birth':data.basic_detail.date_of_birth,'Email':data.basic_detail.email_id,
                'contect No.':data.basic_detail.contect_no,'Course':data.basic_detail.course,'Department':data.basic_detail.department,
                'Current Semester':data.basic_detail.current_sem,'Year Of Addmission':data.basic_detail.year_joining_tu,
                'Year of Passing':data.basic_detail.year_completion_tu,'Bio':data.basic_detail.bio,'Place of Residence':distric,'hostel':hostel}

    secondary_school = {'school name':data.secondary_school.school_name,'class':data.secondary_school.classes,
                                'percent/cgpa':data.secondary_school.percent_cgpa,'passing year':data.secondary_school.passing_year,
                                'remark':data.secondary_school.remark}

    high_school = {'school name':data.high_school.school_name,'class':data.high_school.classes,
                                'percent/cgpa':data.high_school.percent_cgpa,'passing year':data.high_school.passing_year,
                                'remark':data.high_school.remark}
    ug = {'collage name':data.ug.collage_name,'degree':data.ug.degree,'cgpa':data.ug.percent_cgpa,'passing year':data.ug.passing_year,
              'remark':data.ug.remark}
    
    pg = {'collage name':data.pg.collage_name,'degree':data.pg.degree,'cgpa':data.pg.percent_cgpa,'passing year':data.pg.passing_year,
              'remark':data.pg.remark}
    key = credentials.username
    userdata = {'username':credentials.username,'basic_detail':user,'education':{'secondary_sch':secondary_school,'high_sch':high_school,'ug':ug,'pg':pg},'skills':skills,'send_request':list[str],'recv_request':list[str]}
    collection.insert_one(userdata)
    return {"message":f"added succesfully {key}"}
def search_users(
    name: str = None,
    semester: str = None,
    department: str = None,
    program: str = None,
    hostel: str = None,
    residence: str = None,
    skills: List[str] = None,
):
    docs = []
    result = collection.find({})
    for doc in result:
        if name:
            if name == doc['basic_detail']['First Name']:
                docs.append(doc['username'])
        if semester:
            if semester == doc['basic_detail']['Current Semester']:
                docs.append(doc['username'])
        if department:
            if department == doc['basic_detail']['Department']:
                docs.append(doc['username'])
        if program:
            if program == doc['basic_detail']['Course']:
                docs.append(doc['username'])
        if hostel:
            if hostel == doc['basic_detail']['hostel']:
                docs.append(doc['username'])
        if residence:
            if residence == doc['basic_detail']['Place of Residence']:
                docs.append(doc['username'])
        if skills:
            if any(element in skills for element in doc['skills']):
                docs.append(doc['username'])
    return {"found":docs}

# Endpoint for searching users
@app.post("/search")
def search_users_endpoint(credentials: HTTPBasicCredentials = Depends(security),
    name: str  = None,
    semester: str = None,
    department: str = None,
    program: str  = None,
    hostel: str = None,
    residence: str  = None,
    skills: List[str]  =  None,
):
    return search_users(
        name=name,
        semester=semester,
        department=department,
        program=program,
        hostel=hostel,
        residence=residence,
        skills=skills,
    )



@app.get("/autocomplete/{prefix}")
def autocomplete(prefix: str,credentials: HTTPBasicCredentials = Depends(security)):
    username = users_collection.find_one({"username": credentials.username, "password": credentials.password})
    if not username:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    user = users_collection.find({})
    user_names = [doc['username'] for doc in user ]
    suggestions = [name for name in user_names if name.startswith(prefix)]
    return {"suggestions": suggestions}

@app.get("/get_user_detail")
def get_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = users_collection.find_one({"username": credentials.username, "password": credentials.password})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    username = credentials.username
    query = {'username':username}  # Empty query retrieves all documents
    result = collection.find(query)
    for doc in result:
        data = doc
    return data['basic_detail']
@app.delete("/delete_user")
def delete_user(credentials: HTTPBasicCredentials = Depends(security)):

    result = users_collection.delete_one({"username": credentials.username, "password": credentials.password})
    info_data = {'username':credentials.username}
    result = collection.delete_many(info_data)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found.")
    return {"message": "User account deleted successfully"}
@app.post("/upload")
async def upload_file(file: UploadFile = File(...),credentials: HTTPBasicCredentials = Depends(security)):
    contents = await file.read()
    Query = {'username':credentials.username}
    existing_document = collection.find_one(Query)
    if existing_document:
        # Update the document with the new key and value
        existing_document['resume'] = contents
        collection.update_one(Query, {"$set": existing_document})
        return {"message": "Document updated successfully"}
    else:
        return {"message": "Document not found"}
friends = {}
friends['samunder']= {'send':[],'recv':[],'accept':[]}
friends['raja'] = {'send':[],'recv':[],'accept':[]}
friends['abhishek'] = {'send':[],'recv':[],'accept':[]}
friends['rohit'] = {'send':[],'recv':[],'accept':[]}
@app.post("/send_request",description=f"initially you dont have any friend check this api first login by anther accunt and send you(with username) a friend request and then login your account and call accept request api then you will see your friend")
def send(username :str ,credentials: HTTPBasicCredentials = Depends(security)):
    user = users_collection.find_one({"username": credentials.username, "password": credentials.password})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    if username == credentials.username:
        raise HTTPException(status_code=401, detail="sander and reciver both are same.")
    if username not in list(friends.keys()):
        friends[username]= {'send':[],'recv':[],'accept':[]}
    if credentials.username not in list(friends.keys()):
        friends[credentials.username]= {'send':[],'recv':[],'accept':[]}
    sendlist = friends[username]['recv']
    sendlist.append(credentials.username)
    return {"message":f"sended the request to {username} {friends[username]}"}
@app.post("/accept_request",description="this api depends on send request api first send yourself a friend request")
def accept(username :str ,credentials: HTTPBasicCredentials = Depends(security)):
    user = users_collection.find_one({"username": credentials.username, "password": credentials.password})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    if username == credentials.username:
        raise HTTPException(status_code=401, detail="sander and reciver both are same.")
    if username not in list(friends.keys()):
        friends[username]= {'send':[],'recv':[],'accept':[]}
    if credentials.username not in list(friends.keys()):
        friends[credentials.username]= {'send':[],'recv':[],'accept':[]}
    recvlist = friends[credentials.username]['recv']
    if username in recvlist:
        acceptlist = friends[credentials.username]['accept']
        acceptlist.append(username)
    else:
        return{"message":f"you dont have friend request by {username}"}
    return {"message":f"you accepted the {username} friend request and your friends are {friends[credentials.username]['accept']}"}

connections = [('a', 'b'), ('b', 'c'), ('d', 'e'),('b','k'),('c','d'),('q','m')]

def check_same_friend_circle(connections: List[Tuple[str, str]], user1: str, user2: str ) -> bool:
    graph = {}

    for connection in connections:
        user_a, user_b = connection
        user_a = user_a.lower()
        user_b = user_b.lower()
        if user_a not in graph:
            graph[user_a] = []
        if user_b not in graph:
            graph[user_b] = []
        graph[user_a].append(user_b)
        graph[user_b].append(user_a)
    
    def dfs(user: str, visited: set) -> bool:
        visited.add(user)
        if user in graph:
            for friend in graph[user]:
                if friend == user2:
                    return True
                if friend not in visited:
                    if dfs(friend, visited):
                        return True
        return False
    
    return dfs(user1, set())

@app.post("/friend-circle/{user1}/{user2}",description=f"please check the connections before input so you get right answer {connections}")
def check_friend_circle(user1: str, user2: str):
    result = check_same_friend_circle(connections, user1, user2)
    return {"result": result}
   
    