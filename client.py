class MollerTrumboreRayTracer:
    """Fast, memory-efficient 3D ray-triangle intersection using the Moller-Trumbore algorithm."""
    def __init__(self, epsilon: float = 1e-7):
        self.epsilon = epsilon

    def _cross(self, u: list[float], v: list[float]) -> list[float]:
        return [u[1]*v[2] - u[2]*v[1], u[2]*v[0] - u[0]*v[2], u[0]*v[1] - u[1]*v[0]]

    def _dot(self, u: list[float], v: list[float]) -> float:
        return sum(u[i] * v[i] for i in range(3))

    def intersect(self, ray_origin: list[float], ray_dir: list[float],
                  v0: list[float], v1: list[float], v2: list[float]) -> dict:
        edge1 = [v1[i] - v0[i] for i in range(3)]
        edge2 = [v2[i] - v0[i] for i in range(3)]

        h = self._cross(ray_dir, edge2)
        a = self._dot(edge1, h)

        if -self.epsilon < a < self.epsilon:
            return {"hit": False, "reason": "Parallel ray to triangle plane"}

        f = 1.0 / a
        s = [ray_origin[i] - v0[i] for i in range(3)]
        u = f * self._dot(s, h)

        if u < 0.0 or u > 1.0:
            return {"hit": False, "reason": "Intersection outside barycentric u"}

        q = self._cross(s, edge1)
        v = f * self._dot(ray_dir, q)

        if v < 0.0 or u + v > 1.0:
            return {"hit": False, "reason": "Intersection outside barycentric v"}

        t = f * self._dot(edge2, q)

        if t > self.epsilon:
            hit_point = [ray_origin[i] + ray_dir[i] * t for i in range(3)]
            return {
                "hit": True,
                "distance": round(t, 5),
                "hit_point": [round(x, 5) for x in hit_point],
                "barycentric_u": round(u, 5),
                "barycentric_v": round(v, 5),
                "barycentric_w": round(1.0 - u - v, 5)
            }
        return {"hit": False, "reason": "Intersection behind ray origin"}
