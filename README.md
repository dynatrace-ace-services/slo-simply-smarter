# SLO Simply Smarter

## 1) Prerequisite : `Host Group` and `Management Zone` best practices

- [quickstart-ace-configurator](https://github.com/dynatrace-ace-services/quickstart-ace-configurator)

## 2) Create an `APi-Token` with these scope :
 
Prerequisi for BiZops ([detail](https://dynatrace.github.io/BizOpsConfigurator/index.html#prerequisites))  
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


## 2) `BizOpsConfigurator` : import Dashboard `Dynatrace: Simply Smarter`
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
 
## 3) Import `SLO template`
 - Use [monaco](https://dynatrace-oss.github.io/dynatrace-monitoring-as-code/)
 
 `installation`
 
       git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
       cd slo-simply-smarter
       wget https://github.com/dynatrace-oss/dynatrace-monitoring-as-code/releases/latest/download/monaco-linux-amd64
       mv monaco-linux-amd64 monaco
       chmod +x monaco
       
`varaiables`

       export NEW_CLI=1
       export MyTenant=abcd123.live.dynatrace.com (without https://...)
       export MyToken=xxxx1234yyyy1234
       
`deploy`

       ./monaco deploy -e=environments.yaml SLOSimplySmarter
       
 ## 4) Mapp `SLO Simply Smarter` and `SLO Resource Optimization` with SLO Smarter  
 2 options :
 - manually 
 - or automatic
 
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
      

 ## OR automatic mapping with python3.x  
 SLO are uploaded if missing (no need to deploy with monaco) and the mapping between SLO and Dashboard is automatic  
 
      git clone https://github.com/dynatrace-ace-services/slo-simply-smarter
      cd slo-simply-smarter
      
      export MyTenant=abcd123.live.dynatrace.com (without https://...)
      export MyToken=xxxx1234yyyy1234
      python3 Mapping_SLO_Simply_Smarter.py
    
  ![image](https://user-images.githubusercontent.com/40337213/211681761-736ab18d-46ca-4488-9e14-bc8872af4e38.png)

 
 
 

  
