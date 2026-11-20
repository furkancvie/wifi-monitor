import argparse, platform, subprocess, time
p=argparse.ArgumentParser(); p.add_argument('--host',default='1.1.1.1'); a=p.parse_args()
try:
    while True:
        start=time.monotonic()
        args=['ping','-n' if platform.system()=='Windows' else '-c','1',a.host]
        try:
            r=subprocess.run(args,capture_output=True,timeout=5)
            status='reachable' if r.returncode==0 else 'unreachable'
        except subprocess.TimeoutExpired: status='timeout'
        print(time.strftime('%H:%M:%S'),status,flush=True)
        time.sleep(max(0,3-(time.monotonic()-start)))
except KeyboardInterrupt: pass

