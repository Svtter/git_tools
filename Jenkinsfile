pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        timeout(time: 1, unit: 'HOURS')
    }

    // environment {
    // }

    stages {
        stage('build') {
            agent any
            steps {
                sh 'poetry install --no-interaction --no-ansi -vvv'
            }
        }
        stage('lint') {
            agent any
            steps {
                echo 'Pulling...' + env.GIT_BRANCH
                echo 'Path: ' + env.PATH
                sh 'poetry run flake8 --exclude=__init__.py --ignore=E203,E501,W503,W291,E402 --max-line-length=120 src tests'
            }
        }
        stage('test') {
            agent any
            steps {
                // 防止切换文件夹
                sh 'poetry install --no-interaction --no-ansi -vvv'

                // 功能测试
                sh 'poetry run pytest'
            }
        }
    }
}
