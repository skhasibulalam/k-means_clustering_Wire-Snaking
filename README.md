# k-means clustering (Wire Snaking)
*Building an equal-height tree for sink coordinates*
- The script **cluster.py** loads "sink.txt" file having with 81 coordinates (or as many coordinates you want).
- Then it builds a connected network from origin to *k* number of clusters. You can **change** the number of clusters you want.
- The tree will be of equal height. So wire snaking is used.
### Workflow
- A connected network has to be built, where a signal is to be routed from a source to each 81 sinks.
- After clustering, there will be 5 clusters (5 centroids, assume C1, C2, ..., C5), *probably* each cluster contains 16 sinks.
- Distances from each centroid to sinks need to be measured: (d1, d2, ..., d16 for cluster 1), (d17, d18, ..., d32 for cluster 2), ..., (d65, d66, ..., d81 for cluster 5).
- max(d1, d2, ..., d81) = dmax, is assigned as a height of network.
- Now a path is determined that will assign origin O=(0,0) to common point (X1), then go to each C1, C2, ..., C5. Here X1 is the centroid of all centroids (C1, C2, ..., C5).
- Then C1→p1 with a length dmax, C1→p2 with a length dmax, ..., C5→p80 = dmax, C5→p81 = dmax.
- Eventually, the network is drawn as
  - O→X1→C1, X1→C2, ..., X1→C5
  - C1→p1, C1→p2, ..., C1→p16
  - C2→p17, C2→p18, ..., C2→p32
  - ...
  - C5→p65, C5→p66, ..., C5→p81
