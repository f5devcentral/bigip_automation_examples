pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    options {
        skipStagesAfterUnstable()
    }

    stages {
        stage('Check Branch') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main' }
                    expression { env.CHANGE_TARGET == 'main' }
                }
            }
            steps {
                echo "Running because branch is main or PR targets main."
            }
        }

        stage('Clone GitHub Repo') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main' }
                    expression { env.CHANGE_TARGET == 'main' }
                }
            }
            steps {
                git url: 'git@github.com:yoctoalex/bigip-demo-jenkins.git', branch: env.BRANCH_NAME
            }
        }

        stage('Terraform Init & Action') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main' }
                    expression { env.CHANGE_TARGET == 'main' }
                }
            }
            steps {
                withCredentials([
                    string(credentialsId: 'terraform-cloud-token', variable: 'TF_TOKEN_app_terraform_io'),
                    string(credentialsId: 'aws-access-key-id', variable: 'AWS_ACCESS_KEY_ID'),
                    string(credentialsId: 'aws-secret-access-key', variable: 'AWS_SECRET_ACCESS_KEY'),
                    string(credentialsId: 'aws-session-token', variable: 'AWS_SESSION_TOKEN'),
                    string(credentialsId: 'bigip-admin-password', variable: 'TF_VAR_bigip_admin_password')
                ]) {
                    dir('terraform') {
                        script {
                            sh 'terraform init'

                            if (env.CHANGE_ID) {
                                echo "🔍 Pull request: plan only"
                                sh '''
                                    terraform plan -input=false -no-color -out=tfplan
                                    terraform show -json tfplan > ../tfplan.json
                                    terraform output -json > ../terraform-output.json
                                '''
                            } else {
                                echo "✅ Apply mode"
                                sh '''
                                    terraform apply -auto-approve -input=false -no-color
                                    terraform output -json > ../terraform-output.json
                                '''
                            }
                        }
                    }
                }
            }
        }

        stage('Generate Ansible Inventory') {
            when {
                anyOf {
                    expression { env.BRANCH_NAME == 'main' }
                    expression { env.CHANGE_TARGET == 'main' }
                }
            }
            steps {
                script {
                    def tfOutput = readJSON file: 'terraform-output.json'
                    def mgmtIp = tfOutput.management_public_ip.value
                    def extIp = tfOutput.external_public_ip.value
                    withCredentials([string(credentialsId: 'bigip-admin-password', variable: 'BIGIP_PASSWORD')]) {
                        writeFile file: 'ansible/inventory.ini', text: """
[bigip]
${mgmtIp} bigip_host=${mgmtIp} bigip_user=admin bigip_password=${BIGIP_PASSWORD}
"""
                    }
                }
            }
        }

        stage('Run Ansible') {
            when {
                allOf {
                    anyOf {
                        expression { env.BRANCH_NAME == 'main' }
                        expression { env.CHANGE_TARGET == 'main' }
                    }
                    expression { fileExists('terraform-output.json') }
                }
            }
            steps {
                script {
                    sh 'ansible-galaxy install -r ansible/requirements.yml'
                    if (env.CHANGE_ID) {
                        echo 'Dry run: ansible-playbook --check'
                        sh "ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --check"
                    } else {
                        echo 'Running full ansible-playbook'
                        sh "ansible-playbook -i ansible/inventory.ini ansible/playbook.yml"
                    }
                }
            }
        }

        stage('Comment on Pull Request') {
            when {
                allOf {
                    expression { env.CHANGE_ID != null }
                    expression { env.CHANGE_TARGET == 'main' }
                }
            }
            steps {
                withCredentials([string(credentialsId: 'github-token', variable: 'GITHUB_TOKEN')]) {
                    script {
                        def planJson = readJSON file: 'tfplan.json'
                        def dangerous = planJson.resource_changes.findAll {
                            def acts = it.change.actions
                            acts.contains("delete") || acts.contains("replace")
                        }.collect {
                            "- ❗ `${it.address}`: ${it.change.actions.join("/")}"
                        }.join("\n")

                        def comment = dangerous ? """
### ⚠️ Potentially Destructive Terraform Changes

${dangerous}

_These resources will be deleted or replaced. Please review carefully._
""" : "✅ No destructive changes detected in Terraform plan."

                        def payload = groovy.json.JsonOutput.toJson([body: comment])
                        def prNumber = env.CHANGE_ID

                        writeFile file: 'gh_comment.json', text: payload

                        withEnv(["GH_TOKEN=${GITHUB_TOKEN}"]) {
                            sh '''
                                curl -s -H "Authorization: token $GH_TOKEN" \
                                    -H "Accept: application/vnd.github.v3+json" \
                                    -X POST \
                                    -d @gh_comment.json \
                                    https://api.github.com/repos/yoctoalex/bigip-demo-jenkins/issues/$CHANGE_ID/comments
                            '''
                        }
                    }
                }
            }
        }

    }

    post {
        always {
            echo "Pipeline completed on branch: ${env.BRANCH_NAME}"
        }
    }
}
