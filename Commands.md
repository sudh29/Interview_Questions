[11:08 AM] Sudhanshu Chaudhary
commands
[11:08 AM] Sudhanshu Chaudhary
tar -xzf .\frm5.tar.gz     -------- windows
[11:09 AM] Sudhanshu Chaudhary
find . -name '*.pyc' -type f -delete
cd /home/intucell/son5/src/openson/apps/
 
tar -czvf ides.tar.gz ides/
[11:09 AM] Sudhanshu Chaudhary
screen -ls
screen -S name
crtl+A+C---------create
crtl+A+W---------watch
crtl+A+P---------previous
crtl+A+d---------deattach
screen -r 23564.pts-3.hclson-dev-app-123 ------attach
screen -x 23564.pts-3.hclson-dev-app-123 ------attach already attach screen
screen -XS <PID ya screen ka name> quit
[11:10 AM] Sudhanshu Chaudhary
sudo chmod -R ugo+rwX .
sudo chown -R intucell:intucell *
sudo chown -R hclson:hclson *
[11:10 AM] Sudhanshu Chaudhary
grep -irn "import pdb" *
 
find . -name path_resolver.pyc
[11:11 AM] Sudhanshu Chaudhary
__________________________ Log to file  __________________________________________
 
gzip -d file
unzip file
 
sed -n '2111135,2113452' log_000
 
awk 'NR>=2111135 && NR<=2113452' log_000 |
 
head -2113452 log_000 | tail +2111135
 
awk 'NR>=2111135 && NR<=2113452' log_000 >> /home/intucell/result.txt
 
awk 'NR>=3653' apps.appmanager-NFL-VTC1FFA_NFL_006.log
 
grep -irn "_create_rf_relations:INFO]" result.txt >> /home/intucell/result1.txt
 
grep -irn "validating mos values against db values for cell"  result.txt >> /home/intucell/result2.txt
 
grep -irn "7f34d05d82d0"  log_command >> /home/intucell/commander1.txt
 
grep -irn "create" d2022_07_29_t12_09_04_2111f6d20f3711edbfd7c7b1168f9f44.xml
 
[11:12 AM] Sudhanshu Chaudhary
------------------------SCP---------------------------------
 
scp mo_mappings.py intucell@10.233.194.248:/intucell/latest/lib/python2.7/site-packages/son.infra-212.0.0-py2.7.egg/son/infra/store
[11:12 AM] Sudhanshu Chaudhary
################### mongo ##############################
 
check mogo version--- /intucell/packages/ tab tab
 
/intucell/packages/mongodb-4.4.11/bin/mongo --port=5022 --username=service -p service --authenticationDatabase=admin
 
db.getCollection('action_set_report').find({"changes.object_name":"18L114681"})
db.getCollection('oss_change').find({"oss_change.app_name":"cicol"})
db.getCollection('action_set').find({"app_data.trigger_cell_ids":{$in:["NLAHM1ENM01_a15fc0507a547f97"]}})
db.getCollection('oss_change_tracking').find({"last_commander_change.app_name":"cicol"})
db.getCollection('app_settings').find({"_id" : ObjectId("6107d00de9e0ed41af0a959b")})
db.getCollection('rtu').find({"_id" : "NLAHM1ENM01_SubNetwork=Utran1,SubNetwork=LTE,MeContext=rbsL11468A,ManagedElement=rbsL11468A,vsDataEquipment=1,vsDataAntennaUnitGroup=Sector11,vsDataAntennaNearUnit=1,vsDataRetSubUnit=1"})
 
 
 
nc_id :362528, start_time :{$gte:ISODate("2023-04-19"),$lt:ISODate("2023-04-21")}
[11:12 AM] Sudhanshu Chaudhary
#################### Linux ###################
ps -aef
kill -p pid
[11:12 AM] Sudhanshu Chaudhary
git stash save
git pull
git fetch -all
git add
git commit --amend
git branch
git push -f origin
git cherry-pick
git commit -m "SON5-53650 racol"
git blame -L6441 sync_test.py       
 
git add --all
git reset --hard HEAD
git reset --hard ORIG_HEAD
 
git branch -d <branch_name>

git branch -D <branch_name>
[11:14 AM] Sudhanshu Chaudhary
tar -xvzf ides_ericsson.tar.gz -x
[11:14 AM] Sudhanshu Chaudhary
.
[11:50 AM] Sudhanshu Chaudhary
• You can write to fnfselement@hcl.com for F&F related queries. Please ensure to mention your SAP ID.
[11:50 AM] Sudhanshu Chaudhary
• You can write to fnfselement@hcl.com for F&F related queries. Please ensure to mention your SAP ID.

• For Background verification (BGV) related queries please get in touch with bgv_ex_emp@hcl.com.

• For EVL/PR experience leer please drop mail to EVLSuppo@hcl.com.

• Employee belongs HCLTech (other than C3i and Sankap entity) please get in touch with PFHelpdesk@hcl.com

• Employee belongs to C3i: -For PF Related queries please get in touch with c3ipfstatus@hcl.com

• For Employee belongs to Sankalp entity: For PF Related queries please get in touch with payroll@hcl.com

• For any additional payout/waiver related query, pls. coordinate with your HR Paner.
