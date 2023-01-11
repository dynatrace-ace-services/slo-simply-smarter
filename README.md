# SLO Simply Smarter

## 1) Prerequisite : `Host Group` and `Management Zone` best practices

- [quickstart-ace-configurator](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)

## 2) Create an `APi-Token` with this scope :
 
Prerequisi for BizOps ([detail](https://dynatrace.github.io/BizOpsConfigurator/index.html#prerequisites))  
 - Access problem and event feed, metrics, and topology
 - Read configuration 
 - Write configuration
 - User sessions 
 - Read metrics
 - Write metrics
 - Ingest Metrics  
 
Prerequisi for SLO with monaco ([detail](https://dynatrace-oss.github.io/dynatrace-monitoring-as-code/configuration/configTypes_tokenPermissions))  
 - Read SLO
 - Write SLO
 
  ![image](https://user-images.githubusercontent.com/40337213/210615861-e34ab003-df23-455f-9513-2d1ac63a4759.png)

## 3) Automatic installation and update with `script python3.x`
Prerequisite : requests installed 
 
    pip install requests
 
 2 options :  
 1- Deploy or update SLOs and Dashboards (export Deploy=`ALL` - default value )
 2- Mapping SLO with Dashboards  (export Deploy=`SLO`, no dashboard updating )
 
  
    git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
    cd slo-simply-smarter
     
    export MyTenant=abcd123.live.dynatrace.com for saas or export MyTenant=domaine.com/e/abcd12234 for managed (without https://...) or 
    export MyToken=dt0c01.1234ABCD.XXXX
    export Deploy=ALL(Default)|SLO
    export Owner=MyOwner (optionel - no need to define this user in the UI)
       
    python3 Deploy_and_Update_SLO_Simply_Smarter.py
    
  ![image](https://user-images.githubusercontent.com/40337213/211926417-dcc48062-1e0a-4845-b26d-d6f1b22af44f.png)


# Installation without `Python`
Others option to install `SLO Simply Smarter`if you don't have a runtime python 

---

## 4) `BizOps` : import Dashboard `Dynatrace: Simply Smarter`
 - For Saas and Managed, use the [bizops configurator](https://dynatrace.github.io/BizOpsConfigurator/index.html#begin)  

 
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
 
## 3) `Monaco`Import `SLO template`
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
 With Python3.x : see paragraph Automatic installation with `script python3.x`
 option `Deploy=SLO`

 
