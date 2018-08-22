"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill
"""

from __future__ import print_function

import json
#import requests
import urllib2
import base64
# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        #'card': {
            'type': 'Simple',
           # 'title': "SessionSpeechlet - " + title,
           # 'content': "SessionSpeechlet - " + output
       # },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def build_speechlet_link_account_needed_response(reprompt_text, should_end_session):
    return {
    "version": "1.0",
    "sessionAttributes": {},
    "response": {
      "outputSpeech": {
        "type": "PlainText",
        "text": reprompt_text 
      },
      "card": {
        "type": "LinkAccount"
      },
      "shouldEndSession": should_end_session
    }
}
    
    
# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    
    if 'accessToken' in session['user']:
        card_title = "Welcome"
        speech_output = "You can control the smart bed with the voice command like head up"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = None
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    else:
        should_end_session = True
        reprompt_text = "You must have a top qizhi account to control a bed. Please use the Alexa app to link your Amazon account with your top qizhi Account." 
        return build_speechlet_link_account_needed_response(reprompt_text, should_end_session)

def help_response(session):
    
    session_attributes = {}
    
    if 'accessToken' in session['user']:
        card_title = "Help"
        speech_output = "you can control your smart bed by say:Alexa ask audio dongle head up"
        # If the user either does not reply to the welcome message or says something
        # that is not understood, they will be prompted again with this text.
        reprompt_text = "you can control your smart bed by say:Alexa ask audio dongle head up"
        should_end_session = False
        return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    else:
        should_end_session = True
        reprompt_text = "You must have a top qizhi account to control a bed. Please use the Alexa app to link your Amazon account with your top qizhi Account." 
        return build_speechlet_link_account_needed_response(reprompt_text, should_end_session)

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Bye bye! Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))
        
def send_request_to_server(deviceId,msg):
    headers = {'Content-Type': 'application/json'}
    #params = {"topic":"umomoSofa","payload":"open sofa","qos":1,"retain":False,"client_id":"C_TEST"}
    params = {"topic":"umomoSofa","payload":msg,"qos":1,"retain":False,"client_id":"C_TEST"}
    data = json.dumps(params)
    print(data)
    base64string = base64.b64encode('%s:%s' % ('iot', 'iotserver'))
    request = urllib2.Request("http://120.27.138.117:18083/api/v2/mqtt/publish", data, headers)
    #request = urllib2.Request("http://120.27.138.117:8081/api/v2/mqtt/publish", data, headers)
    request.add_header("Authorization", "Basic %s" % base64string)   
    response = urllib2.urlopen(request)
    result = response.read()
    print(result)
    
def head_up_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"head up")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))   
        
def head_down_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"head down")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 

def foot_up_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"foot up")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 

def foot_down_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"foot down")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def leg_up_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"leg up")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        

def leg_down_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"leg down")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 

def lumbar_up_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"lumbar up")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def lumbar_down_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"lumbar down")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
   
def stop_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, bye bye!" 
        should_end_session = True
    send_request_to_server(access_token,"stop")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
 
def flat_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"flat")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def antisnore_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"antisnore")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
  
  
  
def lounge_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"lounge")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def lounge_program_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"lounge program")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
 
def zero_gravity_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"zero gravity")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
 
def zero_gravity_program_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"zero gravity program")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def incline_program_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"incline program")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def incline_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"incline")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def massage_on_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"massage on")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 

def wave_one_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"wave one")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
    
    
def wave_two_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"wave two")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
       
def wave_three_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"wave three")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
       
       
def wave_four_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"wave four")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def full_body_one_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"full body one")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def full_body_two_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"full body two")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def massage_up_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"massage up")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))         
    

def massage_down_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"massage down")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def massage_stop_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"massage stop")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
     

def light_on_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"light on")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def light_off_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"light off")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def lights_on_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"lights on")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))      
        

def lights_off_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"lights off")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def toggle_light_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"toggle light")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
       

def toggle_lights_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"toggle lights")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
        
def feedback_on_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?"  
        should_end_session = False
    send_request_to_server(access_token,"feedback on")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
  
def feedback_off_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    access_token = session['user']['accessToken']
    
    #access_token = "abc"
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False
    send_request_to_server(access_token,"feedback off")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session)) 
        
def close_sofa_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    
    access_token = session['user']['accessToken']
    
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False

    send_request_to_server("access_token","close sofa")
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))  
def open_sofa_head_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False

    send_request_to_server("123456","open sofa head")
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))      
def close_sofa_head_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False

    send_request_to_server("123456","close sofa head")
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))   
def stop_sofa_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "Ok, is there anything you'd like me to do?" 
        should_end_session = False

    send_request_to_server("123456","stop sofa")
    
    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
        
def reset_sofa_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    
    access_token = session['user']['accessToken']
    print("access_token");
    print(access_token)
    
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output ="Ok, is there anything you'd like me to do?" 
        should_end_session = False
        
    send_request_to_server("123456","reset sofa")
    
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(session)


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    
    print("==========intent name==============:%r" %(intent_name))
    
    # Dispatch to your skill's intent handlers
    #if intent_name == "MyColorIsIntent":
    #    return set_color_in_session(intent, session)
    #elif intent_name == "WhatsMyColorIntent":
    #    return get_color_from_session(intent, session)
    #el
    if intent_name == "AMAZON.HelpIntent":
        return help_response(session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "headup":
        return head_up_session(intent, session)
    elif intent_name == "headdown":
        return head_down_session(intent, session)
    elif intent_name == "footup":
        return foot_up_session(intent, session)
    elif intent_name == "footdown":
        return foot_down_session(intent, session)
    elif intent_name == "legup":
        return leg_up_session(intent, session)
    elif intent_name == "legdown":
        return leg_down_session(intent, session)
    elif intent_name == "lumbarup":
        return lumbar_up_session(intent, session)
    elif intent_name == "lumbardown":
        return lumbar_down_session(intent, session)
    elif intent_name == "stop":
        return stop_session(intent, session)
    elif intent_name == "flat":
        return flat_session(intent, session)
    elif intent_name == "antisnore":
        return antisnore_session(intent, session)
    elif intent_name == "lounge":
        return lounge_session(intent, session)
    elif intent_name == "zerogravity":
        return zero_gravity_session(intent, session)
    elif intent_name == "incline":
        return incline_session(intent, session)
    elif intent_name == "loungeprogram":
        return lounge_program_session(intent, session)
    elif intent_name == "zerogravityprogram":
        return zero_gravity_program_session(intent, session)
    elif intent_name == "inclineprogram":
        return incline_program_session(intent, session)
    elif intent_name == "massageon":
        return massage_on_session(intent, session)
    elif intent_name == "waveone":
        return wave_one_session(intent, session)
    elif intent_name == "wavetwo":
        return wave_two_session(intent, session)
    elif intent_name == "wavethree":
        return wave_three_session(intent, session)
    elif intent_name == "wavefour":
        return wave_four_session(intent, session)
    elif intent_name == "fullbodyone":
        return full_body_one_session(intent, session)        
    elif intent_name == "fullbodytwo":
        return full_body_two_session(intent, session)
    elif intent_name == "massageup":
        return massage_up_session(intent, session)
    elif intent_name == "massagedown":
        return massage_down_session(intent, session)
    elif intent_name == "massagestop":
        return massage_stop_session(intent, session)
    elif intent_name == "lighton":
        return light_on_session(intent, session)
    elif intent_name == "lightoff":
        return light_off_session(intent, session)
    elif intent_name == "lightson":
        return lights_on_session(intent, session)
    elif intent_name == "lightsoff":
        return lights_off_session(intent, session)
    elif intent_name == "togglelight":
        return toggle_light_session(intent, session)
    elif intent_name == "togglelights":
        return toggle_lights_session(intent, session)
    elif intent_name == "feedbackoff":
        return feedback_off_session(intent, session)
    elif intent_name == "feedbackon":
        return feedback_on_session(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

def need_account_link(intent_request, session):
    """ You should do account link to access this audio dongle skill.
    """

    session_attributes = {}
    card_title = "Account link needed."
    speech_output = "You should do account link to access this audio dongle skill."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "You should do account link to access this audio dongle skill. " 
    should_end_session = True
    #should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    #print("event.session.application.applicationId=" + event['session']['application']['applicationId'])
    
    SS = event['session']
    
    #print(event['session']['user']['accessToken'])
    #if event['session']['user']['accessToken']:
    #   print(event['session']['user']['accessToken'])
    #else:
    #    return need_account_link(event['request'], event['session'])
    #
    print("==================session================")
    print(event['session'])
    print("==================request================")
    print(event['request'])
    #account link check
    
    if 'accessToken' in event['session']['user']:
        print(event['session']['user']['accessToken'])
    else:
        should_end_session = True
        reprompt_text = "You must have a top qizhi account to control a bed. Please use the Alexa app to link your Amazon account with your top qizhi Account." 
        return build_speechlet_link_account_needed_response(reprompt_text, should_end_session)
        
    #print("=================device id=================")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

