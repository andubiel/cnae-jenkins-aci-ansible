node {
//	
// Clean workspace before doing anything
    deleteDir()

    try {
        stage ('Clone') {
        	checkout scm
        }
        stage ('Build') {
        	sh "ansible-playbook -i hosts-dev.txt playbooks/discover-fabric.yml"
                sh "ansible-playbook -i hosts-dev.txt playbooks/vlan-pool.yml"
                sh "ansible-playbook -i hosts-dev.txt playbooks/vpc-profile.yml"
                sh "ansible-playbook -i hosts-dev.txt playbooks/vmm-domain.yml"
                sh "ansible-playbook -i hosts-dev.txt playbooks/common-tenant.yml"
                sh "ansible-playbook -i hosts-dev.txt playbooks/tenants.yml"
       }

        stage ('Test') {
                sh "ansible-playbook playbooks/cnae.yml"
}
       
        stage ('MergetoMaster') {
                     sh (script: "cd /var/lib/jenkins/workspace/pipeline2 && git checkout master")
                     sh (script: "cd /var/lib/jenkins/workspace/pipeline2 && git branch -u origin/master")
                     sh (script: "cd /var/lib/jenkins/workspace/pipeline2 && git merge origin/dev")
		     sh (script: "cd /var/lib/jenkins/workspace/pipeline2 && git push http://netdevopsuser:network@192.168.1.100:3000/netdevopsuser/jenkins-aci-ansible")        
      }
     stage ('Notification Details') {
            sparkSend credentialsId: 'be3a4748-0434-46ef-a580-a4c286e183b9', message: 'Dev Build Sucessful! Dev Merged to Master:[$JOB_NAME]($BUILD_URL)', messageType: 'text', spaceList: [[spaceId: 'Y2lzY29zcGFyazovL3VzL1JPT00vZTg4Y2M4NjAtMTA0ZS0zMmRjLWEzY2YtMTcxNTcwNzRkMGMw', spaceName: 'NetDevOps CICD Bot']] 
         }
       
         stage ('Configure Production'){
                sh "ansible-playbook -i hosts-prod.txt playbooks/discover-fabric.yml"
                sh "ansible-playbook -i hosts-prod.txt playbooks/vlan-pool.yml"
                sh "ansible-playbook -i hosts-prod.txt playbooks/vpc-profile.yml"
                sh "ansible-playbook -i hosts-prod.txt playbooks/vmm-domain.yml"
                sh "ansible-playbook -i hosts-prod.txt playbooks/common-tenant.yml"
                sh "ansible-playbook -i hosts-prod.txt playbooks/tenants.yml"
       }
     stage ('Notification Details') {
            sparkSend credentialsId: 'be3a4748-0434-46ef-a580-a4c286e183b9', message: 'Prod Build Sucessful! $JOB_NAME]($BUILD_URL)', messageType: 'text', spaceList: [[spaceId: 'Y2lzY29zcGFyazovL3VzL1JPT00vZTg4Y2M4NjAtMTA0ZS0zMmRjLWEzY2YtMTcxNTcwNzRkMGMw', spaceName: 'NetDevOps CICD Bot']]
    } 
    } catch (err) {
         sparkSend credentialsId: 'be3a4748-0434-46ef-a580-a4c286e183b9', message: 'Job Failed! $JOB_NAME]($BUILD_URL) Check CNAE to resolve ACI Configuration  Errors: https://192.168.1.96/#/real-time-change-analysis', messageType: 'text', spaceList: [[spaceId: 'Y2lzY29zcGFyazovL3VzL1JPT00vZTg4Y2M4NjAtMTA0ZS0zMmRjLWEzY2YtMTcxNTcwNzRkMGMw', spaceName: 'NetDevOps CICD Bot']]
        currentBuild.result = 'FAILED'
        throw err
    }
}




