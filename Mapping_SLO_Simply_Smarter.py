#JLL
import json
import requests
import os
import urllib3
import re  

##################################
### Environment saas
##################################
Tenant="https://"+str(os.getenv('MyTenant'))
Token=os.getenv('MyToken')

##################################
## API
##################################
APIdashboard='/api/config/v1/dashboards'
APIslo='/api/v2/slo'

##################################
## SLO
##################################
SLO_source={'Optimization - CPU Usage':'d432ca69-7cb0-3dcf-a176-6225a6d5ff4c','Optimization - Disk Usage':'f73c599d-87ba-38e8-98ff-1dae02879969','Optimization - Memory Usage':'ef700817-f0c2-33f8-916d-8dfeb0f1ce3a','Smarter - Application Performance':'eb99760c-52f6-303b-94eb-4a67d5bf3b32','Smarter - Browser Monitor Availability':'2d23383a-8124-3799-916a-548d307ffbcd','Smarter - Database Performance':'91f1aaee-8e54-37cd-9771-cacd0bc977dc','Smarter - Database Success Rate':'c3b96795-e1db-3e55-806b-c4dbba302094','Smarter - Http Monitor Availability':'7dffcc5b-a736-32da-bf7e-a981205fc9fb','Smarter - Service Availability':'a0a88884-5d41-3425-8f02-37436794da80','Smarter - Service Performance':'811465a3-5b0b-3096-9279-02a3d499ba25'}
SLO_target={'Optimization - CPU Usage':'','Optimization - Disk Usage':'','Optimization - Memory Usage':'','Smarter - Application Performance':'','Smarter - Browser Monitor Availability':'','Smarter - Database Performance':'','Smarter - Database Success Rate':'','Smarter - Http Monitor Availability':'','Smarter - Service Availability':'','Smarter - Service Performance':''}

##################################
## Others
##################################
#disable warning
urllib3.disable_warnings()

# variable changed if script is run on Windows or Linux. "\\" for Windows, "/" for Linux
head = {
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8'
}


##################################
## Generic Dynatrace API
##################################

# generic function GET to call API with a given uri
def queryDynatraceAPI(uri):
    jsonContent = None
    response = requests.get(uri,headers=head,verify=False)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        if(len(response.text) > 0):
            jsonContent = json.loads(response.text)
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if(jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)

#generic function POST to call API with a given uri
def postDynatraceAPI(uri, payload):
    jsonContent = None
    response = requests.post(uri,headers=head,verify=False, json=payload)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        if(len(response.text) > 0):
            jsonContent = json.loads(response.text)
            jsonContent="success"
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if(jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)

#generic function PUT to call API with a given uri
def putDynatraceAPI(uri, payload):
    jsonContent = None
    #print(uri,head,payload)
    response = requests.put(uri,headers=head,verify=False, json=payload)
    # For successful API call, response code will be 200 (OK)
    if(response.ok):
        jsonContent="success"
    else:
        jsonContent = json.loads(response.text)
        print(jsonContent)
        errorMessage = ""
        if (jsonContent["error"]):
            errorMessage = jsonContent["error"]["message"]
            print("Dynatrace API returned an error: " + errorMessage)
        jsonContent = None
        #raise Exception("Error", "Dynatrace API returned an error: " + errorMessage)

    return(jsonContent)
   
##################################
## Get SLO Target
##################################
def getSlo(TENANT, TOKEN):
    for slo_filter in ['smarter', 'optimization']:
        uri=TENANT+APIslo+'?pageSize=100&sloSelector=text("'+slo_filter+'")&sort=name&timeFrame=CURRENT&demo=false&evaluate=false&enabledSlos=true&showGlobalSlos=true&Api-Token='+TOKEN

        #print(uri)
        datastore = queryDynatraceAPI(uri)
        #print(datastore)
        slos = datastore['slo']
        for slo in slos :
            if slo['name'] in SLO_target:
                if SLO_target[slo['name']] == '':
                    #print(slo['name'])
                    SLO_target[slo['name']]=slo['id']
            
    return()


def getdashboard(TENANT, TOKEN):
    uri=TENANT+APIdashboard+'?tags=smarter&Api-Token='+TOKEN

    #print(uri)
    datastore = queryDynatraceAPI(uri)
    #print(datastore)
    dashboards = datastore['dashboards']
    print('update dashbaord')
    deploy_dash=False
    for dashboard in dashboards :
            if dashboard['name'] in ['✔ SLO Simply Smarter', '✔ SLO Resource Optimization'] :

                uri=TENANT+APIdashboard+'/'+dashboard['id']+'?Api-Token='+TOKEN
                datastore = queryDynatraceAPI(uri)
                #print(datastore)
                data=json.dumps(datastore)
                for i in SLO_source:
                    if SLO_target[i] != '':
                        data=re.sub(SLO_source[i], SLO_target[i], data)

                print(dashboard['name'],dashboard['id'])
                putDynatraceAPI(uri,json.loads(data))
                deploy_dash=True

    if not deploy_dash:
        print('no dashbaords, import Dynatrace: Simply Smarter')

    return()


def generateSLO(TENANT, TOKEN):
    for slo in SLO_target:
        if SLO_target[slo] == '':
            url='https://raw.githubusercontent.com/dynatrace-ace-services/slo-simply-smarter/main/SLOSimplySmarter/slo/'+slo.replace(' ','')+'.json'
            req = requests.get(url)
            payload=req.json()
            payload['name']=slo
        
            print('deploy', slo)
            uri=TENANT+APIslo+'?Api-Token='+TOKEN
            result=postDynatraceAPI(uri, payload)
            
    return()

##################################
## Main program
##################################
getSlo(Tenant, Token)
generateSLO(Tenant, Token)
getSlo(Tenant, Token)
getdashboard(Tenant, Token)


#################################
