// This shows a simple example of how to archive the build output artifacts.
def COLOR_MAP = [
    'SUCCESS': 'good',
    'FAILURE': 'danger',
]
pipeline {
    agent {label 'master'}
    environment{
        IMAGE_NAME = "spinnydocker/spinny-web"
        DOCKER_CREDS = 'docker-credentials'
        IMAGE_TAG = 'dev'
    }
    stages {

        stage ("Create build output"){
            steps {
                sh "echo build success!"
            }
        }

        stage ("Pull code"){
            steps {
                 sh "echo code pulled"
            }
        }

        stage ("Pull code"){
            steps {
                sh "echo code pulled"
            }
        }

        stage ("Deploy code"){
            steps {
                sh "echo code pulled"
            }
        }
    }
}