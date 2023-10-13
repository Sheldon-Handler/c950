from collections import namedtuple

package_tuple = namedtuple('Package', ['package_id', 'address', 'city', 'state', 'postal', 'weight', 'deadline', 'note', 'status'])
status_tuple = namedtuple('Status', ['status_id', 'status'])
