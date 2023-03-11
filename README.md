# Dashboarding Dynatrace Simply Smarter

Foundations for deployment & configuration : [quickstart-ace-configurator](https://github.com/dynatrace-ace-services/quickstart-ace-configurator#readme)  
ITSM integration & SLO Quality of Service : [easy-itsm-integration](https://github.com/dynatrace-ace-services/easy-itsm-integration#readme)  
✅ Dashboarding Dynatrace Simply Smarter : [slo-simply-smarter](https://github.com/dynatrace-ace-services/slo-simply-smarter#readme)  

Demo (internal only): [https://demo.live.dynatrace.com](https://demo.live.dynatrace.com/#dashboard;gtf=-2h;gf=all;id=bbbbbbbb-a003-a017-0000-000000000133)

![image](https://user-images.githubusercontent.com/40337213/217482105-8ad929a7-ce7a-4a7e-b0c4-026886851441.png)


## 1) Prerequisites installation

- `Host Group` and `Management Zone` best practices with [Deployment best practices](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)
- `ITSM integration` best practices with [Easy ITSM integration](https://github.com/dynatrace-ace-services/easy-itsm-integration/blob/main/Readme.md)

## 2) Create an `APi-Token` with this scope :

 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO

## 3) Automatic installation and update with `python script`
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
    
Optional variables

    export Deploy=ALL|SLO (default Deploy=ALL, Deploy=SLO option does not deploy the dashboards but only creates the mapping SLO with already imported dashboards)
    export Owner=ACE (default Owner=smarter, the owner don't need to exist as user)
    
Run the script 

    python3 Deploy_and_Update_SLO_Simply_Smarter.py
    
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

# Installation without `Python`
If you can't install `SLO Simply Smarter` with python script, you can follow this workflow installaton which uses Bizops and Monaco

## 1) Create an `APi-Token` with this scope :

 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO
 - Access problem and event feed, metrics, and topology (*)
 - User sessions(*)
 - Read metrics(*)
 - Write metrics(*)
 - Ingest Metrics(*) 
   
  ![image](https://user-images.githubusercontent.com/40337213/210615861-e34ab003-df23-455f-9513-2d1ac63a4759.png)  
  (*) token used by BizOpsConfigurator ([detail](https://dynatrace.github.io/BizOpsConfigurator/index.html#prerequisites))  

## 2) `BizOps` : import Dashboard `Dynatrace: Simply Smarter`
For Saas and Managed, with the [bizops configurator](https://dynatrace.github.io/BizOpsConfigurator/index.html#begin)  

 
    https://dynatrace.github.io/BizOpsConfigurator/index.html#begin
    use your *tenant** and **token** (don't care with Source)
    connect
    deploy 
    .../ALL
    Dynatrace_Simply Smarter
    next
    advanced (you can define the owenr = smarter)
    done
       
 
 ![image](https://user-images.githubusercontent.com/40337213/210232428-7de19b44-579a-4979-9e4e-6b9ef61bcc7a.png)  
 - For OffLine environment, follow the process [here](/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)
 
## 3) `Monaco`Import `SLO template`
 - Use [monaco](https://dynatrace-oss.github.io/dynatrace-monitoring-as-code/)
 
 `installation`
 
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
    curl -L https://github.com/dynatrace/dynatrace-configuration-as-code/releases/download/v1.8.9/monaco-linux-386 -o monaco
    chmod +x monaco
       
`varaiables`

    export NEW_CLI=1
    export MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...) or 
    export MyToken=dt0c01.1234ABCD.XXXX
       
`deploy`

    ./monaco deploy -e=environments.yaml SLOSimplySmarter
       
 ## 4) Mapp `SLO Simply Smarter` and `SLO Resource Optimization` with SLO Smarter  
 
 # Manually mapping
 
 `SLO Simply Smarter`: for each SLO tile, mapp SLO Smarter and period  
 Set the period -1M and -1y manually for all the SLOs (by default -1w)  
 
 `Application`
 
    Smarter - Application Performance => 1w, 1M and 1y
    Smarter - Browser Monitor Availability => 1w, 1M and 1y
    Smarter - HTTP Monitor Availability => 1w, 1M and 1y
    
`Webservice and Webrequest`
 
    Smarter - Service Performance => 1w, 1M and 1y
    Smarter - Service Availability => 1w, 1M and 1y
 
`Database`
 
    Smarter - Database Performance => 1w, 1M and 1y
    Smarter - Database Success Rate => 1w, 1M and 1y
       
![image](https://user-images.githubusercontent.com/40337213/210246167-71c63329-11f5-4f0b-9ba9-98c4485be86b.png)  

`SLO Resource Optimization` : for each SLO tile, mapp SLO Smarter and period  

`Memory`

    Optimization - Memory Usage => 1w, 1M and 1y
    
`CPU`

    Optimization - CPU Usage => 1w, 1M and 1y
    
`Disk`

    Optimization - Disk Usage => 1w, 1M and 1y    

![image](https://user-images.githubusercontent.com/40337213/210247317-06d3a1dd-331c-44ca-9c41-cc3d08249a2c.png)
      
  
 ## Automatic mapping  
 With Python - : see paragraph Automatic installation with `python script`
 with this variable: 
 
    export Deploy=SLO

---
---

# Installation  for `OffLine` environment

1) offline insatallation   
with `python script` and witout Internet access : click [here](https://github.com/JLLormeau/slo_simply_smarter_offline)

2) manual installation  
only if you can't install `SLO Simply Smarter` with python script or with Bizops, follow the process [here](https://github.com/JLLormeau/slo_simply_smarter_offline/blob/main/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)



