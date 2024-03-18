from speedrun.db import db 
from dataclasses import dataclass 
from speedrun.implant_pb2 import * 


@dataclass
class Implant(db.Model):
    id =  db.Column(db.Integer, primary_key = True)
    implant_guid = db.Column(db.String)
    username = db.Column(db.String)
    hostname = db.Column(db.String)

def make_implant_from_reqquest(r : Register):
    # TODO make sure it s all valid 
    return Implant(
            implant_guid = r.GUID, 
            username = r.Username, 
            hostname = r.Hostname,
            )

opcodes = {
        "exec": 1
        }



STATUS_CREATED  = "created"
STATUS_TASKED = "tasked" # the implant pulled down the task 
STATUS_OK = "ok" # the implant succesfull completed the task 
STATUS_FAIL = "fail" # implant did not complete the task 

import os 
def make_task_id():
    return os.urandom(16).hex()

# TODO NOT NULL most of these 
@dataclass 
class Task(db.Model):
    id: int  =  db.Column(db.Integer, primary_key = True)
    task_id: str = db.Column(db.String)
    status: str = db.Column(db.String)
    implant_id:int   = db.Column(db.Integer)
    task_opcode:str  = db.Column(db.String)
    task_args:str  = db.Column(db.String)

def make_task( implant_id, task_opcode, task_args):
    return Task(
            task_id=make_task_id(), 
            status = STATUS_CREATED, 
            implant_id = implant_id, 
            task_args  = task_args
            )
    

def make_implant(implant_id, username, hostname):
    im = Implant(
            implant_guid=implant_id, username=username, hostname=hostnmae,
        )
    return im 
