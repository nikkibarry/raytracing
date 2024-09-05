# Mathematics

The `raytracing.mathematics` package includes the basic mathematical classes and functions.

---

## Ray

`Ray` represents a ray in cartesian space.

### Constructor

`class Ray(origin: Vector3, direction: Vector3)`

- `origin` and `direction` are both instance of [`Vector3`](vector3.md)
- `direction` will be normalized on initialization

---

## Vector3

`Vector3` represents either:

- a 3d cartesian coordinate
- a 3d direction

### Constructor

`class Vector3(x: float, y:float, z:float)`

- `x`, `y`, and `z` are all required

### Class attributes

`Vector3.origin`

- returns `Vector3(0.0, 0.0, 0.0)`

### Supported Operations

<style>
table, th, td {
border: 1px solid;
}
</style>

<table>
    <tr>
        <th> Operation </th>
        <th> Type 1 </th>
        <th> Type 2 </th>
        <th> Result </th>
    </tr>
    <tr>
        <td><code>+</code></td>
        <td>Vector3</td>
        <td>Vector3</td>
        <td>Vector3</td>
    </tr>
    <tr>
        <td><code>-</code></td>
        <td>Vector3</td>
        <td>Vector3</td>
        <td>Vector3</td>
    </tr>
    <tr>
        <td><code>==</code></td>
        <td>Vector3</td>
        <td>Vector3</td>
        <td>Equality comparison.</td>
    </tr>
    <tr>
        <td><code>*</code></td>
        <td>Vector3</td>
        <td>Number</td>
        <td>Vector3</td>
    </tr>
    <tr>
        <td><code>/</code></td>
        <td>Vector3</td>
        <td>Number</td>
        <td>Vector3</td>
    </tr>
</table>

### Instance methods

#### `vector3.norm()`

> Return a `Vector3` object with normalized values

#### `vector3.magnitude`

> Return `float` magnitude of the Vector3 object

#### `vector3.dot(vector: Vector3)`

> Return `float` dot product of this `Vector3` object and another `Vector3` object.

#### `vector3.cross(vector: Vector3)`

> Return `Vector3` cross product of this `Vector3` object and another `Vector3` object.
