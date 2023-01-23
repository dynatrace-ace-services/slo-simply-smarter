#JLL
import json
import requests
import os
import urllib3
import re  

##################################
### Environment Dynatrace
##################################
Tenant="https://"+str(os.getenv('MyTenant'))
Token=os.getenv('MyToken')
Cookie=os.getenv('Cookie')
CSRF=os.getenv('CSRFToken')


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
## Dashboard
##################################
Dashboard_source={'🏠 Dynatrace: simply smarter':'bbbbbbbb-a003-a017-0000-000000000133','✔ SLO Simply Smarter':'bbbbbbbb-a003-a017-0008-000000000133','✔ SLO Resource Optimization':'bbbbbbbb-a003-a017-0009-000000000133','✔ User experience (web applications)':'bbbbbbbb-a003-a017-0002-000000000133','✔ User experience (mobile apps)':'bbbbbbbb-a003-a017-0003-000000000133','✔ Synthetic (browser)':'bbbbbbbb-a003-a017-0004-000000000133','✔ Services':'bbbbbbbb-a003-a017-0001-000000000133','✔ Database services':'bbbbbbbb-a003-a017-0005-000000000133','✔ Synthetic (service)':'bbbbbbbb-a003-a017-0006-000000000133','✔ Infrastructure':'bbbbbbbb-a003-a017-0007-000000000133'}
Dashboard_target={'🏠 Dynatrace: simply smarter':'','✔ SLO Simply Smarter':'','✔ SLO Resource Optimization':'','✔ User experience (web applications)':'','✔ User experience (mobile apps)':'','✔ Synthetic (browser)':'','✔ Services':'','✔ Database services':'','✔ Synthetic (service)':'','✔ Infrastructure':''}
Dashboard_mapping_name={'🏠 Dynatrace: simply smarter':'Dynatrace_simply smarter.json','✔ SLO Simply Smarter':'SLO Simply Smarter.json','✔ SLO Resource Optimization':'SLO Resource Optimization.json','✔ User experience (web applications)':'User experience (web applications).json','✔ User experience (mobile apps)':'User experience (mobile apps).json','✔ Synthetic (browser)':'Synthetic (browser).json','✔ Services':'Services.json','✔ Database services':'Database services.json','✔ Synthetic (service)':'Synthetic (service).json','✔ Infrastructure':'Infrastructure.json'}

##################################
## Others
##################################
deploy=os.getenv('Deploy')
if deploy == None:
    deploy = 'ALL'
owner=os.getenv('Owner')
if owner == None:
    owner = 'admin'
owner_old=''

#disable warning
urllib3.disable_warnings()

# variable changed if script is run on Windows or Linux. "\\" for Windows, "/" for Linux
if Cookie == None:
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
		'Authorization': 'Api-Token {}'.format(dynToken)
    }
else:
    head = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8',
		'Authorization': 'Api-Token {}'.format(Token),
        'X-CSRFToken': CSRF,
        'Cookie': Cookie
    }

##################################
## Generic Dynatrace API
##################################

# generic function GET to call API with a given uri
def queryDynatraceAPI(uri):
    jsonContent = None
    #print(head)
    response = requests.get(uri,headers=head,verify=False)
    #print(response)
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
def getSLO(TENANT, TOKEN):
    for slo_filter in ['smarter', 'optimization']:
        uri=TENANT+APIslo+'?pageSize=100&sloSelector=text("'+slo_filter+'")&sort=name&timeFrame=CURRENT&demo=false&evaluate=false&enabledSlos=true&showGlobalSlos=true'

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

def getDashboard(TENANT, TOKEN):
    global owner
    uri=TENANT+APIdashboard+'?tags=smarter'

    #print(uri)
    datastore = queryDynatraceAPI(uri)
    #print(datastore)
    dashboards = datastore['dashboards']
    for dashboard in dashboards :
        if dashboard['name'] in Dashboard_target:
            if Dashboard_target[dashboard['name']] == '':
                #print(dashboard['name'])
                Dashboard_target[dashboard['name']]=dashboard['id']
        owner_old=dashboard['owner']

    if owner == '' :
        owner == owner_old

    return()


def mappSloDashboard(TENANT, TOKEN):
    print('\nmapping slo')
    uri=TENANT+APIdashboard+'?tags=smarter'

    #print(uri)
    datastore = queryDynatraceAPI(uri)
    #print(datastore)
    dashboards = datastore['dashboards']
    deploy_dash=False
    for dashboard in dashboards :
            if dashboard['name'] in ['✔ SLO Simply Smarter', '✔ SLO Resource Optimization'] :

                uri=TENANT+APIdashboard+'/'+dashboard['id']
                datastore = queryDynatraceAPI(uri)
                #print(datastore)
                data=json.dumps(datastore)
                for i in SLO_source:
                    if SLO_target[i] != '':
                        data=re.sub(SLO_source[i], SLO_target[i], data)

                print(' mapping slo for ', dashboard['name'],dashboard['id'])
                putDynatraceAPI(uri,json.loads(data))
                deploy_dash=True

    if not deploy_dash:
        print(' no dashbaords, import Dynatrace: Simply Smarter or run this script with Deploy=ALL')
    
    return()

def updateSLO(TENANT, TOKEN):
    print('\nupdate slo')
    for slo in SLO_target:
        url='https://raw.githubusercontent.com/dynatrace-ace-services/slo-simply-smarter/main/SLOSimplySmarter/slo/'+slo.replace(' ','')+'.json'
        req = requests.get(url)
        payload=req.json()
        payload['name']=slo
        payload['id']=SLO_target[slo]
        
        print(' update', slo, SLO_target[slo])
        uri=TENANT+APIslo+'/'+SLO_target[slo]
        putDynatraceAPI(uri, payload)


    return()

def generateSLO(TENANT, TOKEN):
    print('\ndeploy slo')
    for slo in SLO_target:
        if SLO_target[slo] == '':
            url='https://raw.githubusercontent.com/dynatrace-ace-services/slo-simply-smarter/main/SLOSimplySmarter/slo/'+slo.replace(' ','')+'.json'
            req = requests.get(url)
            payload=req.json()
            payload['name']=slo
        
            print(' deploy', slo, SLO_target[slo])
            uri=TENANT+APIslo
            result=postDynatraceAPI(uri, payload)

    return()


def generateDashboard(TENANT, TOKEN):
    print('\ndeploy dashboards')
    global owner
    if owner == '' :
        owner = 'admin'

    for dashboard in Dashboard_target:
        if Dashboard_target[dashboard] == '':
            url='https://raw.githubusercontent.com/JLLormeau/dynatrace_template_fr/master/'+Dashboard_mapping_name[dashboard]
            req = requests.get(url)
            payload=req.json()
            payload['dashboardMetadata']['owner']=owner
            del payload['id']
    
            print(' deploy', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard
            result=postDynatraceAPI(uri, payload)
        else:
            url='https://raw.githubusercontent.com/JLLormeau/dynatrace_template_fr/master/'+Dashboard_mapping_name[dashboard]
            req = requests.get(url)
            payload=req.json()
            payload['dashboardMetadata']['owner']=owner
            payload['id']=Dashboard_target[dashboard]
    
            print(' deploy', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            result=putDynatraceAPI(uri, payload)
            
    return()

def mappDashboard(TENANT, TOKEN):
    global owner
    print('\nupdate dashboards')
    for dashboard in Dashboard_target: 
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            datastore = queryDynatraceAPI(uri)
            #print(datastore)
            datastore['dashboardMetadata']['owner']=owner
            data=json.dumps(datastore)
            for i in Dashboard_source:
                if Dashboard_target[i] != '':
                        data=re.sub(Dashboard_source[i], Dashboard_target[i], data)
                        
            print(' update', dashboard, Dashboard_target[dashboard])
            uri=TENANT+APIdashboard+'/'+Dashboard_target[dashboard]
            putDynatraceAPI(uri, json.loads(data))
    print(' => with owner', owner)
            
    return()

##################################
## Main program
##################################
print("######## SLO Simply Smarter automatic deployment ")
print('\nvariables') 
print(' MyTenant', Tenant)
print(' MyToken', 'dt0c01.'+Token.split('.')[1]+'.*****')
print(' Deploy', deploy)
if Cookie != None or CSRF != None :
    print(' Temporary Cookie and CSRFToken from Mission Control')
    print('  Cookie', Cookie)
    print('  X-CSRFToken', CSRF)
if deploy != 'SLO' and deploy != 'slo' :
    print(' Owner', owner)
if Tenant == None :
    print('ERROR : MyTenant is empty')
    exit()
if Token == None :
    print('ERROR : MyToken is empty')
    exit()
if Cookie != None :
    if CSRF == None :
        print('ERROR : CSRFToken is empty')
        exit()
if CSRF != None :
    if Cookie == None :
        print('ERROR : Cookie is empty')
        exit()

#info dashboard
getDashboard(Tenant, Token)

#update dashboards
if deploy != 'SLO' and deploy != 'slo' :
    generateDashboard(Tenant, Token)
    getDashboard(Tenant, Token)
    mappDashboard(Tenant, Token)

#validate slo
getSLO(Tenant, Token)
generateSLO(Tenant, Token)
getSLO(Tenant, Token)

#mapping slo dashboards
mappSloDashboard(Tenant, Token)

#update slo and owner
if deploy != 'SLO' and deploy != 'slo' :
    updateSLO(Tenant, Token)
    

print('\nsimply smarter')
Home=Tenant+"/#dashboard;id="+Dashboard_target['🏠 Dynatrace: simply smarter']
print(' ',Home)
#################################
