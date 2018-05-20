pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh './build_d.sh'
            }
        }
        stage ('Deploy'){
            steps {
                sh 'ssh admin@www.ghoulmanor.org ./var/www/deploy.sh'   
            }
        }
    }
}
