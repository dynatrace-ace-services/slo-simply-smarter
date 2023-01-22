# SLO Simply Smarter

Deployment best practices : https://github.com/dynatrace-ace-services/quickstart-ace-configurator#readme  
Easy ITSM integration : https://github.com/dynatrace-ace-services/easy-itsm-integration#readme  
✅ Install SLO Simply Smarter : https://github.com/dynatrace-ace-services/slo-simply-smarter#readme  

## 1) Prerequisites

- `Host Group` and `Management Zone` best practices with [deployment best practices](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)
- `ITSM integration` best practices with [easy ITSM integration](https://github.com/dynatrace-ace-services/easy-itsm-integration/blob/main/Readme.md)

## 2) Create an `APi-Token` with this scope :

 - Access problem and event feed, metrics, and topology
 - Read configuration 
 - Write configuration
 - Read SLO
 - Write SLO
 - User sessions(*)
 - Read metrics(*)
 - Write metrics(*)
 - Ingest Metrics(*) 
   
  ![image](https://user-images.githubusercontent.com/40337213/210615861-e34ab003-df23-455f-9513-2d1ac63a4759.png)  
  (*) optionnel for BizOps only ([detail](https://dynatrace.github.io/BizOpsConfigurator/index.html#prerequisites))  

  
## 3) Automatic installation and update with `script python`
Prerequisite : requests installed 
 
    python 3.6+
    pip install requests
 
 2 options :  
 - Deploy or update SLOs and Dashboards : export Deploy=`ALL` (default value, full update )  
 - Mapping SLO with Dashboards : export Deploy=`SLO` (only mapping, dashboard and slos are not updated )  
 
 You can use this script if you want install or update `SLO Simply Smarter`.  
 Have a look to the update [here](https://github.com/JLLormeau/dynatrace_template_fr#readme)
  
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
     
    export MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...)
    export MyToken=dt0c01.1234ABCD.XXXX
    export Deploy=ALL(Default)|SLO
    export Owner=MyOwner (optionel - no need to define this user in the UI)
       
    python3 Deploy_and_Update_SLO_Simply_Smarter.py
    
   ![image](https://user-images.githubusercontent.com/40337213/211930107-21d89c32-55fa-4dfb-a36d-6ce6b1182ffb.png)  
  
 The `SLO simply smarter` is installed 
 
---

# Installation without `Python`
If you can't install `SLO Simply Smarter` with python script, you can follow this workflow installaton which uses Bizops and Monaco

## step1) `BizOps` : import Dashboard `Dynatrace: Simply Smarter`
For Saas and Managed, with the [bizops configurator](https://dynatrace.github.io/BizOpsConfigurator/index.html#begin)  

 
    https://dynatrace.github.io/BizOpsConfigurator/index.html#begin
    use your *tenant** and **token** (don't care with Source)
    connect
    deploy 
    .../ALL
    Dynatrace_Simply Smarter
    next
    advanced (you can define the owenr = admin)
    done
       
 
 ![image](https://user-images.githubusercontent.com/40337213/210232428-7de19b44-579a-4979-9e4e-6b9ef61bcc7a.png)  
 - For OffLine environment, follow the process [here](/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)
 
## step2) `Monaco`Import `SLO template`
 - Use [monaco](https://dynatrace-oss.github.io/dynatrace-monitoring-as-code/)
 
 `installation`
 
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
    wget https://github.com/dynatrace-oss/dynatrace-monitoring-as-code/releases/latest/download/monaco-linux-amd64
    mv monaco-linux-amd64 monaco
    chmod +x monaco
       
`varaiables`

    export NEW_CLI=1
    export MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...) or 
    export MyToken=dt0c01.1234ABCD.XXXX
       
`deploy`

    ./monaco deploy -e=environments.yaml SLOSimplySmarter
       
 ## step3) Mapp `SLO Simply Smarter` and `SLO Resource Optimization` with SLO Smarter  
 
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
 With Python : see paragraph Automatic installation with `script python`
 option `Deploy=SLO`


---

# Installation manually for `OffLine` environment
If you can't install `SLO Simply Smarter` with python script or with Bizops, follow the process [here](/Import_Dynatrace_Simply_Smarter_for_OffLine_environment.pdf)
 
