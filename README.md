# dallas

You can clone my repo to your local and just save the file main.py and user.txt on linpy path.
./main.py will print the duplicated ID with full username lines.

![image](https://user-images.githubusercontent.com/53182424/116794478-e4e68280-aad5-11eb-91e9-4672927d9db4.png)


print the .sh file located under linpd folder by command '#cat dupids.sh' and run first or second way to display duplicated IDs with username in linux one liner by awk.


### To run and docckerize flask app, we need some prerequsities:
  - Python3.5+ version
  - pip
  - virtualenv


#activate virtual environment after clonning my repo
// I will continue next steps within activated venv directory.
// I had created dallas repository first and clone it in activated environment 
git clone https://github.com/emre-23/dallas.git

Create a folder as in my case mkdir project_2501
cd myproject_2501
python3 -m venv venv
. venv/bin/activate

###My_sql_set-up
cd my_sql
docker-compose -f stack.yml up -d

my_sql![image](https://user-images.githubusercontent.com/53182424/116794415-6be72b00-aad5-11eb-85ed-45d9caa03e91.png)

Setting up two-node cluster on GKE

Ekran Resmi 2021-05-01 23.36.01![image](https://user-images.githubusercontent.com/53182424/116794508-1f501f80-aad6-11eb-91aa-9b641b15e075.png)





