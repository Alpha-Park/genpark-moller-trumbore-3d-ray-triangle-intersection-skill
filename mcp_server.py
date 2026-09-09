import sys
import json
from client import MollerTrumboreRayTracer

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "ray_intersect":
        tracer = MollerTrumboreRayTracer()
        return tracer.intersect(params["origin"], params["dir"], params["v0"], params["v1"], params["v2"])
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
