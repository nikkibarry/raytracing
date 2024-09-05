# Design Document

---

## Problem Statement

The purpose of this project is to provide a ray tracing library.

---

## Project Scope

### Rendering of simple shapes

The ray tracing library will be able to render the following simple shapes:

- Planes
- Spheres
- Triangles

### Shading

The ray tracing library will utilize Lambertian shading to start.

### Cameras

The ray tracing library will include two types of cameras:

- Pinhole
- Thin-lens approximation

### Textures

The ray tracing library will include the following forms of texturing:

- Color mapping
- Normal mapping

### Sampling

The ray tracing library will provide options for sampling, including:

- Regular Sampling
- Random Sampling
- Jittered Sampling
- N-Rooks Sampling
- Multi-jittered sampling

### Lighting

The library will provide several options for lighting, including:

- Ambient Lights
- Point Lights
- Area Lights
- Directional Lights

---

## Stretch Goals

The following areas are out-of-scope for the minimal loveable product, but may later be added.

### Advanced shapes

A stretch goal is to support advanced shapes, including:

- bounding boxes
- triangle meshes

### Advanced materials

A stretch goal is to move beyond Lambertian shading to include more materials.

### Advanced cameras

A stretch goal is to support advanced cameras, including:

- Stereography
- fish-eye lens

### Advanced lighting models

A stretch goal is to explore advanced lighting models, including:

- Path tracing
- Photon mapping

### Generative Textures

A stretch goal is to explore generative textures, such as:

- Perlin Noise
- Value Noise
- Fractal Noise
- Sine-based noise

---

## Data Model

See [Data Models](data_models.md)

---

## Overview

See [Overview](overview.md)

---

## Packages

- [mathematics](../packages/mathematics/mathematics.md)
