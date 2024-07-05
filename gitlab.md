step 1:
#cloning the git repository to local vm
git clone http://10.10.16.125:8989/UserName/gitlabname

you will have gitlab folder in desktop

step2:
#adding local files to gitlab cloned folder

fileExplorer > Drive C:// > Users > Administrator > PycharmProjects > pythonProject > Wipro

step3:
select all [ctrl + a] files copy or cut [ctrl+c / ctrl+x]

step4:
paste [ctrl+v] in gitlab cloned folder which is on desktop

step5:
#checking for file status
git status

step6:
#commiting the files to gitlab repository
git add .
#checking for file status
git status

step7:
#if green
git commit -m "commit message"
#for first time
git config --global user.email "email in the gitlab cred mail" > press enter

git config --global user.name "gitlab username" > press enter

step8:
#pusing the files to gitlab
git push -uf origin main

step9:
#checking for files online
refresh the gitlab