# dallas

You can clone my repo to your local and just save the file main.py and user.txt on linpy path.
./main.py will print the duplicated ID with full username lines.

![image](https://user-images.githubusercontent.com/53182424/116794478-e4e68280-aad5-11eb-91e9-4672927d9db4.png)


print the .sh file located under linpd folder by command '#cat dupids.sh' and run first or second way to display duplicated IDs with username in linux one liner by awk.

![image](https://user-images.githubusercontent.com/53182424/116794747-25470000-aad8-11eb-8802-91722f2b7124.png)


### To run and dockerize flask app, we need some prerequisites:
  - Python3.5+ version
  - pip
  - virtualenv
  - Docker, docker-ce


Activate virtual environment after clonning my repo
// I will continue next steps within activated venv directory.
// I had created dallas repository first and clone it in activated environment 
git clone https://github.com/emre-23/dallas.git

Create a folder as in my case mkdir project_2501
cd myproject_2501
python3 -m venv venv
. venv/bin/activate

###My_sql_set-up####
#cd my_sql
#docker-compose -f stack.yml up -d

user:root
passwd: required_password

my_sql![image](https://user-images.githubusercontent.com/53182424/116794415-6be72b00-aad5-11eb-85ed-45d9caa03e91.png)

Setting up two-node cluster on GKE

Ekran Resmi 2021-05-01 23.36.01![image](https://user-images.githubusercontent.com/53182424/116794508-1f501f80-aad6-11eb-91aa-9b641b15e075.png)

As we'd installed Gcloud SDK, we can connect to our cluster via our local terminal as well

#gcloud cloud-shell ssh --authorize-session
To this i've mentioned here some helful gcloud commands:
/*
gcloud auth login

gcloud cloud-shell ssh —authorize-session // Connect to cluster

gcloud config set project deployment-emre1

gcloud source repos clone hello-world --project=deployment-emre1 // clone repo on cloud

gcloud container clusters get-credentials emre-helm --zone us-east1-b --project deployment-emre1

git clone ssh://ygormus173@gmail.com@source.developers.google.com:2022/p/deployment-emre1/r/hello-world


##########ssh to VM#######
gcloud compute config-ssh

ssh ansible-server.us-east1-b.phrasal-descent-309313

*/
Ekran Resmi 2021-05-01 23.40.16![image](https://user-images.githubusercontent.com/53182424/116794595-d3ea4100-aad6-11eb-8c76-c4fed79bbd8e.png)

#cd k8s_files
#kubectl create -f deployment.yml
#kubectl create -f service.yml
#kubectl get deployments, svc

![image](https://user-images.githubusercontent.com/53182424/116794931-ae126b80-aad9-11eb-81b0-65ba9be2f1c0.png)

![image](https://user-images.githubusercontent.com/53182424/116794951-d9955600-aad9-11eb-9db7-c6ceef9b3102.png)

running only 5000 port of your localhost or External IP address of your machine it turns 200 or empty page with /status prefix with 204 code

![image](https://user-images.githubusercontent.com/53182424/116795030-95568580-aada-11eb-9533-9e9a6318c413.png)
You can arrive http://35.184.101.253:5000 or http://35.184.101.253:5000/status or just try;
#export FLASK_APP=hello.py
#flask run on your local.




