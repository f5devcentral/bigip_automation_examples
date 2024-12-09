
from ansible.errors import AnsibleFilterError

def zip_pools_and_nodes(pools, nodes):
    result = []
    try:
        for pool in pools:
            pool_nodes = []
            for index in pool.get('nodes', []):
                result.append({
                    'pool': pool['name'],
                    'node': nodes[index] 
                })
    except Exception as e:
        raise AnsibleFilterError(f"Error combining pools and nodes: {e}")

    return result

class FilterModule(object):
    def filters(self):
        return {
            'zip_pools_and_nodes': zip_pools_and_nodes
        }
