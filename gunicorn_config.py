pidfile = 'face-detection-ui.pid'
worker_tmp_dir = '/dev/shm'
worker_class = 'gthread'
workers = 2
worker_connections = 1000
timeout = 30
keepalive = 2
threads = 4
proc_name = 'face-detection-ui'
bind = '0.0.0.0:5006'
backlog = 2048
accesslog = '-'
errorlog = '-'
