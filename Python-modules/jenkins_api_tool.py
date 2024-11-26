import jenkins
import kubernetes

try:
    server = jenkins.Jenkins('http://18.234.142.87:8080/', username='devops', password='Kwasi1991')
    user = server.get_whoami()
    print(f"User Full Name: {user['fullName']}")
    version = server.get_version()
    print(f"Jenkins Version: {version}")

except Exception as e:
    print(f"Error: {e}")
