from client import MollerTrumboreRayTracer

def main():
    print("=== Moller-Trumbore 3D Ray-Triangle Intersection ===")
    tracer = MollerTrumboreRayTracer()

    # Triangle lying on Z=5 plane
    v0 = [0.0, 0.0, 5.0]
    v1 = [4.0, 0.0, 5.0]
    v2 = [0.0, 4.0, 5.0]

    # Ray shooting from origin along +Z axis
    res = tracer.intersect([1.0, 1.0, 0.0], [0.0, 0.0, 1.0], v0, v1, v2)
    print("Ray Hit Result:", res)
    assert res["hit"] is True
    assert abs(res["distance"] - 5.0) < 1e-4

    print("Moller-Trumbore 3D Intersection verified successfully!")

if __name__ == "__main__":
    main()
