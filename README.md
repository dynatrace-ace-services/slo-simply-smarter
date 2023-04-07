# Dashboarding Dynatrace Simply Smarter

Fundamentals for deployment & configuration : [quickstart-ace-configurator](https://github.com/dynatrace-ace-services/quickstart-ace-configurator#readme)  
ITSM integration & SLO Quality of Service : [itsm-integration-with-slo](https://github.com/dynatrace-ace-services/itsm-integration-with-slo#readme)  
✅ Dashboarding Dynatrace Simply Smarter : [slo-simply-smarter](https://github.com/dynatrace-ace-services/slo-simply-smarter#readme)  

Demo (internal only): [https://demo.live.dynatrace.com](https://demo.live.dynatrace.com/#dashboard;gtf=-2h;gf=all;id=bbbbbbbb-a003-a017-0000-000000000133)

![image](https://user-images.githubusercontent.com/40337213/217482105-8ad929a7-ce7a-4a7e-b0c4-026886851441.png)

---
---

# Installation with `Monaco v2` (recommanded)

## 1) Prerequisites installation

- `Host Group` and `Management Zone` best practices with [Deployment best practices](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)
- `ITSM integration` best practices with [ITSM integration & SLO Quality of Service](https://github.com/dynatrace-ace-services/easy-itsm-integration/blob/main/Readme.md)


## 2) Create an `APi-Token` with this scope :

 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO
 - Access problem and event feed, metrics, and topology


## 3) Deploy with Monaco :

Documentation v2 [here](https://www.dynatrace.com/support/help/manage/configuration-as-code)  
Example for linux 

`installation`  
 
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
    curl -L https://github.com/Dynatrace/dynatrace-configuration-as-code/releases/latest/download/monaco-linux-amd64 -o monaco
    chmod +x monaco
       
`variables`

    export DT_TENANT_URL=https://abcd123.live.dynatrace.com for saas or export MyTenant=https://domaine.com/e/abcd12234 for managed 
    export DT_API_TOKEN=dt0c01.1234ABCD.XXXX
       
`deploy`

    ./monaco deploy manifest.yaml
    
`result`

![image](https://user-images.githubusercontent.com/40337213/230628299-ace2a7f6-1555-4f18-b67d-3f184c83d9d0.png)

---
---
Other installations

# Installation with `Python`

## 1) Create an `APi-Token` with this scope :

 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO

## 2) Automatic installation and update with `python script`
Prerequisite : python with requests installed 
 
    python 3.6+
    pip install requests
    
+ internet acces [dahsboard template](https://github.com/JLLormeau/dynatrace_template_fr) & [slo template](https://github.com/dynatrace-ace-services/slo-simply-smarter/tree/main/SLOSimplySmarter/slo)
+ git clone on local host (linux or windows)
  
Download the script

    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter

`Linux`  
Export variables
     
    export MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...)
    export MyToken=dt0c01.1234ABCD.XXXX
    
Run the script 

    python3 project_python/script/Deploy_and_Update_SLO_Simply_Smarter.py
    
   ![image](https://user-images.githubusercontent.com/40337213/211930107-21d89c32-55fa-4dfb-a36d-6ce6b1182ffb.png)  
  
 The `SLO simply smarter` is installed 
 
 ---
 
If you use windows, 

`windows cmd`  
Export variables
     
    set MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...)
    set MyToken=dt0c01.1234ABCD.XXXX
    
Run the script 

    python Deploy_and_Update_SLO_Simply_Smarter.py
    
`windows powershell`  
Export variables
     
    $env:MyTenant="abcd123.live.dynatrace.com" for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...)
    $env:MyToken="dt0c01.1234ABCD.XXXX"
    
Run the script 

    python Deploy_and_Update_SLO_Simply_Smarter.py

 ---
 
# From Mission Control 
Doesn't work from `Azure Bash`. Works fine from VM host : linux or windows.  

Open the python script and add these two temporary variables `Cookie` & `X-CSRFToken` and run the script (in this case MyTenant=[clusterid]-managed.internal.dynatrace.com:8021/e/[tenantid])  :  
 
    Cookie='xxx'
    CSRFToken='xxx'
    
From the Mission Control, Dev Tools, collect the temporary X-CSRFToken and the full Cookie like that 
![image](https://user-images.githubusercontent.com/40337213/213934116-62c8eb34-241b-44e3-870b-ea7b0a5b47be.png)

and run the `python script` as described above.

---
---

# Installation for `OffLine` environment

1) offline insatallation   
with `python script` and witout Internet access : click [here](https://github.com/JLLormeau/slo_simply_smarter_offline)

2) manual installation  
only if you can't install `SLO Simply Smarter` with python script or with Bizops, follow the process [here](https://github.com/JLLormeau/slo_simply_smarter_offline/blob/main/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)



