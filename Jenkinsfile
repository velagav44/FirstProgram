pipeline {
    agent any  // Use any available agent, or specify one if needed
    
     stages {
        stage('Connect to AWS') {
            steps {
                // Use AWS credentials in this block
                withAWS(credentials: 'aws-credentials', region: 'us-east-1') {
                 sh 'aws sts get-caller-identity'
                    }
                }
            }
        stage('Run Python Script')
        {
            steps {
                script {
                    sh 'python3 publish_message.py'  
                }
            }
        }
    }
}
